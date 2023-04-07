from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Model object - single student data
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    # print(stu)
    serializers = StudentSerializer(stu)
    # print(serializers)
    # print(serializers.data)
    json_data = JSONRenderer().render(serializers.data)
    # print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')


# Query - set -> All student data;

def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializers = StudentSerializer(stu, many = True)
    # print(serializers)
    # print(serializers.data)
    json_data = JSONRenderer().render(serializers.data)
    # print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')






