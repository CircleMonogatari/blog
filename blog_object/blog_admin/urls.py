# -- coding: utf-8 --
from django.contrib import admin
from django.urls import path, include

from blog_admin import views

urlpatterns = [
    path('', views.IndexView.as_view(), )

]