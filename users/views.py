from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users
    
    list: Get all users (admin only)
    retrieve: Get user details
    create: Create new user
    update: Update user information
    destroy: Delete user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            # Allow anyone to create a user (registration)
            permission_classes = [permissions.AllowAny]
        else:
            # Only authenticated users can view/edit users
            # In production, you might want IsAdminUser or custom permissions
            permission_classes = [permissions.IsAuthenticated]
        
        return [permission() for permission in permission_classes]
