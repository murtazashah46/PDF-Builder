from django.contrib import admin
from django.urls import path
from pdfGeneratorApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("convert", views.convertPDF, name='pdfForm')
]