from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.forms import CustomerLocationForm

@login_required
def add_location(request):
    if request.method == 'POST':
        form = CustomerLocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user  # Only runs if user is logged in due to @login_required
            location.save()
            return redirect('home')
    else:
        form = CustomerLocationForm()
    return render(request, 'locations/add_locations.html', {'form': form})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Location saved successfully.")
