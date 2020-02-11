from django.db import models

# Create your models here.
# class Transmission(models.Model):
#     MECHANICS = 1
#     AUTOMAT = 2
#     ROBOT = 3
#     CAR_TRANSMISSION_CHOICES = [
#         (MECHANICS, 'Механика'),
#         (AUTOMAT, 'Автомат'),
#         (ROBOT, 'Робот'),
#     ]
#     transmission_name = models.SmallIntegerField(choices=CAR_TRANSMISSION_CHOICES, default="1")

class Car(models.Model):
	car_model = models.CharField(max_length=50)
	release = models.IntegerField()
	manufacturer = models.CharField(max_length=50)
	MECHANICS = 1
	AUTOMAT = 2
	ROBOT = 3
	CAR_TRANSMISSION_CHOICES = [
		(MECHANICS, 'Механика'),
		(AUTOMAT, 'Автомат'),
		(ROBOT, 'Робот'),
	]
	transmission_name = models.SmallIntegerField(choices=CAR_TRANSMISSION_CHOICES, default="1")
	color = models.CharField(max_length=50)

	def __str__(self):
		return self.manufacturer

