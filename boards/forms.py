from django import forms
from boards.models import *
# from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget

class BoardForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Board
        # fields = '__all__'
        fields = ['name', 'description']
        # widgets = { 'description': CKEditorWidget()}
