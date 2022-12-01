from rest_framework.response import Response
from configs.variable_response import *
from django.http import JsonResponse

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

def validate_error(data={}):
    # if data == {}:
    #     return response_data(status=STATUS['TOKEN_EXPIRED'], message='ERROR')
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0])
    return response_data(status=STATUS['TOKEN_EXPIRED'], message=error_message)