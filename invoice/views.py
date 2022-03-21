from django.shortcuts import render
from .forms import AddCompanyForm

# Create your views here.



def home(request):
  if request.method == "POST":
    form = AddCompanyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = AddCompanyForm()

  context = {
    "form":form
  }


  return render(request, "home.html", context)