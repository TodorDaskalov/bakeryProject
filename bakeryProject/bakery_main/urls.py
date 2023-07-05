from django.urls import path
from bakeryProject.bakery_main import views

urlpatterns = [
    path('', views.home_page, name='home_page')
]
