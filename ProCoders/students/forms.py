from django import forms
from django.forms import EmailField,Textarea
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import FeedBack
# ''UserCreationForm''   this class use for user creating data 
BIRTH_YEAR_CHOICES = ['1995', '1996', '1997','1998','1999','2000','2001','2002','2003','2004','2005']
User = get_user_model()
class Profile(UserCreationForm):
    
    first_name=forms.CharField(max_length=40,widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=40,widget = forms.TextInput(attrs={'class':'form-control'}))
    phone_no=forms.CharField(max_length=15,widget = forms.NumberInput(attrs={'class':'form-control'}))
    dob=forms.DateField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    location=forms.CharField(max_length=20,widget = forms.TextInput(attrs={'class':'form-control'}))
    collage_name=forms.CharField(max_length=55,widget = forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control'}))
    user_profile_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-primary'}))
    
    
    class Meta:
        model =User
        fields = ['user_profile_image','first_name','last_name', 'phone_no','dob','location','collage_name','email']


class FeedbackForm(forms.ModelForm):
    email=forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control'}))
    feedBackText=forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
     
    class Meta:
        model = FeedBack
        fields = ['email','feedBackText']
    
