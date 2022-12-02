from django.contrib import admin
from django.urls import path
from .views.auth_views import *
from .views.user_views import *

all_url = {
    'url_auth':[
        path('login', AuthView.as_view({'post':'login'})),
        path('refresh-token', AuthView.as_view({'post':'refresh_token'})),
        path('register', AuthView.as_view({'post':'register'})),
    ],
    'url_in_auth':[
        path('get-data-token', AuthView.as_view({'post':'get_data_token'})),
        path('logout', AuthView.as_view({'post':'logout'})),
    ],
    'url_user':[
        path('all-user', UserView.as_view({'get':'all_user'})),
        path('get-user/<int:id>', UserView.as_view({'get':'get_user'})),
        path('add-user', AuthView.as_view({'post':'register'})),
        path('edit-user/<int:id>', UserView.as_view({'put':'edit_user'})),
        path('delete-user/<int:id>', UserView.as_view({'delete':'delete_user'})),
    ]
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]