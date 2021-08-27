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
        serializer_company = CompaniesSerializer(data=company_data)

        self.assertTrue(serializer_company.is_valid())

    def test_serializer_validate_nit(self):
        company_data = Companies.objects.values().first()
        company_data.company_nit = "2314413-2" # valid NIT

        serializer_company = CompaniesSerializer(data=company_data)
        self.assertTrue(serializer_company.is_valid())

        company_data.company_nit = "2314413LLKB-2"  # Not valid NIT
        serializer_company = CompaniesSerializer(data=company_data)
        self.assertFalse(serializer_company.is_valid())
