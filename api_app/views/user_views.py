from .views import *

class UserView(ViewSet):
    def all_user(self, request):
        queryset = User.objects.filter(deleted_at__isnull=True)
        serializer = UserSerializer(queryset, many=True)
        return response_data(serializer.data)