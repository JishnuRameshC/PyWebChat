from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup_page,name="signup"),
    path('home/',views.home, name='home'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.LogoutPage,name='logout'), 
]