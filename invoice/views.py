from django.shortcuts import render, redirect
from .forms import AddCompanyForm, AddItemsForm
from .models import CompanyInvoice
# Create your views here.





def home(request):

  # add comapny logic
  if request.method == "POST":
    form = AddCompanyForm(request.POST)
    form_a = AddItemsForm(request.POST, None)
    if form.is_valid():
      form.save()
      return redirect('invoice')

  # add items logic

    if form_a.is_valid():
      invoice = CompanyInvoice.objects.all()[0]
      obj = form_a.save(commit=False)
      obj.Company_invoice = invoice
      form_a.save()
    
      
  else:
    form = AddCompanyForm()
    form_a = AddItemsForm()

  all_companies = CompanyInvoice.objects.all()
  company = ""
  
  if not all_companies:
    ...
  else:
   company = all_companies[0]
   print(all_companies)

  context = {
    "form":form,
    "form_a":form_a,
    "company": company,
  }

  

  return render(request, "home.html", context)