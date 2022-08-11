from django import forms
from .models import Bookmark

class BookmarkFrom(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = [ 'title', 'url', 'memo']

