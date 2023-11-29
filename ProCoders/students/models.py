from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.contrib.auth.models import User


class Profile(AbstractUser):
    username=None
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email=models.EmailField(unique=True)
    phone_no=models.CharField(max_length=15)
    dob=models.DateField(null=True)
    location=models.CharField(max_length=20)
    collage_name=models.CharField(max_length=55)
    user_profile_image = models.ImageField(upload_to='user_profile_images', null=False,unique=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'PNG', 'SVG', 'jfif'])])

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=UserManager()

    def __str__(self):
        return str(self.id)


BCA_CHOICES = (
    ('B1', 'B.C.A-1'),
    ('B2', 'B.C.A-2'),
    ('B2', 'B.C.A-3'),
)

MCA_CHOICES = (
    ('M1', 'M.C.A-1-SEM'),
    ('M2', 'M.C.A-2-SEM'),
    ('M3', 'M.C.A-3-SEM'),
    ('M4', 'M.C.A-4-SEM'),
)
class BcaFileUpload(models.Model):
    Bca_id=models.AutoField(primary_key=True)
    bca_file_name=models.CharField(max_length=150,null=True,blank=True)
    Hindi_write_file=models.FileField(upload_to='',null=True,blank=True)
    English_write_file=models.FileField(upload_to='',null=True,blank=True)
    category = models.CharField(choices=BCA_CHOICES , max_length=2)
    
    def __str__(self):
        return self.bca_file_name
    
    
class McaFileUpload(models.Model):
    Mca_id=models.AutoField(primary_key=True)
    Mca_file_name=models.CharField(max_length=150,null=True,blank=True)
    Hindi_write_file=models.FileField(upload_to='',null=True,blank=True)
    English_write_file=models.FileField(upload_to='',null=True,blank=True)
    category = models.CharField(choices=MCA_CHOICES, max_length=2)
    
    def __str__(self):
        return self.Mca_file_name
    
    
class FeedBack(models.Model):
    stu_email = models.EmailField()
    stu_FeedBackText = models.TextField()
    date = models.DateField(auto_now_add=True)
     
    def __str__(self):
        return self.stu_email