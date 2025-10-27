# Task Management API

A Django REST Framework API for managing tasks with user authentication, filtering, and sorting capabilities.

## Features

### ✅ Core Functionality
- **Task Management (CRUD)**: Create, read, update, and delete tasks
- **User Management (CRUD)**: Full user management with authentication
- **Task Ownership**: Users can only access their own tasks
- **Task Status Management**: Mark tasks as complete or incomplete
- **Completion Timestamps**: Automatic timestamp tracking for completed tasks
- **Task Filtering**: Filter by status, priority, and due date
- **Task Sorting**: Sort by due date or priority level
- **Task Validation**: 
  - Due dates must be in the future for new tasks
  - Priority levels (Low, Medium, High)
  - Completed tasks cannot be edited unless reverted to pending

### ✅ Technical Implementation
- Django ORM for database interactions
- Django REST Framework for API endpoints
- Session-based authentication
- RESTful API design principles
- Pagination (10 items per page)
- Error handling with appropriate HTTP status codes
- Automatic validation of task data

## API Endpoints

### Base URL
- **Development**: `http://localhost:8000`
- **Production**: [Your Heroku URL]

### Endpoints

#### Root
- `GET /` - API documentation and available endpoints

#### Users
- `GET /api/users/` - List all users (authenticated users only)
- `POST /api/users/` - Create a new user
- `GET /api/users/{id}/` - Retrieve user details
- `PUT /api/users/{id}/` - Update user information
- `DELETE /api/users/{id}/` - Delete a user

#### Tasks
- `GET /api/tasks/` - List user's tasks (requires authentication)
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve task details
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task
- `POST /api/tasks/{id}/mark_status/` - Mark task as complete/incomplete

#### Authentication
- `GET /api-auth/login/` - Login page
- `GET /api-auth/logout/` - Logout

#### Admin
- `GET /admin/` - Django admin panel

### Task Filters

Add query parameters to filter tasks:

```
GET /api/tasks/?status=Completed
GET /api/tasks/?priority=High
GET /api/tasks/?due_date=2024-12-31
GET /api/tasks/?sort_by=due_date
GET /api/tasks/?sort_by=priority
```

You can combine multiple filters:
```
GET /api/tasks/?status=Pending&priority=High&sort_by=priority
```

## Task Model

### Fields
- `id`: Primary key
- `user`: Foreign key to User (read-only)
- `title`: CharField (max 200 characters)
- `description`: TextField (optional)
- `due_date`: DateTimeField
- `priority`: CharField (Low, Medium, High)
- `status`: CharField (Pending, Completed)
- `completed_at`: DateTimeField (auto-set when status becomes Completed)

### Priority Levels
- `Low`: Low priority
- `Medium`: Medium priority (default)
- `High`: High priority

### Status
- `Pending`: Task is not yet completed
- `Completed`: Task is completed

## Installation & Setup

### Prerequisites
- Python 3.13
- pip
- virtualenv (optional but recommended)

### Local Development

1. **Clone the repository**
   ```bash
   cd /path/to/Capstone_Project
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the API**
   - API Root: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - Login: http://localhost:8000/api-auth/login/

## Deployment to Heroku

### Prerequisites
- Heroku CLI installed
- Heroku account

### Deployment Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create a Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY='your-secret-key-here'
   heroku config:set DEBUG=False
   ```

4. **Deploy to Heroku**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **Run migrations on Heroku**
   ```bash
   heroku run python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   heroku run python manage.py createsuperuser
   ```

7. **Access your deployed app**
   ```bash
   heroku open
   ```

## API Usage Examples

### Creating a User
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

### Creating a Task
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "title": "Complete project",
    "description": "Finish the Django project",
    "due_date": "2024-12-31T23:59:00Z",
    "priority": "High"
  }'
```

### Filtering Tasks
```bash
# Get completed tasks
curl http://localhost:8000/api/tasks/?status=Completed

# Get high priority tasks sorted by due date
curl http://localhost:8000/api/tasks/?priority=High&sort_by=due_date
```

## Security Notes

⚠️ **Important for Production**:
- Change `SECRET_KEY` in `settings.py`
- Set `DEBUG = False` in production
- Update `ALLOWED_HOSTS` with your domain
- Use environment variables for sensitive data
- Consider adding HTTPS
- Review Django security best practices

## Project Structure

```
Capstone_Project/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
├── README.md
├── db.sqlite3
├── taskmanager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── tasks/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── admin.py
    ├── apps.py
    └── migrations/
```

## Testing

You can test the API using:
- Browser (for GET requests and authentication)
- Postman
- cURL (command line)
- Python requests library

## Contributing

This is a capstone project demonstrating backend development skills with Django and Django REST Framework.

## License

This project is for educational purposes.

