from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('index/',views.index,name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('All_notes_detail/', views.Bca_Notes_Pdf.as_view(),
         name="BCA"),
    path('All_notes_details/', views.Mca_Notes_pdf.as_view(),
         name="MCA"),
    path('feed_back_form/',views.feed_back_form,name="feed_back_form"),
    path('alreadyfeedback/',views.alreadyfeedback,name='alreadyfeedback')
    
]
