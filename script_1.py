# Create package.json for QUIZZICLES
package_json = """{
  "name": "quizzicles",
  "version": "2.0.0",
  "description": "Official website for QUIZZICLES - Annual Math & Physics Competition",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js",
    "setup-db": "node config/database-setup.js"
  },
  "keywords": ["quizzicles", "math", "physics", "competition", "students"],
  "author": "QUIZZICLES Team",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "ejs": "^3.1.9",
    "pg": "^8.11.0",
    "dotenv": "^16.3.1",
    "body-parser": "^1.20.2",
    "express-session": "^1.17.3",
    "bcrypt": "^5.1.0",
    "nodemailer": "^6.9.7"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  },
  "engines": {
    "node": ">=16.0.0"
  }
}"""

# Create .env file
env_content = """# QUIZZICLES Environment Configuration
PORT=3000
NODE_ENV=development

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=quizzicles_db
DB_USER=your_username
DB_PASSWORD=your_password

# Session Secret
SESSION_SECRET=your_super_secret_session_key_here

# Email Configuration (for contact form)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

# Site Configuration
SITE_NAME=QUIZZICLES
COMPETITION_YEAR=2025
EDITION_NUMBER=2
"""

# Create .gitignore
gitignore_content = """# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment variables
.env
.env.local
.env.production

# Logs
logs
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# nyc test coverage
.nyc_output

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Temporary files
tmp/
temp/
"""

# Write all configuration files
with open('./quizzicles/package.json', 'w') as f:
    f.write(package_json)

with open('./quizzicles/.env', 'w') as f:
    f.write(env_content)

with open('./quizzicles/.gitignore', 'w') as f:
    f.write(gitignore_content)

print("✅ Configuration files created:")
print("   📄 package.json")
print("   📄 .env")  
print("   📄 .gitignore")