from django import forms
from boards.models import *
from tinymce.widgets import TinyMCE

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = '__all__'
        fields = ['name', 'description']
        widgets = { 'description': TinyMCE(attrs={'cols': 80, 'rows': 30}) }

