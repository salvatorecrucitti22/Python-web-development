from modulefinder import IMPORT_NAME
from django.contrib import admin
from django.urls import path
from CRUD import crudviews
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add/', crudviews.add, name = 'add')
]
