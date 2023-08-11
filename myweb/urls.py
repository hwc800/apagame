"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import app01.urls, app02.urls, app03.urls, app04.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include((app01.urls, 'ind'), namespace='ind')),
    url(r'', include((app02.urls, 'app02'), namespace='app02')),
    url(r'', include((app03.urls, 'app03'), namespace='app03')),
    url(r'', include((app04.urls, 'app04'), namespace='app04')),
]
