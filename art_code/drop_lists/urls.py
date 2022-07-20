from django.urls import path, include
from .views import index, first_choice, second_choice, third_choice

urlpatterns = [
    path('', index, name='lists'),
    path('<slug:choice>/', first_choice, name='first_choice'),
    path('<slug:choice>/<slug:choice_2>/', second_choice, name='second_choice'),
    path('<slug:choice>/<slug:choice_2>/<slug:choice_3>/', third_choice, name='third_choice')
]