from rest_framework import serializers
from .models import Companies


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        exclude = ['id_company']
