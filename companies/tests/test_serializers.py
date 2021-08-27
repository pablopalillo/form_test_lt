from django.test import TestCase
from companies.models import Companies
from companies.serializers import CompaniesSerializer


class TestCompaniesSerializer(TestCase):

    @classmethod
    def setUpTestData(cls):
        Companies.objects.create(
            company_name="Nestle",
            company_address="Calle 50c # 34 -45",
            company_telephone="32323232",
            company_nit="23232323"
        )

    def test_serializer_valid_data(self):
        company_data = Companies.objects.values().first()
        serializer_employee = CompaniesSerializer(data=company_data)

        self.assertTrue(serializer_employee.is_valid())
