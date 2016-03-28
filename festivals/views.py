from django.shortcuts import render
from .models import Festival

# List of the festivals
def festival_list(request):
    festivals = Festival.objects.all()
    return render(request, 'festivals/festival_list.html', {'festivals': festivals})

def festival_detail(request, festival_id):
    festival = Festival.objects.get(pk=festival_id)
    return render(request, 'festivals/festival_detail.html', {'festival': festival})
