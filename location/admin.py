from django.contrib import admin
from .models import Country, State, District, City, Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'state', 'city']

admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Person, PersonAdmin)