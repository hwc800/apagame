from django.conf.urls import url

from app01 import views

urlpatterns = [
    url(r'^ind', views.ind, name='ind'),
    url(r'^zhuye', views.zhuye, name='zhuye'),
    url(r'^up', views.download_template, name='up'),
    url(r'^down', views.down, name='down'),
    url(r'^top', views.connect, name='top'),
    url(r'^main',views.main, name='main'),
    url(r'^url', views.url, name='url'),
]
