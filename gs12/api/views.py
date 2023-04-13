from django.shortcuts import render
# ! from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class StudentAPI(APIView):
    def get(self, request, format = None, pk = None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created'}, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def put(self, request,pk , format = None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Complete Data Updated'})
        else:
            return Response(serializer.errors)

    def patch(self, request,pk, format = None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated'})
        else:
            return Response(serializer.errors)

    def delete(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg' : 'Data Deleted'})

        



# @api_view(['GET', 'POST', 'PUT','PATCH','DELETE'])
# def student_api(request, pk = None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         else:
#             stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data Created'}, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)

    # if request.method == 'PUT':
        # id = pk
        # stu = Student.objects.get(pk = id)
        # serializer = StudentSerializer(stu, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'msg' : 'Complete Data Updated'})
        # else:
        #     return Response(serializer.errors)

    # if request.method == 'PATCH':
        # id = pk
        # stu = Student.objects.get(pk = id)
        # serializer = StudentSerializer(stu, data=request.data, partial = True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'msg' : 'Partial Data Updated'})
        # else:
        #     return Response(serializer.errors)


    # if request.method == 'DELETE':
    #     id = pk
    #     stu = Student.objects.get(pk = id)
    #     stu.delete()
    #     return Response({'msg' : 'Data Deleted'})





           

    