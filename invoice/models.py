from django.db import models
import uuid

# Create your models here.

def modify(token):
  new_token = token[:12]
  return new_token.replace('-', "")
  
          


class CompanyInvoice(models.Model):
    uid = modify(str(uuid.uuid4()))
    uid = models.CharField(default=uid,
                          editable=False,
                          max_length=255)

    company_name = models.CharField(max_length=255)
    invoice_date = models.DateField()
    balance_due = models.IntegerField()
    address =  models.CharField(max_length=255)

    # @property
    # def uuid(self):
    #    uid = str(uuid.uuid1())
    #    return uid.replace("-", "")[:12]

    
    class Meta:
        ordering = ['-pk']
    def __str__(self) -> str:
        return self.company_name

    


class AddItems(models.Model):
    item = models.CharField(max_length=255)
    descrition = models.TextField()
    unit_cost = models.DecimalField(decimal_places=2, max_digits=40)
    quantity = models.CharField(max_length=255)
    Company_invoice = models.ForeignKey(CompanyInvoice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "AddItem"

    def __str__(self):
        return self.item
