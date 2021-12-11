from django import forms
from . models import Holdings

class HoldingsForm(forms.ModelForm):
    class Meta:
        model = Holdings
        fields = ['title', 'holding', 'authors', 'category']
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'holding': forms.FileInput(attrs={'type': 'file'}),
            'authors': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            
        }
class SearchForm(forms.Form): # create a search form
    query = forms.CharField(max_length=250)
    class Meta:
        widgets={
            'query': forms.TextInput(attrs={'class': 'form-control'}),
            }
