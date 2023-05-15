from django.conf.urls import url

from app02 import views

urlpatterns = [
    url(r"^select", views.select, name='select'),
    url(r"^arges_mesg", views.arges_mesg, name='arges_mesg'),
    url(r"^build_arges", views.build_arges, name='build_arges'),
    url(r"^datadb", views.version, name='datadb'),
    url(r"^json_arges", views.build_arges, name='json_arges'),
]
