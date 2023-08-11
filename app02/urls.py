from django.conf.urls import url

from app02 import views

urlpatterns = [
    url(r"^select", views.select, name='select'),  # 版本号查询信息url
    url(r"^build_arges", views.build_arges, name='build_arges'),  # 详细构建参数url
    url(r"^datadb", views.version, name='datadb'),  # 版本号查询信息数据请求url
]
