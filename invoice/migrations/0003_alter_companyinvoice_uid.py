# Generated by Django 4.0.3 on 2022-03-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_companyinvoice_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinvoice',
            name='uid',
            field=models.CharField(default='7ff23bbc25b', editable=False, max_length=255),
        ),
    ]