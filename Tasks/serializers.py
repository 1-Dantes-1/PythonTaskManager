from rest_framework import serializers
from .models import Tasks, Tags, Tasks_Tags
# from .models import Tasks, Tags

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', "finished"]
        read_only_fields = ['id']
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'title']
        read_only_fields = ['id']

class TaskTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks_Tags
        fields = ['id', 'task_id', 'tag_id']
        read_only_fields = ['id']
        
