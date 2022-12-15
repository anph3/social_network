from .views import *
from time import sleep
from django.core.mail import EmailMultiAlternatives


from django.core.files import File

class TestView(ViewSet):
    def sleep_test(self, request):
        data = {
            "name": "Muhammed Ali"
        }
        return response_data(data)