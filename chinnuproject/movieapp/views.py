from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Movie
from.forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def login(request):

    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid registation")
            return redirect('login')
    return render(request,"login.html")
def register(request):

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['password1']
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save();


            return redirect('/')
        return render(request, "register.html")
def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dep =request.POST.get('dep',)
        year=request.POST.get('year',)

        movie=Movie(name=name,dep=dep,year=year)

        return redirect('/')
    return render(request,'add.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

