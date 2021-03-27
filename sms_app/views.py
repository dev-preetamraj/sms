from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff
from .forms import AddStaffForm


def admin_dashboard(request):
    context = {}
    return render(request, 'app/hod_dashboard.html', context)


def add_staff(request):
    form = AddStaffForm()
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    context = {'form': form}
    return render(request, 'app/add_staff.html', context)
