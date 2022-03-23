from django.urls import path
from .views import home


urlpatterns = [
  
  path("", home, name="invoice"),
  path("print", print, name='print')
  
  
  ]