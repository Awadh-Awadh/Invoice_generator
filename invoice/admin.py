from django.contrib import admin
from .models import CompanyInvoice, AddItems

# Register your models here.
models = [CompanyInvoice, AddItems]

for model in models:
  admin.site.register(model)