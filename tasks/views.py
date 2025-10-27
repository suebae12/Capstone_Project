from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # Added base queryset
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Task.objects.filter(user=user)
            
            # Filter by status
            task_status = self.request.query_params.get('status', None)
            if task_status in ['Pending', 'Completed']:
                queryset = queryset.filter(status=task_status)
            
            # Filter by priority
            priority = self.request.query_params.get('priority', None)
            if priority in ['Low', 'Medium', 'High']:
                queryset = queryset.filter(priority=priority)
            
            # Filter by due date
            due_date_filter = self.request.query_params.get('due_date', None)
            if due_date_filter:
                try:
                    from django.utils.dateparse import parse_datetime
                    from django.utils import timezone
                    filter_date = parse_datetime(due_date_filter)
                    if filter_date:
                        queryset = queryset.filter(due_date__date=filter_date.date())
                except:
                    pass
            
            # Sort by priority or due date
            sort_by = self.request.query_params.get('sort_by', None)
            if sort_by == 'due_date':
                queryset = queryset.order_by('due_date')
            elif sort_by == 'priority':
                # Custom ordering for priority
                from django.db.models import Case, When, Value, IntegerField
                queryset = queryset.annotate(
                    priority_order=Case(
                        When(priority='High', then=Value(1)),
                        When(priority='Medium', then=Value(2)),
                        When(priority='Low', then=Value(3)),
                        default=Value(4),
                        output_field=IntegerField(),
                    )
                ).order_by('priority_order')
            else:
                queryset = queryset.order_by('-due_date')  # Default: newest first
            
            return queryset
        return Task.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_status(self, request, pk=None):
        task = self.get_object()
        task_status = request.data.get('status')
        if task_status not in ['Pending', 'Completed']:
            return Response({"error": "Status must be Pending or Completed"}, status=status.HTTP_400_BAD_REQUEST)
        task.status = task_status
        task.save()
        return Response(TaskSerializer(task).data)