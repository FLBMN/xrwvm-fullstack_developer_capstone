from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class CarMake(models.Model):
    """Model representing a car manufacturer."""
    name = models.CharField(max_length=100, verbose_name="Car Make Name")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"


class CarModel(models.Model):
    """Model representing a car model."""
    car_make = models.ForeignKey(CarMake, 
    on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100, verbose_name="Car Model Name")
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, 
    choices=CAR_TYPES, default='SUV', verbose_name="Car Type")
    year = models.IntegerField(
        default=datetime.now().year,
        validators=[
            MaxValueValidator(datetime.now().year),
            MinValueValidator(2015)
        ],
        verbose_name="Model Year"
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"
