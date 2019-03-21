from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from django.http import Http404

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskList(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""
class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class TaskDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            task = Task.objects.filter(pk=pk)
            return task
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)



