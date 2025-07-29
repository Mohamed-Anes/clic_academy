from django.urls import path
from .views.dict import search


urlpatterns = [
    path('search', search, name='search'),

]
