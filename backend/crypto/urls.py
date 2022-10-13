from django.contrib import admin
from django.urls import path, re_path
from .views import get_scraper_data

urlpatterns = [
    re_path(r'^api/', get_scraper_data, name='get_scraper_data'),
]