from django.shortcuts  import render,HttpResponseRedirect,redirect,HttpResponse
from .forms import Profile
from .models import BcaFileUpload,McaFileUpload
from django.contrib import messages
from django.views import View
from unicodedata import category, name
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as login_pro,logout
from .forms import FeedbackForm
from .models import FeedBack
def signup(request):
    if request.method=='POST':
        form=Profile(request.POST,request.FILES)
        if form.is_valid():
            Profile(request.FILES['user_profile_image'])
            form.save()
            messages.success(request, 'Congratulation!! Updated successfully')
            # return render(request,'visits/login.html',{'form':form}) 
            return redirect('/')
    else:
        form =Profile()
    return render(request,'visits/Register.html',{'form':form})   


def login(request):
    if not request.user.is_authenticated:
      if request.method=="POST":
          form=AuthenticationForm(request=request,data=request.POST)
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']
              usr=authenticate(username=username,password=password)
              if usr is not None:
                  login_pro(request,usr)
                  messages.success(request,'You are successfully loggedin !!')
                  return render(request,'visits/index.html')
      else:        
       form=AuthenticationForm()
      return render(request,'visits/login.html',{'form':form})
    else:
        return HttpResponseRedirect('index/')
  

class Bca_Notes_Pdf(View):
    def get(self, request):
    #   if request.user.is_authenticated:  
         BCA1=BcaFileUpload.objects.filter(category='B1')
         BCA2=BcaFileUpload.objects.filter(category='B2')
         BCA3=BcaFileUpload.objects.filter(category='B3')
         
         Bcayears={
            'BCA1':'B.C.A First Year',
            'BCA2':'B.C.A Second Year',  
            'BCA3':'B.C.A Third Year',
         }
         return render(request,'visits/BCA.html',{'BCA1':BCA1,'BCA2':BCA2,'BCA3':BCA3,'Bcayears':Bcayears})
    #   else:
    #       return HttpResponseRedirect('/login/')
     
class Mca_Notes_pdf(View):
    def get(self,request):
        # if request.user.is_authenticated: 
            MCA1=McaFileUpload.objects.filter(category='M1')
            MCA2=McaFileUpload.objects.filter(category='M2')
            MCA3=McaFileUpload.objects.filter(category='M3')   
            MCA4=McaFileUpload.objects.filter(category='M4')
            Mcayears={
            'MCA1':'M.C.A-Fisrt-Semester',
            'MCA2':'M.C.A-Second-Semester',  
            'MCA3':'M.C.A-Third-Semester',
            'MCA4':'M.C.A-Fourth-Semester',
            } 
            return render(request,'visits/MCA.html',{'MCA1':MCA1,'MCA2':MCA2,'MCA3':MCA3,'MCA4':MCA4,'Mcayears':Mcayears})
        # else:
        #     return HttpResponseRedirect('/login/')  



def feed_back_form(request):
  if not request.user.is_authenticated:  
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
        #  form = FeedbackForm(request.POST)
         Email=form.cleaned_data['email']
         FeedBackText=form.cleaned_data['feedBackText']
         form=FeedBack(stu_email=Email,stu_FeedBackText=FeedBackText)
         form.save()
        
         return render(request, 'visits/feedback.html',{'form':form,'active':'btn-primary'})
            # return HttpResponse("successfully!")
        else:     
          return HttpResponse("error!")
    else: 
         #  return HttpResponse("error!")
         form = FeedbackForm()
         return render(request, 'visits/feedback.html',{'form':form,'active':'btn-primary'})
  else: 
    return HttpResponseRedirect('/feed_back_form/')
     
            

def alreadyfeedback(request):
    add = FeedBack.objects.filter()
    return render(request,'visits/feedback.html',{'add':add,'active':'btn-primary'})


def index(request):
    return render(request,'visits/index.html')


# def feed_back(request):
#     if request.method == 'POST':
#         form = FeedbackForm()
#         if form.is_valid():
#             form = FeedbackForm(request.POST)
            
#             email=request.cleaned_data['email']
#             text=request.cleaned_data['FeedBackText']
#             form=FeedBack(email=email,FeedBackText=text)
#             form.save()
#             add=FeedBack.objects.filter()
#             print(add)
#             return render(request, 'visits/index.html',{'form':form,'add':add})
#     else:
#      form = FeedbackForm()
#     return render(request, 'visits/index.html',{'form':form})
        