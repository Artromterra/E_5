from django.urls import path 
from .views import CarList, CarDetailView

app_name = 'carstorage'
urlpatterns = [
    path('', CarList.as_view(), name='car_list'),
    path('car_details/', CarDetailView.as_view(), name='car_details'),
]