from django.urls import path
from app1.views import *

app_name='something'

urlpatterns=[
    path('manu/',manu,name='manu'),
]