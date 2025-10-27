from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'completed_at']
        read_only_fields = ['user', 'completed_at']

    def validate(self, data):
        # Check if this is an update to an existing task
        instance = self.instance
        if instance and instance.status == 'Completed':
            # Only allow reverting to Pending status, no other fields can be changed
            new_status = data.get('status')
            if new_status not in [None, 'Pending']:
                raise serializers.ValidationError(
                    "Cannot edit completed tasks. Change status to 'Pending' first to edit the task."
                )
            # If trying to edit any field other than status (to Pending), block it
            if len(data) > 1 or (len(data) == 1 and 'status' not in data):
                raise serializers.ValidationError(
                    "Cannot modify completed tasks. Only status can be changed to 'Pending'."
                )
        
        # Validate priority
        if 'priority' in data and data['priority'] not in ['Low', 'Medium', 'High']:
            raise serializers.ValidationError("Priority must be Low, Medium, or High.")
        
        # Validate status
        if 'status' in data and data['status'] not in ['Pending', 'Completed']:
            raise serializers.ValidationError("Status must be Pending or Completed.")
        
        return data