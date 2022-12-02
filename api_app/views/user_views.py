from .views import *

class UserView(ViewSet):
    def all_user(self, request):
        queryset = User.objects.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        query_data = paginator.paginate_queryset(queryset)
        serializer = UserSerializer(query_data, many=True)
        return response_paginator(
            sum=queryset.count(), 
            per_page=paginator.page_size, 
            data=serializer.data
        )
        
    # register not access
    # def create_user(self, request):
    #     data = request.data.copy()
    #     data_save = UserSerializer(data=data)
    #     if not data_save.is_valid():
    #         return validate_error(data_save.errors)
    #     data_save.save()
    #     return response_data(data=data_save.data)
    
    def edit_user(self, request):
        data = request.data.copy()