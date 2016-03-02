from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.festival_list, name='festival_list'),
]
