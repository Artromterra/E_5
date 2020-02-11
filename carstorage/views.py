from django.shortcuts import render
from .models import Car
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
class CarList(ListView):
	model = Car
	template_name = "car_list.html"

class CarDetailView(ListView):
	model = Car
	template_name = "car_details.html"

	def get_queryset(self):
		query = self.request.GET.get('q')
		try:
			object_list = Car.objects.filter(
				Q(car_model__icontains=query)| 
				Q(manufacturer__icontains=query)|
				Q(transmission_name__icontains=query)|
				Q(color__icontains=query) 
				)
		except Car.DoesNotExist:
			raise Exception("Car does not exist")
		return object_list