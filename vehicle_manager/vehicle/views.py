from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from django.db.models import Q


# Create your views here.
def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_input')
        if search_query.isdigit():
            vehicle = Vehicle.objects.filter(pk=search_query).first()
        else:
            vehicle = Vehicle.objects.filter(serial_number=search_query).first()

        context = {'vehicle': vehicle} if vehicle else {'error_msg': 'No vehicle found.'}
        return render(request, 'vehicle/index.html', context)
    return render(request, 'vehicle/index.html')