from django import forms

class ComplaintForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First and Last'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@domain.tld'}))
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(555) 555-5555'}))
    complaint = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your Complaint here.....', 'rows': 6}))
