from django.shortcuts import render,redirect
from .models import Profile,Business
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,BusinessForm

# Create your views here.
def welcome(request):

    return render(request,'welcome.html')

def index(request):
    title = "Index Page"
    return render (request, 'index.html', {"title":title})


@login_required(login_url='/accounts/login/')
def profile(request):
    logged_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('welcome')

    else:

        form = ProfileForm()

    return render(request,'profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    
    try:
        prof = Profile.objects.get(user=current_user)
    except Exception as e:
        return redirect('Profile')

    return render(request,'view_profile.html',{'profile':prof})
