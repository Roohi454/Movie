from django.conf.urls import url
from movieapp import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]
