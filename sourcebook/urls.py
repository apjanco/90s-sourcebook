"""sourcebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from sourcebook_app import views
from django.conf.urls import include
from django.contrib.flatpages import views as flat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('schedule/', flat_views.flatpage, {'url':'/schedule/'}, name='schedule'),
    path('uxdesign/', flat_views.flatpage, {'url':'/uxdesign/'}, name='uxdesign'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('wind/',  views.wind, name='wind'),
    path('people/',  views.people, name='people'),
    path('items/',  views.items, name='items'),
    path('item/<title>', views.item_view, name='item_view'),
]
