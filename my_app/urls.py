from django.urls import path
from .views.fail_request import custom404
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views.game_view import GameView
# from django.conf.urls import (
#     handler400, handler403, handler404, handler500
# )
schema_view = get_schema_view(
    openapi.Info(
        title='api_app API',
        default_version='1.0.0',
        description='API documentation of App',
    ),
    public=True
)

all_url = {
    'url_swagger':[
        path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger')
    ],
    'url_game':[
        path('all-game', GameView.as_view({'get':'all_game'}), name='all_game'),
        
    ],
#     'url_user':[
#         path('all-user', UserView.as_view({'get':'all_user'}), name='all_user'),
#         path('get-user/<int:id>', UserView.as_view({'get':'get_user'}), name='get_user'),
#         path('add-user', AuthView.as_view({'post':'register'}), name='add_user'),
#         path('edit-user/<int:id>', UserView.as_view({'put':'edit_user'}), name='edit_user'),
#         path('restore-user/<int:id>', UserView.as_view({'put':'restore_user'}), name='restore_user'),
#         path('delete-user/<int:id>', UserView.as_view({'put':'delete_user'}), name='delete_user'),
#         path('drop-user/<int:id>', UserView.as_view({'delete':'delete_user'}), name='delete_user'),
#     ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]

handler404 = custom404