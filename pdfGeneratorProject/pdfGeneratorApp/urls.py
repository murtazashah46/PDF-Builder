from django.urls import path
from pdfGeneratorApp import views

urlpatterns = [
    path("pdfForm_Senegal", views.convertPDF_Senegal, name='pdfForm_Senegal'),
    path("pdfForm_IvoryCoast", views.convertPDF_IvoryCoast, name='pdfForm_IvoryCoast'),
    path("pdf_Templates", views.pdf_Templates, name='pdf_Templates')
]