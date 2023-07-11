from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from todo.models import Todo
from todo.serializers import TodoCreateSerializer, TodoUpdateSerializer

import json

class TodoAPIView(APIView):
    
    
    #추가
    def post(self, request):
        request.data["writer"] = request.user.email#writer추가
        #추가 작업
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"resultCode":200,"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"resultCode":500, "data":None}, status=status.HTTP_400_BAD_REQUEST)
    
	#수정
    def put(self, request, pk):
        #todo = get_object_or_404(Todo, id=pk)
        todo = Todo.objects.get(id=pk)

        if todo.writer != str(request.user): #작성자 일치여부 확인
            return Response({"resultCode":500}, status=status.HTTP_400_BAD_REQUEST)
        
        #수정작업
        serializer = TodoUpdateSerializer.update(instance=todo, validated_data=request.data)
        
        result = {}
        result["title"] = serializer.title
        result["year"] = serializer.year
        result["month"] = serializer.month
        result["day"] = serializer.day
        result["title"] = serializer.title
        result["color"] = serializer.color #color
        result["description"] = serializer.description #description
        result["time"] = serializer.time #time
        result["id"] = serializer.id #id
        if str(serializer.done) == "1":
            result["done"] = True #done
        elif str(serializer.done) == "0":
            result["done"] = False
        else:
            result["done"] = serializer.done

        return Response({"resultCode":200,"data":result}, status=status.HTTP_200_OK)
    #삭제
    def delete(self, request, pk):
        todo = Todo.objects.get(id=pk)
        print(todo)
        
        if todo.writer != str(request.user): #작성자 일치여부 확인
            return Response({"resultCode":500}, status=status.HTTP_400_BAD_REQUEST)
        
        #삭제작업
        todo.delete()
        return Response({"resultCode":200}, status=status.HTTP_200_OK)