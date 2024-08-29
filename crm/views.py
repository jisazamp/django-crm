from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect("home")
        else:
            messages.error(request, "Something went wrong when trying to sign you in")
            return redirect("home")
    else:
        context = {}
        context['records'] = Record.objects.all();

        return render(request, "home.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    context = {}

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        context["form"] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect("home")

    else:
        form = SignUpForm()
        context["form"] = form

    return render(request, "register.html", context)


def customer_record(request, pk):
    context = {}

    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        context['customer_record'] = customer_record
        return render(request, "record.html", context)
    else:
        messages.error(request, 'You must be logged in to see this page')
        return redirect("home")
    
