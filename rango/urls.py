from django.conf.urls import url
from rango import views
from django.urls import path


urlpatterns = [path('', url(r'^$', views.index, name='index'))]