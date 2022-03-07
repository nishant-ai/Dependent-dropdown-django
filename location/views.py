from email.policy import default
import time
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Person, Country, State, District, City

# Create your views here.
def home_view(request):
    country = Country.objects.all()
    state = State.objects.none()
    district = District.objects.none()
    city = City.objects.none()
    
    context = {
        'country': country,
        'state': state,
        'district': district,
        'city': city,
    }
    
    if request.method == "POST":
        name = request.POST['name']
        birthdate = request.POST['birthdate']
        form_country = request.POST['form-country']
        form_state = request.POST['form-state']
        form_district = request.POST['form-district']
        form_city = request.POST['form-city']
        
        Person.objects.create(
            name=name,
            birthdate=birthdate,
            country=Country.objects.get(id=form_country),
            state=State.objects.get(name=form_state),
            district=District.objects.get(name=form_district),
            city=City.objects.get(name=form_city)
            )
        
        context['message'] = "Form Submitted Succesfully!"
    
    return render(request, 'location/main.html', context)

def get_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country=country_id)
    return JsonResponse(list(states.values('id', 'name')), safe=False)

def get_districts(request):
    state = request.GET.get('state')
    districts = District.objects.filter(state__name=state)
    return JsonResponse(list(districts.values('id', 'name')), safe=False)

def get_cities(request):
    district = request.GET.get('district')
    cities = City.objects.filter(district__name=district)
    return JsonResponse(list(cities.values('id', 'name')), safe=False)


def user_table(request):
    people = Person.objects.all()
    context = {
        'people': people,
    }
    return render(request, 'location/user_table.html', context)