from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('veteran', views.veteran_list, name='veteran')
]