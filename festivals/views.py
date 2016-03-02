from django.shortcuts import render

# List of the festivals
def festival_list(request):
    return render(request, 'festivals/festival_list.html', {})
