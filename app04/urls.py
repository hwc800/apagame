
from django.conf.urls import url

from app04 import views

urlpatterns = [
    url(r'^phone_info', views.select_machine, name='phone_info'),  # 手机信息查询
]
