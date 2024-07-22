from django.urls import path, include
from quicktips import views

app_name = 'quicktips'

urlpatterns = [
    path('quicktips/', views.quicktips_view, name='quicktips_view'),
    path('quicktips/add/', views.add_tip_view, name='add_tip'),
]