from django.http import HttpResponse
from django.shortcuts import redirect, render



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='hod').exists():
                return redirect('hod_dashboard')
            elif request.user.groups.filter(name='staff').exists():
                return redirect('staff_dashboard')
            else:
                return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                if request.user.groups.all()[0].name == 'hod':
                    return redirect('hod_dashboard')
                elif request.user.groups.all()[0].name == 'staff':
                    return redirect('staff_dashboard')
                else:
                    return redirect('dashboard')
                # return render(request, 'accounts/notallowed.html', {})
        return wrapper_func
    return decorator

def hod_only():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name='hod'):
                return view_func(request, *args, **kwargs)
            elif request.user.groups.filter(name='staff'):
                return redirect('staff_dashboard')
            else:
                return redirect('dashboard')
        return wrapper_func
    return decorator