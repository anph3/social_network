from .views import *
from time import sleep
from django.core.files.storage import FileSystemStorage

class TestView(ViewSet):
    def sleep_test(self, request):
        data = {
            "name": "Muhammed Ali"
        }
        return response_data(data)
    
    def upload(self, request):
        path_media = "http://" + request.META['HTTP_HOST']+ "/media"
        myfile = request.FILES.getlist('file')
        list_name = []
        for item in myfile:
            name = (datetime.now()).strftime('%d%m%Y%H%M%S') + str(item.name)
            fs = FileSystemStorage()
            filename = fs.save(name, item)
            uploaded_file_url = fs.url(filename)
            list_name.append(path_media + uploaded_file_url)
        return response_data(list_name)