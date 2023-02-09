from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import RegisterForm,LoginForm,ChangePasswordForm,UpdateForm,ImageForm
from django.contrib import messages
from django.contrib.auth import logout as logouts
from.models import Register,Image
# Create your views here.
def hello(request):
   return HttpResponse("welcome to django")
def index(request):
    name='amal'
    return render(request, 'index.html',{'data':name}) #context

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST) 
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'user already exists')
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,'passwordmissmatch')
                return redirect('/register')
            else:
                tab=Register(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"data saved")
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request, 'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST) 
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            try:
                user=Register.objects.get(Email=email)
                if not user:
                    messages.warning(request,'email or password')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'password incorrect')
                    return redirect('/login')
                else:
                    messages.success(request,"login success")
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'email or password')
                return redirect('/login')

    else:
        form=LoginForm()
    return render(request, 'login.html',{'form':form})

def home(request,id):
    user=Register.objects.get(id=id)
    return render(request, 'home.html',{'user':user})

def changepassword(request,id):
    data=Register.objects.get(id=id)
    if request.method=='POST':
     form=ChangePasswordForm(request.POST)
     if form.is_valid():
        oldpassword=form.cleaned_data['OldPassword']
        newpassword=form.cleaned_data['NewPassword']
        confirmpassword=form.cleaned_data['ConfirmPassword']

        if oldpassword!=data.Password:
            messages.warning(request,"incorrect")
            return redirect('/changepassword/%s' % data.id)
        elif oldpassword==newpassword:
            messages.warning(request,"similar")
            return redirect('/changepassword/%s' % data.id)
        elif newpassword!=confirmpassword:
            messages.warning(request,"missmatch")
            return redirect('/changepassword/%s' % data.id)
        else:
            data.Password=newpassword
            data.save()
            messages.success(request,"success")
            return redirect('/home/%s' % data.id)
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form})

def showusers(request):
    users=Register.objects.all()
    return render(request,'showusers.html',{'users':users})

def showimages(request):
    images=Image.objects.all()
    return render(request,'showimages.html',{'images':images})


def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user) 
        if form.is_valid():
            form.save()
            messages.success(request,"data saved")
            return redirect('/showusers')
    else:
        form=UpdateForm(instance=user)
    return render(request, 'update.html',{'form':form})

def delete(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    messages.success(request,"data deleted ")
    return redirect('/showusers')

def logout(request):
    logouts(request)
    messages.success(request,"success logout ")
    return redirect('/')

def image(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Image.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,'user already exists')
                return redirect('/image')
            elif password!=confirmpassword:
                messages.warning(request,'passwordmissmatch')
                return redirect('/image')
            else:
                tab=Image(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"data saved")
                return redirect('/')
    else:
        form=ImageForm()
    return render(request, 'image.html',{'form':form})