from django.http import Http404, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Companies
from .serializers import CompaniesSerializer


class CompanyView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        try:
            company = Companies.objects.first()
            serializer_company = CompaniesSerializer(company)

        except ObjectDoesNotExist:
            raise Http404

        return Response(serializer_company.data)

    def post(self, request):
        try:
            serializer_company = CompaniesSerializer(data=request.data)
            if serializer_company.is_valid(raise_exception=True):
                serializer_company.save()
            return Response(serializer_company.data)

        except ValidationError:
            raise HttpResponseBadRequest

    def put(self, request):
        try:
            company_data = get_object_or_404(Companies, id_company=request.data.get('id_company'))
            serializer_company = CompaniesSerializer(company_data, data=request.data)

            if serializer_company.is_valid(raise_exception=True):
                serializer_company.save()
            return Response(serializer_company.data)

        except ObjectDoesNotExist:
            raise Http404

    def delete(self, request, id_company=None):
        try:
            company_data = get_object_or_404(Companies, id_company=id_company)
            company_data.delete()

            return Response()

        except ObjectDoesNotExist:
            raise Http404
