from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_datetime),
    path('table/', views.multiplication_table),
    path('day/', views.programmers_day),
]
