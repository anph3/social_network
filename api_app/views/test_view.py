from .views import *
from time import sleep
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
from django.conf import settings

from django.core.files import File

class TestView(ViewSet):
    def sleep_test(self, request):
        data = {
            "name": "Muhammed Ali"
        }
        return response_data(data)
    
    def read_excel(self, request):
        data = request.data.copy()
        xls = excel.read_excel(request)
        return response_data(xls)
    
    def upload(self, request):
        path_media = "http://" + request.META['HTTP_HOST']+ "/media"
        myfile = request.FILES.getlist('file')
        list_name = []
        for item in myfile:
            name = (datetime.now()).strftime('%d%m%Y%H%M%S') + '.' + str(item.name).split('.')[-1]
            fs = FileSystemStorage()
            filename = fs.save(name, item)
            uploaded_file_url = fs.url(filename)
            list_name.append(path_media + uploaded_file_url)
        return response_data(list_name)
    
    def rm_upload(self, request, id):
        if not str(id).isdigit():
            return response_data(status=2, message='id not found')
        return response_data(id)
    
    def download_file(self, request, id):
        if not str(id).isdigit():
            return response_data(status=2, message='id not found')
        file = open(str(settings.BASE_DIR) + str(settings.MEDIA_URL) + str(id)+'.png', 'rb')
        return StreamingHttpResponse(FileWrapper(file), content_type='application/png')