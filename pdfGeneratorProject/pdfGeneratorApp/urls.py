from django.urls import path
from pdfGeneratorApp import views

urlpatterns = [
    path("convert", views.convertPDF, name='pdfForm')
]