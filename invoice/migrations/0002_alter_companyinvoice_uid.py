# Generated by Django 4.0.3 on 2022-03-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinvoice',
            name='uid',
            field=models.UUIDField(default='fb8b30d567a', editable=False),
        ),
    ]