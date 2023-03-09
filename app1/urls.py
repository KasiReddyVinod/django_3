from app1.views import *
from django.urls import path
app_name='love'
urlpatterns=[
    path('vinod/',vinod,name='vinod'),
]