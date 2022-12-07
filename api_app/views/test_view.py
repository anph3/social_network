from .views import *
from time import sleep

class TestView(ViewSet):
    def sleep_test(self, request):
        data = {
            "name": "Muhammed Ali"
        }
        return response_data(data)