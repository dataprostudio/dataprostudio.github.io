# DataProStudio Inc. - Setup Guide

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dataproStudio-website.git
   cd dataproStudio-website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

4. **Set up database**
   - Create a Supabase project at https://supabase.com
   - Run the migrations in `supabase/migrations/`
   - Update your environment variables

5. **Start development server**
   ```bash
   npm run dev
   ```

## Database Setup

### Using Supabase (Recommended)

1. Create a new project at [Supabase](https://supabase.com)
2. Go to the SQL Editor in your Supabase dashboard
3. Run the migration file: `supabase/migrations/20250629041430_graceful_meadow.sql`
4. Update your `.env` file with the Supabase credentials

### Using Local MySQL (Alternative)

1. Install MySQL 8.0+
2. Create a database: `CREATE DATABASE dataproStudio_db;`
3. Update the database configuration in `api/consultation.py`
4. Run the Flask API: `python api/consultation.py`

## Environment Variables

Create a `.env` file in the root directory:

```env
# Supabase Configuration
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key

# For local MySQL (if not using Supabase)
DB_HOST=localhost
DB_NAME=dataproStudio_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=3306

# Admin Access
ADMIN_TOKEN=your_secure_admin_token
```

## Deployment

### Netlify (Frontend)
1. Connect your GitHub repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Add environment variables in Netlify dashboard

### Supabase (Backend)
- Database and API are automatically handled by Supabase
- Edge functions can be deployed using Supabase CLI

## Project Structure

```
dataproStudio-website/
├── src/
│   ├── styles/main.css      # Main stylesheet
│   └── js/main.js          # JavaScript functionality
├── api/
│   └── consultation.py     # Flask API (if using local MySQL)
├── supabase/
│   └── migrations/         # Database migrations
├── dist/                   # Built files (auto-generated)
├── index.html             # Main landing page
├── package.json           # Dependencies and scripts
├── README.md             # Project documentation
└── .env.example          # Environment variables template
```

## Features

- ✅ Responsive design for all devices
- ✅ Professional corporate styling
- ✅ Industry-specific solutions showcase
- ✅ Lead capture form with validation
- ✅ Database integration (Supabase/MySQL)
- ✅ Performance optimized
- ✅ SEO ready

## Support

For questions or issues, please refer to the documentation or create an issue in the GitHub repository.