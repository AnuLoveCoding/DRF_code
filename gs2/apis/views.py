from django.shortcuts import render
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser

def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

