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
    path('ko/<filename>', views.ko, name='ko'),
    path('KO/<year>/<issue>/<date>/', views.kos2, name='kos2'),
    path('KO/<year>/<issue>/', views.kos1, name='kos1'),
    path('KO/<year>/', views.kos0, name='kos0'),
    path('ko_text/<year>/', views.ko_text, name='ko_text'),
    path('all-kos/', views.kos, name='kos'),
    path('datatable/ko/', views.KOListJson.as_view(), name='ko_list_json'),
    path('distant_viewing_json/', views.DistantViewingJson.as_view(), name='distant_viewing_json'),
    path('distant_viewing/', views.distant_viewing, name='distant_viewing'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('network_json/', views.network_json, name='network_json'),
    path('text_summarization/', views.text_summarization, name='text_summarization'),
    path('secret/', views.secret, name='secret'),
]
