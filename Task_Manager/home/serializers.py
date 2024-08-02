from rest_framework import serializers
from .models import TaskDetails

class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskDetails
        fields = "__all__"


