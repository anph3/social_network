from .views import *

class GameView(ViewSet):
    def all_game(self, request):
        data = request.GET.copy()
        queryset = Game.objects.filter()
        if 'trash' in data:
            if data['trash']:
                queryset = queryset.exclude(deleted_at__isnull=True)
            else:
                queryset = queryset.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        query_data = paginator.paginate_queryset(queryset, request=request)
        serializer = GameSerializer(query_data, many=True)
        return response_paginator(
            sum=queryset.count(), 
            per_page=paginator.page_size, 
            data=serializer.data
        )