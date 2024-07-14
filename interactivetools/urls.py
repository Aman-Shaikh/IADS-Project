from django.urls import path
from . import views

urlpatterns = [
    path('searchable-database/', views.searchable_database, name='searchable_database'),
    path('carbon-footprint-calculator/', views.carbon_footprint_calculator, name='carbon_footprint_calculator'),
]
