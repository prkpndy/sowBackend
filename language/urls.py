from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("terms/", views.terms, name="terms"),
  path("us/", views.us, name="us"),
  path("navigation/", views.navigation, name="navigation"),
  path("pricelist/", views.pricelist, name="pricelist")
]