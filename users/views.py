from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm, PreferenceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Preference


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account has been Created")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, template_name="users/register.html", context={"form": form})


class PreferenceCreateView(LoginRequiredMixin, CreateView):
    model = Preference
    fields = ['genres']
    template_name = 'users/preference.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PreferenceUpdateView(LoginRequiredMixin, CreateView):
    model = Preference
    fields = ['genres']
    template_name = 'users/preference.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
