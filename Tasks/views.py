from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from Tasks.models import Tasks, Tags, Tasks_Tags
from .serializers import TagSerializer, TaskSerializer, TaskTagSerializer

class TaskAPIView(APIView):
    def get(self, request: Request):
        c = Tasks.objects.all()      
        for value in request.query_params:
            if value == 'id':
                if len(request.query_params[value]):
                    c = Tasks.objects.filter(id = request.query_params['id'])
                    return Response({"Tasks: ": TaskSerializer(c, many=True).data})
                raise Exception("Didnt took value for id") 
        return Response({"Tasks": TaskSerializer(c, many=True).data})
    
    def post(self,request:Request):
        ser = TaskSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        tag = get_object_or_404(Tags, pk=request.data.get('tag'))
        task_new = Tasks.objects.create (
            id = request.data['id'],
            title = request.data['title'],
            description = request.data['description'],
            tag = tag,
            finished = request.data['finished']
        )
        return Response({"Tasks":TaskSerializer(task_new).data})

class RelationAPIView(APIView):
    def get(self, request: Request):
        c = Tasks_Tags.objects.all()      
        for value in request.query_params:
            if value == 'task_id':
                if len(request.query_params[value]):
                    c = Tasks_Tags.objects.filter(task_id = request.query_params[value])
                    return Response({f"Tasks with task_id: {request.query_params[value]} " : TaskTagSerializer(c, many=True).data})
                raise Exception("Didnt took value for id")
            if value == 'tag_id':
                if len(request.query_params[value]):
                        c = Tasks_Tags.objects.filter(tag_id = request.query_params[value])
                        return Response({f"Tasks with tag_id: {request.query_params[value]} " : TaskTagSerializer(c, many=True).data})
                raise Exception("Didnt took value for id")
                
        return Response({"Tasks": TaskTagSerializer(c, many=True).data})
    
    def post(self,request:Request):
        ser = TagSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        tag_new = Tags.objects.create(
            title = request.data['title']
        )
        return Response({"Tags":TagSerializer(tag_new).data})