from django.urls import path

from . import views


urlpatterns = [
   path('company', views.CompanyView.as_view()),
   path('company/<int:id_company>', views.CompanyView.as_view()),
]
