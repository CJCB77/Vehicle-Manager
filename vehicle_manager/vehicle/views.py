from django.shortcuts import render, get_object_or_404
from .models import Vehicle

# Create your views here.
def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_input')
        vehicle = Vehicle.objects.filter(pk=search_query).first()
        if vehicle:
            context = {'vehicle': vehicle}
        else:
            context = {'error_msg': 'No vehicle found with that ID. Please try again.'}
        return render(request, 'vehicle/index.html', context)
    return render(request, 'vehicle/index.html')