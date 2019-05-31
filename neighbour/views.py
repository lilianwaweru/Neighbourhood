from django.shortcuts import render

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
        form = EditProfile(request.POST,request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = logged_user
            edit.save()
        return redirect('welcome')

    else:

        form = EditProfile()

    return render(request,'profile.html',{'form':form})
