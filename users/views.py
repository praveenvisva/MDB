from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .forms import UserRegisterForm
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


class PreferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Preference
    fields = ['genres']
    template_name = 'users/preference.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
