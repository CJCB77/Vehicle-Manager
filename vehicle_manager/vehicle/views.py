from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone

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

def download_vehicle_pdf(request, vehicle_id):
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'
    
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    current_user = request.user
    current_date = timezone.now()
    context = {'vehicle': vehicle, 'current_user': current_user, 'current_date': current_date}
    source_html = get_template('vehicle/reports/vehicle_report.html').render(context)
    
    # create a pdf
    pisa_status = pisa.CreatePDF(
       source_html, dest=response
    )
        # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('Error with the download')
    return response