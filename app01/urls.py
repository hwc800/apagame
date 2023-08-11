from django.conf.urls import url

from app01 import views

# 项目组已未使用,可忽略

urlpatterns = [
    url(r'^ind', views.ind, name='ind'),
    url(r'^downloads', views.down_loads, name='downloads'),  # 文件下载，需要将文件移至static目录下
    url(r'^up', views.download_template, name='up'),
    url(r'^down', views.down, name='down'),
    url(r'^top', views.connect, name='top'),
    url(r'^main',views.main, name='main'),  #
    url(r'^url', views.url, name='url'),  # 符号表下载
]
