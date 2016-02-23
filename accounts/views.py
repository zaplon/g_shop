from django.shortcuts import render, render_to_response
from .forms import LoginForm


def login_view(request):
    form = LoginForm()
    return render_to_response('accounts/login.html', {'form': form})