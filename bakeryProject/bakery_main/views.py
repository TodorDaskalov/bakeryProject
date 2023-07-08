from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from bakeryProject.bakery_main.forms import UserRegistrationForm
from bakeryProject.bakery_main.models import Profile, BakeryUser


def home_page(request):
    return render(request, 'home_page.html')


class UserCreationView(CreateView):
    template_name = 'register_user.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.set_password(form.cleaned_data['password1'])
        user.save()

        user = authenticate(
            self.request, username=form.cleaned_data['email'], password=form.cleaned_data['password1']
        )
        login(self.request, user)

        Profile.objects.create(user=user)

        return redirect(self.success_url)


class LoginUserView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home_page')


class LogoutUserView(LogoutView):
    next_page = 'home_page'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['first_name', 'last_name', 'phone_number']

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = BakeryUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('home_page')
