# DataProStudio Inc. - Corporate Website

A professional corporate website for **DataProStudio Inc.**, a strategic data consultancy specializing in high-impact data platforms for mid-to-large enterprises.

## Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Industry-Specific Solutions**: Tabbed interface showcasing sector expertise
- **Lead Capture**: Comprehensive consultation request form
- **Performance Optimized**: Fast loading with video optimization
- **SEO Ready**: Proper meta tags and semantic HTML structure

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask API
- **Database**: MySQL 8.0+
- **Fonts**: Montserrat (headings), Open Sans (body text)
- **Video**: Optimized background video with mobile fallbacks

## Setup Instructions

### 1. Database Setup (MySQL)

1. Create a MySQL database for the project:
   ```sql
   CREATE DATABASE dataproStudio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. Run the SQL script in `database/setup.sql` to create the necessary tables:
   ```bash
   mysql -u your_username -p dataproStudio_db < database/setup.sql
   ```

3. Update the database configuration in `api/consultation.py`

### 2. Backend Configuration

1. Install Python dependencies:
   ```bash
   pip install flask flask-cors mysql-connector-python
   ```

2. Update database credentials in `api/consultation.py`:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'database': 'dataproStudio_db',
       'user': 'your_username',
       'password': 'your_password',
       'port': 3306
   }
   ```

3. Run the Flask application:
   ```bash
   python api/consultation.py
   ```

### 3. Frontend Deployment

1. Upload all files to your web server
2. Ensure the API endpoint is accessible at `/api/consultation`
3. Test the contact form functionality

## Project Structure

```
dataproStudio/
├── index.html              # Main landing page
├── src/
│   ├── styles/
│   │   └── main.css        # Main stylesheet
│   └── js/
│       └── main.js         # JavaScript functionality
├── api/
│   └── consultation.py     # Flask API for form handling
├── database/
│   └── setup.sql          # MySQL database schema
└── README.md              # This file
```

## Key Sections

1. **Hero Section**: Video background with compelling value proposition
2. **Our Expertise**: Six core service areas with detailed descriptions
3. **Sector Solutions**: Industry-specific solutions with tabbed interface
4. **Our Approach**: Four-step methodology visualization
5. **Contact Form**: Comprehensive lead capture with validation
6. **Footer**: Additional navigation and company information

## Business Goals

- Generate 10+ qualified leads within 90 days
- Achieve 60%+ user engagement (scroll depth)
- Build prospect database for future marketing

## Target Personas

- **CFOs**: Focus on ROI, compliance, and cost reduction
- **Supply Chain Directors**: Emphasis on operational efficiency
- **CTOs**: Technical architecture and scalability solutions

## Database Schema

### consultation_requests
- `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
- `name` (VARCHAR(255), NOT NULL)
- `company` (VARCHAR(255), NOT NULL)
- `email` (VARCHAR(255), NOT NULL)
- `industry` (VARCHAR(100))
- `message` (TEXT, NOT NULL)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- `updated_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
- `source` (VARCHAR(100), DEFAULT 'website_contact_form')
- `user_agent` (TEXT)
- `referrer` (VARCHAR(500))
- `status` (ENUM: 'new', 'contacted', 'qualified', 'converted', 'closed')
- `notes` (TEXT)

### analytics_events
- `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
- `event_name` (VARCHAR(100), NOT NULL)
- `properties` (JSON)
- `timestamp` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- `session_id` (VARCHAR(100))
- `user_agent` (TEXT)
- `ip_address` (VARCHAR(45))
- `page_url` (VARCHAR(500))
- `referrer` (VARCHAR(500))

## API Endpoints

### POST /api/consultation
Submit a consultation request.

**Request Body:**
```json
{
  "name": "John Smith",
  "company": "Acme Corp",
  "email": "john@acme.com",
  "industry": "financial-services",
  "message": "We need help with data architecture..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Consultation request submitted successfully",
  "id": 123
}
```

### GET /api/consultation/stats
Get consultation statistics (admin only).

**Headers:**
```
Authorization: Bearer admin_access_token_2025
```

**Response:**
```json
{
  "total_requests": 45,
  "by_industry": [
    {"industry": "financial-services", "count": 15},
    {"industry": "technology", "count": 12}
  ],
  "recent_requests": [...]
}
```

## Performance Features

- Optimized video loading with mobile fallbacks
- Lazy loading for images and animations
- Compressed assets for fast loading
- Progressive enhancement for older browsers

## Analytics & Tracking

The website includes built-in analytics tracking for:
- Page load times
- Scroll depth measurement
- Form interactions
- Tab engagement
- Error monitoring

## Security Features

- Input sanitization for all form fields
- SQL injection prevention
- CORS configuration
- Basic rate limiting (implement as needed)

## Customization

### Colors
Update CSS variables in `src/styles/main.css`:
```css
:root {
  --primary-color: #0D1B2A;
  --accent-color: #00B8D4;
  /* ... other variables */
}
```

### Content
- Update company information in `index.html`
- Modify service descriptions and industry solutions
- Customize form fields as needed

### Branding
- Replace logo and company name throughout
- Update meta tags and SEO information
- Customize email templates (if implementing)

## Deployment Checklist

- [ ] MySQL database created and configured
- [ ] API endpoints tested
- [ ] Contact form validation working
- [ ] Video loading optimized
- [ ] Mobile responsiveness verified
- [ ] SEO meta tags updated
- [ ] Analytics tracking implemented
- [ ] Error handling tested
- [ ] Performance optimization complete

## Environment Variables

For production deployment, consider using environment variables:

```bash
# Database Configuration
DB_HOST=localhost
DB_NAME=dataproStudio_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=3306

# Security
ADMIN_TOKEN=your_secure_admin_token
SECRET_KEY=your_flask_secret_key
```

## Support

For technical support or customization requests, please refer to the project documentation or contact the development team.

## License

This project is proprietary to DataProStudio Inc. All rights reserved.