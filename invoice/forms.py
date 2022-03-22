from django import forms
from django.forms import ModelForm
from .models import CompanyInvoice, AddItems

class AddCompanyForm(forms.ModelForm):
  class Meta:
    model =CompanyInvoice
    fields = '__all__'


class AddItemsForm(forms.ModelForm):
  class Meta:
    models = AddItems
    fields = [ "item", "description", "unit_cost", "quantity", "total" ]