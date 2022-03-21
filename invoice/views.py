from django.shortcuts import render, redirect
from .forms import AddCompanyForm
from .models import CompanyInvoice
# Create your views here.



def home(request):
  if request.method == "POST":
    form = AddCompanyForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('invoice')
  else:
    form = AddCompanyForm()

  companies = CompanyInvoice.objects.all()[0]
  print(companies)

  context = {
    "form":form,
    "company": companies
  }

  

  return render(request, "home.html", context)