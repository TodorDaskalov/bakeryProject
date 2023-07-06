from django.urls import path
from bakeryProject.bakery_main import views
from bakeryProject.bakery_main.views import UserCreationView

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', UserCreationView.as_view(), name='user_register'),
]
