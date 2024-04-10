from django.urls import path
from .views import property_ads,create_property,view_single_property
urlpatterns = [
    path('',property_ads,name='rental_home'),
    path('create_ad/',create_property,name='create_ad'),
    path('property/<slug:slug>/', view_single_property, name='view_single_property'),

]
