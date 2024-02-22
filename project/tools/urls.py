from . import views
from django.urls import path
app_name = 'tools'

urlpatterns = [
    path("reset/cloud", views.cloudByKey, name="cloud"),
    path("reset/pro", views.proByDate, name="pro"),
    path("calculate-energy", views.calculate_energy, name="pro")
    
]
