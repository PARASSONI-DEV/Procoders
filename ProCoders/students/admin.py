from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    location=models.CharField(max_length=20)
    list_display =['email','phone_no','dob','collage_name']

@admin.register(BcaFileUpload)
class BcaFileupload(admin.ModelAdmin):
    list_display=['Bca_id','bca_file_name','Hindi_write_file','English_write_file']
    
    
@admin.register(McaFileUpload)
class McaFileupload(admin.ModelAdmin):
    list_display=['Mca_id','Mca_file_name','Hindi_write_file','English_write_file']
    

@admin.register(FeedBack)
class feedback(admin.ModelAdmin):
    list_display=['stu_email','stu_FeedBackText','date']