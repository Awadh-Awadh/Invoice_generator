from django.db import models
import uuid

# Create your models here.


class CompanyInvoice(models.Model):
    company_name = models.CharField(max_length=255)
    invoice_date = models.DateField()
    balance_due = models.IntegerField(max_length=255)
    address =  models.CharField(max_length=255)

    @property
    def uuid(self):
       uid = str(uuid.uuid1())
       return uid.replace("-", "")[:12]


class AddItems(models.Model):
    item = models.CharField(max_length=255)
    descrition = models.TextField()
    unit_cost = models.DecimalField(decimal_places=40)
    quantity = models.CharField(max_length=255)
    Company_invoice = models.ForeignKey(CompanyInvoice, on_delete=models.CASCADE)