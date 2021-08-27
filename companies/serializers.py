from rest_framework import serializers
from .models import Companies


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = '__all__'

    def validate_company_telephone(self, value):
        """
        Check if telephone is number
        """
        tel_fix_blank_spaces = value.replace(" ", "")
        if not tel_fix_blank_spaces.isnumeric():
            raise serializers.ValidationError("Telephone is not valid.")
        return value

    def validate_company_nit(self, nit):
        """
        Check if nit is valid
        :param nit: numeric value where accept only - character for consecutive value
        :return: nit
        """
        nit_fix_accept_value = nit.replace("-", "")
        nit_fix_blank_spaces = nit_fix_accept_value.replace(" ", "")
        if not nit_fix_blank_spaces.isnumeric():
            raise serializers.ValidationError("Nit is not valid.")
        return nit
