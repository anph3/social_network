from rest_framework.response import Response
from configs.variable_response import *
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from math import ceil

def response_data(data=None, status=1, message="Success"):
    result = {
        'status_code': status,
        'message': message,
        'data': data
    }
    return Response(result)

def json_response(data=None, status=1, message="Success"):
    result = {
        'status_code': status,
        'message': message,
        'data': data
    }
    return JsonResponse(result)

def response_paginator(sum, per_page, data):
    result = {
        'max_page': ceil(sum/per_page),
        'list_data': data
    }
    return response_data(data=result)

def validate_error(data={}, status=STATUS['INPUT_INVALID']):
    # if data == {}:
    #     return response_data(status=STATUS['TOKEN_EXPIRED'], message='ERROR')
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0]) + '<br/>'
    return response_data(status=status, message=error_message)