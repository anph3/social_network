from rest_framework.response import Response
from configs.variable_response import *
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from math import ceil

def data_response(data=None, status=1, message="Success"):
    return {
        'status_code': status,
        'message': message,
        'data': data
    }

def response_data(data=None, status=1, message="Success"):
    return Response(data_response(data, status, message))

def json_response(data=None, status=1, message="Success"):
    return JsonResponse(data_response(data, status, message))

def response_paginator(sum, per_page, data):
    result = {
        'max_page': ceil(sum/per_page),
        'list_data': data
    }
    return response_data(data=result)

def validate_error(data={}, status=STATUS['INPUT_INVALID']):
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0]) + '<br/>'
    return response_data(status=status, message=error_message)