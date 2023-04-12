from django.shortcuts import render
from rest_framework.decorators import api_view
# from django.http import HttpResponse
from rest_framework.response import Response


# @api_view(['GET']) # ! (['GET']) It is default;
# def hello_world(request):
#     return Response({'msg': 'Hello World'})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({'msg': 'This is POST Request'})

# @api_view(['PUT'])
# def hello_world(request):
#     if request.method == 'PUT':
#         return Response({'msg': 'This is PUT Request'})

# @api_view(['DELETE'])
# def hello_world(request):
#     if request.method == 'DELETE':
#         return Response({'msg': 'This is DELETE Request'})

@api_view(['GET','POST','PUT','DELETE'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is GET Request'})
    elif request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is POST Request','data': request.data})
    elif request.method == 'PUT':
        return Response({'msg': 'This is PUT Request'})
    elif request.method == 'PATCH':
        return Response({'msg': 'This is PATCH Request'})
    elif request.method == 'DELETE':
        return Response({'msg': 'This is DELETE Request'})
    else:
        return Response({'msg': 'Invalid Request Method'})
