from django import forms
from .models import Profile,Business

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=[""]

 
class BusinessForm(forms.ModelForm):
    class Meta:
        model =  Business
        exclude=['user']
