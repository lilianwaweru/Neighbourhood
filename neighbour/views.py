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
    print(logged_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user_prof = logged_user
            edit.save()
        return redirect('view_profile')

    else:

        form = ProfileForm()

    return render(request,'profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    print(current_user)
    business = Business.objects.filter(user=current_user)
    prof = Profile.objects.filter(user_prof=current_user)
    print(prof[0])

    # try:
    #      prof = Profile.objects.filter(user_prof=current_user)
    # except Exception as e:
    #     pass
    

    return render(request,'view_profile.html',{'profiles':  prof,'bizna':business})


@login_required(login_url='/accounts/login/')
def view_business(request):
    businesses = Business.objects.all()

    return render(request,'view_business.html',{"businesses":businesses})


@login_required(login_url='/accounts/login/')
def business(request):
    logged_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('view_business')

    else:

        form = BusinessForm()

    return render(request,'business.html',{'form':form})


@login_required(login_url='/accounts/login/')
def create_post(request):
    logged_user = request.user
    print(logged_user.id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('welcome')

    else:

        form = PostForm()

    return render(request,'post.html',{'form':form})
