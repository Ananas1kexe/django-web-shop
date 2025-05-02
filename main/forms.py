from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="", max_length=255, required=False, widget=forms.TextInput(attrs={"placeholder": "Enter book title",
            "class": "search-input"}))