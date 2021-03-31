from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.index,name='index.html'),
    path('slogin', views.slogin,name='slogin.html'),
    path('Plogins', views.Plogins,name='Plogins.html'),
    path('spersonalinfo', views.spersonalinfo,name='spersonalinfo.html'),
    path('academics', views.academics,name='academics.html'),
    path('certifications', views.certifications,name='certifications.html'),
    path('proctor', views.proctor,name='proctor.html'),
]
