from django.urls import path
from configs.variable_system import FILES
from .views.auth_views import *
from .views.user_views import *
from .views.media_view import *
from .views.test_view import *
from .views.fail_request import custom404
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
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
    'url_auth':[
        path('login', AuthView.as_view({'post':'login'}), name='login'),
        path('refresh-token', AuthView.as_view({'post':'refresh_token'}), name='refresh_token'),
        path('register', AuthView.as_view({'post':'register'}), name='register'),
    ],
    'url_in_auth':[
        path('get-data-token', AuthView.as_view({'get':'get_data_token'}), name='get_data_token'),
        path('logout', AuthView.as_view({'post':'logout'}), name='logout'),
    ],
    'url_user':[
        path('all-user', UserView.as_view({'get':'all_user'}), name='all_user'),
        path('get-user/<int:id>', UserView.as_view({'get':'get_user'}), name='get_user'),
        path('add-user', AuthView.as_view({'post':'register'}), name='add_user'),
        path('edit-user/<int:id>', UserView.as_view({'put':'edit_user'}), name='edit_user'),
        path('restore-user/<int:id>', UserView.as_view({'put':'restore_user'}), name='restore_user'),
        path('delete-user/<int:id>', UserView.as_view({'put':'delete_user'}), name='delete_user'),
        path('drop-user/<int:id>', UserView.as_view({'delete':'delete_user'}), name='delete_user'),
    ],
    'url_media':[
        path('upload', MediaView.as_view({'post': 'upload'}), name='upload'),
        path('rm-upload/<str:id>', MediaView.as_view({'post': 'rm_upload'}), name='rm_upload'),
        path(
            FILES['download_file'] + '/<str:id>',
            MediaView.as_view({'get': 'download_file'}),
            name='download_file'
        ),  
    ],
    'url_test':[
        path('sleep_test', TestView.as_view({'post': 'sleep_test'}), name='sleep_test'),
    ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]

handler404 = custom404