from django.shortcuts import render
from .models import Festival

# List of the festivals
def festival_list(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/festival_list.html', {'festivals': festivals})
