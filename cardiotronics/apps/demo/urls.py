from django.urls import path, include
from demo.views import *

urlpatterns = [
    path('', index, name="index"),
]
