from django.shortcuts import render

# Create your views here.
        
from django.shortcuts import render
from django.http import JsonResponse
from .forms import BarcodeForm
from PIL import Image
#pip install Pillow
from pyzbar.pyzbar import decode
#pip install pyzbar

from .models import Student
import cv2
import np

def index(request):
    barcode_data = None
    if request.method == 'POST':
        form = BarcodeForm(request.POST, request.FILES)
        if form.is_valid():
            # barcode_image = form.cleaned_data['barcode_image']
            barcode_image = request.FILES['barcode_image']
            image = Image.open(barcode_image)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            barcodes = decode(image)

            if barcodes:
                barcode_data = barcodes[0].data.decode('utf-8')

                #return JsonResponse({'result': barcode_data})
                if Student.objects.filter(rollno=barcode_data).exists():
                    return JsonResponse({'verified': True, 'message': 'Bus pass is Verified'})
                else:
                    return JsonResponse({'verified': False, 'message': 'Roll number not found'})

            else:
                barcode_data = 'No barcode found'
                #return JsonResponse({'error': 'No barcode found'})
    else:
        form = BarcodeForm()

    return render(request, 'index.html', {'form': form, 'barcode_data': barcode_data})