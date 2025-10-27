# Deployment Guide for Task Manager API

## Deploy to Heroku

### Prerequisites
- Heroku CLI installed
- Git installed
- Heroku account

### Step 1: Login to Heroku
```bash
heroku login
```

### Step 2: Create Heroku App
```bash
heroku create your-task-manager-api
```

### Step 3: Set Environment Variables
```bash
heroku config:set SECRET_KEY='your-secret-key-here'
heroku config:set DEBUG=False
heroku config:set DJANGO_SETTINGS_MODULE=taskmanager.settings
```

### Step 4: Initialize Git and Deploy
```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

### Step 5: Run Migrations on Heroku
```bash
heroku run python manage.py migrate
```

### Step 6: Create Admin User
```bash
heroku run python manage.py createsuperuser
```

### Step 7: Collect Static Files
```bash
heroku run python manage.py collectstatic --noinput
```

### Step 8: Open Your App
```bash
heroku open
```

## Deploy to PythonAnywhere

### Step 1: Upload Your Files
1. Upload your project folder to PythonAnywhere
2. Or use git to clone your repository

### Step 2: Set Up Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.13 venv
pip install -r requirements.txt
```

### Step 3: Configure Web App
1. Go to Web tab in PythonAnywhere dashboard
2. Create a new web app
3. Set the source code path to your project
4. Set working directory to project root

### Step 4: Set WSGI Configuration
Edit the WSGI file to point to your project:
```python
import os
import sys

path = '/home/yourusername/Capstone_Project'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 5: Run Migrations
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

### Step 6: Reload Web App
Click the Reload button in the Web tab

## Security Checklist for Production

- [ ] Change SECRET_KEY to a strong random value
- [ ] Set DEBUG = False
- [ ] Update ALLOWED_HOSTS with your domain
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/SSL
- [ ] Set up proper database (PostgreSQL for Heroku)
- [ ] Review Django security checklist: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

## Testing Your Deployment

After deployment, test these endpoints:
- https://your-app.herokuapp.com/ (or PythonAnywhere URL)
- https://your-app.herokuapp.com/api/
- https://your-app.herokuapp.com/api-auth/login/
- https://your-app.herokuapp.com/admin/

## Troubleshooting

### If migrations fail:
```bash
heroku run python manage.py migrate
```

### If static files don't work:
```bash
heroku run python manage.py collectstatic --noinput
```

### To see logs:
```bash
heroku logs --tail
```

### To run Python shell on Heroku:
```bash
heroku run python manage.py shell
```

