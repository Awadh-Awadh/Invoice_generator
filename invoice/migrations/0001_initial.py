# Generated by Django 4.0.3 on 2022-03-22 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('invoice_date', models.DateField()),
                ('balance_due', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('uid', models.CharField(blank=True, editable=False, max_length=11, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='AddItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('descrition', models.TextField()),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=40)),
                ('quantity', models.IntegerField()),
                ('total', models.CharField(editable=False, max_length=255)),
                ('Company_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.companyinvoice')),
            ],
            options={
                'verbose_name': 'AddItem',
            },
        ),
    ]
