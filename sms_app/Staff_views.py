from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users



def staff_dashboard(req):
    context = {}
    return render(req, 'Staff/dashboard.html', context)


def take_attendance(req):
    context = {}
    return render(req, 'Staff/take_attendance.html', context)


def view_attendance(req):
    context = {}
    return render(req, 'Staff/view_attendance.html', context)


def add_result(req):
    context = {}
    return render(req, 'Staff/add_result.html', context)


def leave(req):
    context = {}
    return render(req, 'Staff/leave.html', context)


def feedback(req):
    context = {}
    return render(req, 'Staff/feedback.html', context)