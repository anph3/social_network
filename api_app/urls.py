from django.urls import path
from .views.auth_views import *
from .views.user_views import *
from .views.test_view import *
from .views.fail_request import custom404
# from django.conf.urls import (
#     handler400, handler403, handler404, handler500
# )

all_url = {
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
    'url_test':[
        path('sleep_test', TestView.as_view({'post': 'sleep_test'}), name='sleep_test'),
    ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]

handler404 = custom404