from django.urls import path
from bakeryProject.bakery_main import views
from bakeryProject.bakery_main.views import UserCreationView, LoginUserView, LogoutUserView, ProfileDetailView, \
    ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', UserCreationView.as_view(), name='user_register'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:pk>`/delete/', ProfileDeleteView.as_view(), name='user_delete')
]
