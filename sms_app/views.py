from django.shortcuts import render


def admin_dashboard(request):
    context = {}
    return render(request, 'app/hod_dashboard.html', context)
