from django.http import JsonResponse


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'message': 'The urls was not found'
    })