from django.urls import path, include
from vacancies import views

urlpatterns = [
    path('', view=views.main),
]
