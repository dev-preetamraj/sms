from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView


def staff_dashboard(request):
    context = {}
    return render(request, 'Staff/dashboard.html', context)