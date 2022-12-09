from .views import *
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper


class MediaView(ViewSet):
    def upload(self, request):
        data_user = get_user_info(request=request)
        path_media = 'http://' + request.META['HTTP_HOST'] + '/download-file/'
        myfile = request.FILES.getlist('file')
        list_name = []
        for item in myfile:
            name = str(data_user['id']) + (datetime.now()).strftime('%d%m%Y%H%M%S') + '.' + str(item.name).split('.')[-1]
            fs = FileSystemStorage()
            file_name = fs.save(name, item)
            path_file = str(fs.url(file_name)).split('/')[-1]
            list_name.append(path_media + path_file)
        return response_data(list_name)
    
    def rm_upload(self, request, id):
        # validate
        validate = FileDownloadValidate(data={'id':str(id)})
        if not validate.is_valid():
            return validate_error(validate.errors)
        # file = validate.data
        os.remove(os.path.join(settings.MEDIA_ROOT, id))
        return response_data()
    
    def download_file(self, request, id):
        # validate
        validate = FileDownloadValidate(data={'id':str(id)})
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        # path file
        path_file = "{}{}{}.{}".format(
            str(settings.BASE_DIR),
            str(settings.MEDIA_URL),
            validate.data['id'],
            validate.data['type']
        )
        
        # open file
        file = open(path_file, 'rb')
        
        # return file
        return StreamingHttpResponse(
            FileWrapper(file),
            content_type='application/'+
            validate.data['type']
        )