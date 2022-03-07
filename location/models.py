from operator import mod
from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=220)
    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=220)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        
class District(models.Model):
    name = models.CharField(max_length=220)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=220)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Cities'
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=220)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'People'