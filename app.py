import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import logging
from datetime import datetime
import hashlib

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration - UPDATE WITH YOUR GODADDY DETAILS
DB_CONFIG = {
    'host': 'localhost',  # Usually localhost on GoDaddy
    'database': 'your_db_name',  # From GoDaddy cPanel
    'user': 'your_db_username',  # From GoDaddy cPanel
    'password': 'your_db_password',  # From GoDaddy cPanel
    'port': 3306,
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        logger.error(f"Database connection error: {e}")
        return None

def validate_email(email):
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/api/waitlist', methods=['POST', 'OPTIONS'])
def add_to_waitlist():
    """Add prospect to waitlist"""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
    
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not data.get('name') or not data.get('email'):
            return jsonify({'error': 'Name and email are required'}), 400
        
        name = data['name'].strip()
        email = data['email'].strip().lower()
        language = data.get('language', 'es')
        
        # Validate email format
        if not validate_email(email):
            return jsonify({'error': 'Invalid email address'}), 400
        
        # Connect to database
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        # Check if email already exists
        check_query = "SELECT id FROM nx8020_waitlist WHERE email = %s"
        cursor.execute(check_query, (email,))
        
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({'error': 'Email already exists'}), 409
        
        # Insert new prospect
        insert_query = """
            INSERT INTO nx8020_waitlist (name, email, language, created_at) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, email, language, datetime.now()))
        connection.commit()
        
        prospect_id = cursor.lastrowid
        
        cursor.close()
        connection.close()
        
        # Log successful signup
        logger.info(f"New waitlist signup: {name} ({email}) - Language: {language}")
        
        return jsonify({
            'success': True, 
            'message': 'Successfully added to waitlist',
            'id': prospect_id
        }), 201
        
    except Exception as e:
        logger.error(f"Waitlist error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/demo-interaction', methods=['POST', 'OPTIONS'])
def log_demo_interaction():
    """Log demo interaction for analytics"""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
    
    try:
        data = request.get_json()
        
        session_id = data.get('session_id', '')
        input_text = data.get('input', '')
        response_type = data.get('response_type', 'unknown')
        language = data.get('language', 'es')
        
        # Connect to database
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        # Insert demo interaction
        insert_query = """
            INSERT INTO nx8020_demo_interactions 
            (session_id, input_text, response_type, language, created_at) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (session_id, input_text, response_type, language, datetime.now()))
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return jsonify({'success': True}), 200
        
    except Exception as e:
        logger.error(f"Demo interaction error: {e}")
        return jsonify({'error': 'Failed to log interaction'}), 500

@app.route('/admin/prospects')
def view_prospects():
    """Admin endpoint to view prospects (password protected)"""
    
    # Simple password protection
    auth_header = request.headers.get('Authorization')
    if not auth_header or not verify_admin_password(auth_header):
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        # Get prospects
        cursor.execute("SELECT * FROM nx8020_waitlist ORDER BY created_at DESC")
        prospects = cursor.fetchall()
        
        # Get demo interactions count
        cursor.execute("SELECT COUNT(*) as total FROM nx8020_demo_interactions")
        demo_count = cursor.fetchone()['total']
        
        # Get interactions by type
        cursor.execute("""
            SELECT response_type, COUNT(*) as count 
            FROM nx8020_demo_interactions 
            GROUP BY response_type
        """)
        interaction_types = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return jsonify({
            'prospects': prospects,
            'stats': {
                'total_prospects': len(prospects),
                'total_interactions': demo_count,
                'interaction_breakdown': interaction_types,
                'conversion_rate': round((len(prospects) / demo_count * 100), 2) if demo_count > 0 else 0
            }
        })
        
    except Exception as e:
        logger.error(f"Admin prospects error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/admin/export')
def export_prospects():
    """Export prospects as CSV"""
    
    # Simple password protection
    auth_header = request.headers.get('Authorization')
    if not auth_header or not verify_admin_password(auth_header):
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT name, email, language, created_at FROM nx8020_waitlist ORDER BY created_at DESC")
        prospects = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        # Convert to CSV format
        import csv
        import io
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write headers
        writer.writerow(['Name', 'Email', 'Language', 'Date'])
        
        # Write data
        for prospect in prospects:
            writer.writerow([
                prospect['name'],
                prospect['email'],
                prospect['language'],
                prospect['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            ])
        
        csv_content = output.getvalue()
        output.close()
        
        return csv_content, 200, {
            'Content-Type': 'text/csv',
            'Content-Disposition': f'attachment; filename=nx8020-prospects-{datetime.now().strftime("%Y%m%d")}.csv'
        }
        
    except Exception as e:
        logger.error(f"Export error: {e}")
        return jsonify({'error': 'Export failed'}), 500

def verify_admin_password(auth_header):
    """Verify admin password from Authorization header"""
    try:
        # Expected format: "Bearer your_password"
        if not auth_header.startswith('Bearer '):
            return False
        
        password = auth_header.split(' ')[1]
        expected_password = "your_secure_admin_password"  # CHANGE THIS!
        
        return password == expected_password
    except:
        return False

@app.route('/health')
def health_check():
    """Health check endpoint"""
    try:
        connection = get_db_connection()
        if connection:
            connection.close()
            return jsonify({'status': 'healthy', 'database': 'connected'}), 200
        else:
            return jsonify({'status': 'unhealthy', 'database': 'disconnected'}), 500
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)