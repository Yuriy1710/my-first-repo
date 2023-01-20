from django.urls import path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='nenu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
