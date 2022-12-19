from .views import *

class MailView(ViewSet):
    def send_mail(self, request):
        data = request.data.copy()
        validate = MailValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        result = validate.data
        if hp.send_mail(
            subject = result['subject'],
            body = result['body'],
            to = result['to'],
            cc = result['cc'],
            bcc = result['bcc']
        ):
            return response_data(
                message=SUCCESS['send_mail']
            )
        return response_data(
            status=STATUS['FAIL_REQUEST'], 
            message=ERROR['send_mail']
        )
        
    def all_mail(self, request):
        data = request.GET.copy()
        queryset = TemplateMail.objects.filter()
        if vs.TRASH in data:
            if data[vs.TRASH]:
                queryset = queryset.exclude(deleted_at__isnull=True)
            else:
                queryset = queryset.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        query_data = paginator.paginate_queryset(queryset, request=request)
        serializer = MailSerializer(query_data, many=True)
        return response_paginator(
            sum=queryset.count(), 
            per_page=paginator.page_size, 
            data=serializer.data
        )
        
    def get_mail(self, request, id):
        status, data = self.get_mail_data(id)
        if status:
            return response_data(data)
        return validate_error(data)
    
    def get_mail_data(self, id):
        validate = IdMailValidate(data={'id':id})
        if not validate.is_valid():
            return False, validate.errors
        return True, validate.data['data']
    
    def add_mail(self, request):
        data = request.data.copy()
        serializer = MailSerializer(data=data)
        if not serializer.is_valid():
            return validate_error(serializer.errors)
        serializer.save()
        return response_data(serializer.data)
    
    def edit_mail(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_mail_data(id)
        if not status:
            return validate_error(data_id)
        queryset = TemplateMail.objects.get(id=id)
        data_save = MailSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(data_save.data)
    
    def delete_mail(self, request, id):
        status, message = self.status_mail(request, id, datetime.now())
        if not status:
            return validate_error(message)
        return response_data()
    
    def restore_mail(self, request, id):
        status, message = self.status_mail(request, id)
        if not status:
            return validate_error(message)
        return response_data()
    
    def status_mail(self, request, id, data=None):
        status, data_id = self.get_mail_data(id)
        if not status:
            return False, data_id
        queryset = TemplateMail.objects.get(id=id)
        if request.method == vs.DROP_METHOD:
            queryset.delete()
            return True, None
        queryset.deleted_at = data
        queryset.save()
        return True, None