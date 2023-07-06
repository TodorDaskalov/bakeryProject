from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from bakeryProject.bakery_main.forms import UserRegistrationForm


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

        return redirect(self.success_url)


class LoginUserView():
    pass


class LogoutUserView():
    pass


