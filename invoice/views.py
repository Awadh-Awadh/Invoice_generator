from django.shortcuts import render, redirect
from .forms import AddCompanyForm
from .models import CompanyInvoice
# Create your views here.



def home(request):

  # add comapny logic
  if request.method == "POST":
    form = AddCompanyForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('invoice')
  else:
    form = AddCompanyForm()

  all_companies = CompanyInvoice.objects.all()
  company = ""
  
  if not all_companies:
    ...
  else:
   company = all_companies[0]
   print(all_companies)

  # add items logic
  

  context = {
    "form":form,
    "company": company
  }

  

  return render(request, "home.html", context)