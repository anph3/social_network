from .views import *
from time import sleep
from console.queues.sleep_queue import *

class TestView(ViewSet):
    def sleep_test(self, request):
        data = {
            "name": "Muhammed Ali"
        }
        return response_data(data)