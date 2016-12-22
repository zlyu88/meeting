from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.log_in, name='log_in'),

    url(r'^base/(?P<uid>\d+)/$', views.base, name='base'),
    url(r'^room_page/(?P<rid>\d+)/$', views.room_page, name='room_page'),

]
