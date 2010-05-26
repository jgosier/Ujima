from django import forms
class SearchForm(forms.Form):
    q=forms.CharField(widget=forms.TextInput(attrs={'size':'30'}),label='search')
    