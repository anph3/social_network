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
        data = request.data.copy()
        validate = FileValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        myfile = request.FILES['file'] 
        name = (datetime.now()).strftime('%d%m%Y%H%M%S') + '.' + str(myfile.name).split('.')[-1]
        fs = FileSystemStorage()
        filename = fs.save(name, myfile)
        uploaded_file_url = fs.url(filename)
        return response_data(uploaded_file_url)