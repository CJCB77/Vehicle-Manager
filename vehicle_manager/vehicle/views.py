from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_input')
        search_criteria = request.POST.get('search_criteria')
        
        # Create dictionary to store search criteria
        search_dict = {search_criteria: search_query}
        if search_criteria == 'id' and not search_query.isdigit():
            return render(request, 'vehicle/index.html', {'error_msg': 'ID must be a number.'})
        else:
            # Filter vehicles based on search criteria
            vehicle = Vehicle.objects.filter(**search_dict).first()

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