from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        # POST
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            # form valid
            register_form.save()
            messages.success(
                request, ("New User Account Created, Login To Get Started!")
            )
            return redirect("register")
    else:
        # GET
        register_form = CustomRegisterForm()
    return render(request, "register.html", {"register_form": register_form})
