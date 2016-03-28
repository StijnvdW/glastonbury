from django.conf.urls import url
from .import views

urlpatterns = [
    #index page: festivals/
    url(r'^$', views.festival_list, name='festival_list'),
    #detail page: festivals/1/
    url(r'^festival/(?P<festival_id>[0-9]+)/$', views.festival_detail, name='festival_detail'),
]
