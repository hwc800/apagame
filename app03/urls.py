
from django.conf.urls import url

from app03 import views

urlpatterns = [
    url(r'^machine_info', views.select_machine, name='machine_info'),
]
