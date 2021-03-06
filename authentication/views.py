from django.shortcuts import render, redirect
from .forms import AdminCreationForm, VoluntereCreationForm, UserCreationForm
# Create your views here.


def register_admin(request):
    if request.POST:
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.is_admin = True
            d.save()
            return redirect('authentication:login')
    form = AdminCreationForm()

    context = {'form': form}

    return render(request, 'authentication/register_admin.html', context)


def register_voluntere(request):
    if request.POST:
        form = VoluntereCreationForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.is_voluntere = True
            d.save()
            return redirect('authentication:login')
    form = VoluntereCreationForm()

    context = {'form': form}

    return render(request, 'authentication/register_voluntere.html', context)


def register_user(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.is_user = True
            d.save()
            return redirect('authentication:login')
    form = UserCreationForm()

    context = {'form': form}

    return render(request, 'authentication/register_user.html', context)


def error(request, *args):
    return render(request, '404.html')
