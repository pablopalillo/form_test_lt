from django.test import TestCase
from companies.models import Companies
from companies.serializers import CompaniesSerializer


class TestCompaniesView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Companies.objects.create(
            company_name="Nestle",
            company_address="Calle 50c # 34 -45",
            company_telephone="32323232",
            company_nit="23232323"
        )

    def test_company_accessible(self):
        resp = self.client.get("/company")
        self.assertTrue(resp.status_code, 200)