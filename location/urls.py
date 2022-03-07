from turtle import home
from django.urls import path
from .views import *

urlpatterns = [
    # Add User
    path('', home_view, name="home-view"),
    path('get-states', get_states, name="get-states"),
    path('get-districts', get_districts, name="get-districts"),
    path('get-cities', get_cities, name="get-cities"),
    # User Table
    path('user-table/', user_table, name="user-table"),
]
