"""my_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from profile_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^team_index/$', views.home),
    url(r'^name_index/$', views.name),
    url(r'^our_index/$', views.index),
    url(r'^my_index/$', views.profile),
    url(r'^index/$', views.myweb, name = "index"),
    url(r'^myweb/$', views.myweb0, name = "myweb"),
    url(r'^yam/$', views.yam, name = "yam"),
    url(r'^tangmay/$', views.tangmay, name = "tangmay"),
    url(r'^contact/$', views.contact, name = "contact"),
    url(r'^index_o/$', views.index_o, name = "index_o"),
    url(r'^index1_o/$', views.index1_o, name = "index1_o"),
    url(r'^index2_o/$', views.index2_o, name = "index2_o"),
    
]


