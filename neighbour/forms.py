from django import forms
from .models import Profile,Business,Post,Neighbourhood

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_prof']


class BusinessForm(forms.ModelForm):
    class Meta:
        model =  Business
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['post_user']

class NeighbourForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['neighbour_user']        
