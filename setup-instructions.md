# GoDaddy Setup Instructions for NX8020™

## Step 1: Database Setup

1. **Login to GoDaddy cPanel**
   - Go to your hosting control panel
   - Find "MySQL Databases" or "phpMyAdmin"

2. **Create Database**
   - Create a new database (e.g., `nx8020_db`)
   - Create a database user with full privileges
   - Note down: database name, username, password

3. **Run SQL Setup**
   - Open phpMyAdmin
   - Select your database
   - Go to "SQL" tab
   - Copy and paste the contents of `database-setup.sql`
   - Click "Go" to execute

## Step 2: Upload Files

1. **Upload PHP Files**
   - Upload `api/` folder to your website root
   - Upload `admin/` folder to your website root
   - Make sure file permissions are set to 644

2. **Update Database Credentials**
   - Edit `api/waitlist.php`
   - Edit `api/demo-interaction.php`
   - Edit `admin/view-prospects.php`
   - Edit `admin/export-prospects.php`
   
   Replace these values:
   ```php
   $username = "your_actual_db_username";
   $password = "your_actual_db_password";
   $dbname = "your_actual_db_name";
   ```

3. **Set Admin Password**
   - Edit `admin/view-prospects.php`
   - Edit `admin/export-prospects.php`
   - Change: `$admin_password = "your_secure_password_here";`

## Step 3: Test the Setup

1. **Test Form Submission**
   - Go to your website
   - Fill out the waitlist form
   - Check if you get success message

2. **Check Database**
   - Go to phpMyAdmin
   - Check if data appears in `nx8020_waitlist` table

3. **Test Admin Panel**
   - Go to `yoursite.com/admin/view-prospects.php`
   - Enter your admin password
   - Verify you can see prospects

## Step 4: Security (Important!)

1. **Protect Admin Files**
   - Add `.htaccess` file in `/admin/` folder:
   ```apache
   AuthType Basic
   AuthName "Admin Area"
   AuthUserFile /path/to/.htpasswd
   Require valid-user
   ```

2. **SSL Certificate**
   - Enable SSL in GoDaddy cPanel
   - Update all URLs to use HTTPS

## Step 5: Monitoring

1. **Check Error Logs**
   - Monitor cPanel error logs
   - Check for PHP errors

2. **Database Backups**
   - Set up automatic backups in cPanel
   - Export data regularly

## Accessing Your Data

- **Admin Dashboard**: `yoursite.com/admin/view-prospects.php`
- **Export CSV**: Click "Export to CSV" in admin dashboard
- **Direct Database**: Use phpMyAdmin in cPanel

## Troubleshooting

- **Form not working**: Check database credentials
- **Admin panel not loading**: Check file permissions
- **No data showing**: Check error logs in cPanel
- **CORS errors**: Make sure API files have proper headers

## File Structure on Server
```
public_html/
├── index.html
├── src/
│   ├── js/main.js
│   └── styles/main.css
├── api/
│   ├── waitlist.php
│   └── demo-interaction.php
└── admin/
    ├── view-prospects.php
    └── export-prospects.php
```