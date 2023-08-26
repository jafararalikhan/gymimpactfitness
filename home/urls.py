from django.urls import path
from home import views

urlpatterns = [
    path('',views.home, name="home"),
    path('signup',views.signup, name="signup"),
    path('login',views.handlelogin, name="handlelogin"),
    path('logout',views.handleLogout, name="handleLogout"),
    path('contact',views.contact, name="contact"),
    path('join',views.enroll, name="join"),
    path('profile',views.profile, name="profile"),
    path('gallery',views.gallery, name="gallery"),
    path('gallery',views.gallery, name="gallery"),
    path('attendance',views.attendance, name='attendance')
]