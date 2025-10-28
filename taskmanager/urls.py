"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from tasks.views import TaskViewSet, task_list_html


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)  

# Root view to show welcome page
def api_root(request):
    return render(request, 'base.html')

# API documentation endpoint for JSON response
def api_docs(request):
    return JsonResponse({
        'message': 'Task Manager API',
        'version': '1.0',
        'documentation': {
            'admin': '/admin/',
            'api_root': '/api/',
            'authentication': '/api-auth/login/',
            'endpoints': {
                'users': {
                    'list_create': 'GET, POST /api/users/',
                    'retrieve_update_delete': 'GET, PUT, DELETE /api/users/{id}/',
                },
                'tasks': {
                    'list_create': 'GET, POST /api/tasks/',
                    'retrieve_update_delete': 'GET, PUT, DELETE /api/tasks/{id}/',
                    'mark_status': 'POST /api/tasks/{id}/mark_status/',
                    'filters': {
                        'status': '?status=Pending or ?status=Completed',
                        'priority': '?priority=Low, Medium, or High',
                        'due_date': '?due_date=YYYY-MM-DD',
                        'sort_by': '?sort_by=due_date or ?sort_by=priority',
                    }
                }
            },
            'note': 'All endpoints require authentication. Use /api-auth/login/ to authenticate.'
        }
    })

#this is the url that helps us with authentication
urlpatterns = [
    path('', api_root, name='root'),
    path('api-docs/', api_docs, name='api-docs'),  # JSON documentation
    path('tasks/', task_list_html, name='tasks-html'),  # Mobile-friendly task list
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
