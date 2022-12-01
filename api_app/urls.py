from django.contrib import admin
from django.urls import path
from .views.auth_views import *

urlpatterns = [
    path('login', AuthView.as_view({'post':'login'})),
    path('refresh-token', AuthView.as_view({'post':'refresh_token'})),
    path('get-data-token', AuthView.as_view({'post':'get_data_token'})),
    path('create_token', AuthView.as_view({'post':'create_token'})),
]