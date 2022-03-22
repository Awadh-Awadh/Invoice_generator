from django.shortcuts import render, redirect
from .forms import AddCompanyForm, AddItemsForm
from .models import CompanyInvoice, AddItems
# Create your views here.





def home(request):

  # add comapany form logic
  if request.method == "POST":
    form = AddCompanyForm(request.POST)
    form_a = AddItemsForm(request.POST, None)
    if form.is_valid():
      form.save()
      return redirect('invoice')

  # add items form logic

    if form_a.is_valid():
      invoice =""
      invoices = CompanyInvoice.objects.all()
      if invoices:
         invoice = invoices[0]
      else:
        ...
      obj = form_a.save(commit=False)
      obj.Company_invoice = invoice
      form_a.save()
    
      
  else:
    form = AddCompanyForm()
    form_a = AddItemsForm()

  # Displaying the most recent company details
  all_companies = CompanyInvoice.objects.all()
  company = ""  
  if not all_companies:
    ...

  else:
   company = all_companies[0]
   print(all_companies)

  # Display table details for items

  items = AddItems.objects.all()
  print(items)

  context = {
    "form":form,
    "form_a":form_a,
    "company": company,
    "items": items
  
  }

  

  return render(request, "home.html", context)