from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Companies
from .serializers import CompaniesSerializer


class CompanyView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            company = Companies.objects.first()
            serializer_company = CompaniesSerializer(company)

        except ObjectDoesNotExist:
            raise Http404

        return Response(serializer_company.data)
