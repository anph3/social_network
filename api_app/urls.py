from django.contrib import admin
from django.urls import path
from .views.auth_views import *
from .views.user_views import *

url_auth = [
    path('login', AuthView.as_view({'post':'login'})),
    path('refresh-token', AuthView.as_view({'post':'refresh_token'})),
]

url_in_auth = [
    path('get-data-token', AuthView.as_view({'post':'get_data_token'})),
]

url_user = [
    path('all-user/<int:id>', UserView.as_view({'get':'all_user'})),
]

urlpatterns = []

urlpatterns += url_auth + url_in_auth + url_user