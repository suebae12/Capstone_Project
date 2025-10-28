from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    completed_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        # Only validate due date if task is not completed
        if self.status != 'Completed':
            # Allow some grace period (1 minute) to account for timing differences
            if self.due_date < (timezone.now() - timedelta(minutes=1)):
                raise ValidationError("Due date must be in the future.")

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'Completed':
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


