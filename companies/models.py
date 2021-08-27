from django.db import models


class Companies(models.Model):
    id_company = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=15)
    company_address = models.CharField(max_length=30)
    company_telephone = models.CharField(max_length=15)
    company_nit = models.CharField(max_length=10)
