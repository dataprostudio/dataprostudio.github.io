# GoDaddy Flask Setup Guide for NX8020™

## Prerequisites
- GoDaddy hosting account with Python support
- cPanel access
- SSH access (recommended)

## Step 1: Enable Python App on GoDaddy

1. **Login to cPanel**
   - Go to your GoDaddy hosting control panel
   - Find "Setup Python App" or "Python Selector"

2. **Create Python Application**
   - Click "Create Application"
   - Python Version: 3.8+ (latest available)
   - Application Root: `/public_html` (or subdirectory)
   - Application URL: Leave blank for root domain
   - Application Startup File: `passenger_wsgi.py`
   - Click "Create"

## Step 2: Database Setup

1. **Create MySQL Database**
   - In cPanel, go to "MySQL Databases"
   - Create database: `nx8020_db` (or your preferred name)
   - Create user with full privileges
   - Note: database name, username, password

2. **Run Database Setup**
   - Open phpMyAdmin
   - Select your database
   - Import or run the SQL from `database-setup.sql`

## Step 3: Upload and Configure Files

1. **Upload Files via File Manager or FTP**
   ```
   public_html/
   ├── app.py
   ├── passenger_wsgi.py
   ├── requirements.txt
   ├── .htaccess
   ├── index.html
   ├── src/
   └── admin/
   ```

2. **Update Database Configuration**
   Edit `app.py` and update the DB_CONFIG section:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'database': 'your_actual_db_name',
       'user': 'your_actual_db_user',
       'password': 'your_actual_db_password',
       'port': 3306,
       'charset': 'utf8mb4',
       'collation': 'utf8mb4_unicode_ci'
   }
   ```

3. **Set Admin Password**
   In `app.py`, find and change:
   ```python
   expected_password = "your_secure_admin_password"  # CHANGE THIS!
   ```

## Step 4: Install Python Dependencies

1. **Via cPanel Python App**
   - Go back to "Setup Python App"
   - Click on your application
   - In the "Configuration" section, add packages:
     - Flask==2.3.3
     - Flask-CORS==4.0.0
     - mysql-connector-python==8.1.0

2. **Via SSH (if available)**
   ```bash
   cd /home/yourusername/public_html
   pip install -r requirements.txt
   ```

## Step 5: Configure URL Routing

The `.htaccess` file should handle routing:
```apache
PassengerEnabled On
PassengerAppRoot /home/yourusername/public_html
PassengerAppType wsgi
PassengerStartupFile passenger_wsgi.py
PassengerPython /usr/bin/python3

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} ^/api/
RewriteRule ^(.*)$ passenger_wsgi.py/$1 [QSA,L]

RewriteCond %{REQUEST_FILENAME} -f
RewriteRule ^(.*)$ $1 [L]
```

## Step 6: Test the Setup

1. **Test Website**
   - Visit your domain
   - Check if the landing page loads

2. **Test API Endpoints**
   - Try submitting the waitlist form
   - Check if demo interactions work

3. **Test Admin Dashboard**
   - Go to `yourdomain.com/admin/dashboard.html`
   - Login with your admin password

## Step 7: Monitor and Troubleshoot

1. **Check Error Logs**
   - In cPanel, go to "Error Logs"
   - Look for Python/Flask errors

2. **Common Issues**
   - **500 Error**: Check file permissions (644 for files, 755 for directories)
   - **Database Connection**: Verify credentials in `app.py`
   - **Module Not Found**: Ensure all dependencies are installed

## Step 8: Security Hardening

1. **SSL Certificate**
   - Enable SSL in cPanel
   - Force HTTPS redirects

2. **Secure Admin Access**
   - Use strong admin password
   - Consider IP restrictions for admin panel

3. **Database Security**
   - Use strong database passwords
   - Limit database user privileges

## API Endpoints

Once deployed, your API will be available at:

- **POST** `/api/waitlist` - Add prospect to waitlist
- **POST** `/api/demo-interaction` - Log demo interaction
- **GET** `/admin/prospects` - View prospects (password protected)
- **GET** `/admin/export` - Export prospects CSV (password protected)
- **GET** `/health` - Health check

## Admin Dashboard

Access your admin dashboard at:
`https://yourdomain.com/admin/dashboard.html`

Features:
- View all prospects
- See demo interaction statistics
- Export data to CSV
- Monitor conversion rates

## Data Management

Your prospect data will be stored in MySQL tables:
- `nx8020_waitlist` - Prospect information
- `nx8020_demo_interactions` - Demo usage analytics

## Support

If you encounter issues:
1. Check GoDaddy's Python app documentation
2. Review error logs in cPanel
3. Test database connectivity via phpMyAdmin
4. Verify file permissions and paths

## File Permissions

Set correct permissions:
- Files: 644
- Directories: 755
- Python files: 644 (executable via passenger)