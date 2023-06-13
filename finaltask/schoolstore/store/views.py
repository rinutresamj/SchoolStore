from django.shortcuts import render
from .forms import UserProfileForm
from django.contrib import messages
from . models import Department,Course
# Create your views here.
def home(request):
    return render(request,'home.html')
def postlogin(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Order Confirmed")

    else:
        form = UserProfileForm()

    return render(request, 'postlogin.html', {'form': form})

