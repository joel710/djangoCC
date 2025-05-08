
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_views, name='Home'),
    path('contact/', views.contact_views),
    path('article/', views.article_views),
]
