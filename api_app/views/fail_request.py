from helpers.response import *


def custom404(request, exception=None):
    return json_response(
        status=404,
        message='The urls was not found'
    )