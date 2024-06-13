# from django import forms
# from .models import UploadedImage
# 
# class ImageUploadForm(forms.ModelForm):
    # class Meta:
        # model = UploadedImage
        # fields = "__all__"

from django import forms

class BarcodeForm(forms.Form):
    barcode_image = forms.ImageField()
