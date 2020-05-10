from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.index, name='index'),
    path('world', views.nice, name='index'),
    path('baidu', views.webTest, name='index'),
    path('api', views.apiTest, name='index')
]