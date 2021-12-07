from urllib import request
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('doc', views.generate_docx, name='doc'),
    path('download1', views.download11, name='download1'),
    path('download2', views.download22, name='download2'),
    path('download3', views.download33, name='download3'),
    path('admin/', admin.site.urls),
    path('checkboxes', views.savevalues, name='checkbx')
]
