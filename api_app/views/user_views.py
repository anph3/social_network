from .views import *

class UserView(ViewSet):
    def all_user(self, request):
        data = request.GET.copy()
        queryset = User.objects.filter()
        if vs.TRASH in data:
            if data[vs.TRASH]:
                queryset = queryset.exclude(deleted_at__isnull=True)
            else:
                queryset = queryset.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        query_data = paginator.paginate_queryset(queryset, request=request)
        serializer = UserSerializer(query_data, many=True)
        return response_paginator(request, 
            sum=queryset.count(), 
            per_page=paginator.page_size, 
            data=serializer.data
        )
        
    def get_user(self, request, id):
        status, data = self.get_user_data(id)
        if status:
            return response_data(request, data)
        return validate_error(request, data)
    
    def get_user_data(self, id):
        validate = IdGetUserValidate(data={'id':id})
        if not validate.is_valid():
            return False, validate.errors
        return True, validate.data['data']
        
    # register not access
    # def create_user(self, request):
    #     data = request.data.copy()
    #     data_save = UserSerializer(data=data)
    #     if not data_save.is_valid():
    #         return validate_error(request, data_save.errors)
    #     data_save.save()
    #     return response_data(request, data=data_save.data)
    
    def edit_user(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_user_data(id)
        if not status:
            return validate_error(request, data_id)
        queryset = User.objects.get(id=id)
        data_save = UserSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(request, data_save.errors)
        data_save.save()
        return response_data(request, data_save.data)
    
    def delete_user(self, request, id):
        status, message = self.status_user(request, id, datetime.now())
        if not status:
            return validate_error(request, message)
        return response_data(request, )
    
    def restore_user(self, request, id):
        status, message = self.status_user(request, id)
        if not status:
            return validate_error(request, message)
        return response_data(request, )
    
    def status_user(self, request, id, data=None):
        status, data_id = self.get_user_data(id)
        if not status:
            return False, data_id
        queryset = User.objects.get(id=id)
        if request.method == vs.DROP_METHOD:
            queryset.delete()
            return True, None
        queryset.deleted_at = data
        queryset.save()
        return True, None
        