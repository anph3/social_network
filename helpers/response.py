from rest_framework.response import Response
from configs.variable_response import *
from django.http import *
from console.jobs import queue_logger as lg
from math import ceil

def data_response(request, data=None, status=1, message='Success'):
    
    
    
    return {
        'status_code': status,
        'message': message,
        'data': data
    }

def response_data(request, data=None, status=1, message='Success'):
    return Response(data_response(request, data, status, message))

def json_response(request, data=None, status=1, message='Success'):
    return JsonResponse(data_response(request, data, status, message))

def response_paginator(request, sum, per_page, data):
    result = {
        'max_page': ceil(sum/per_page),
        'list_data': data
    }
    return response_data(request, data=result)

def validate_error(request, data={}, status=STATUS['INPUT_INVALID']):
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0]) + '<br/>'
    return response_data(request, status=status, message=error_message)

def custom404(request, exception=None):
    return json_response(request, status=404, message=ERROR['404'])