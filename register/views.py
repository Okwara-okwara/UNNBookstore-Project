from urllib import response, request
from django.shortcuts import render, redirect
#from .forms import RegistrationForm
#from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views

from django.urls import path, reverse_lazy



# Create your views here.


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save
            #update the session to keep the user logged in
            update_session_auth_hash(request, user)
            return redirect('/login')

    else:
        form = PasswordChangeForm(request.user)
    
    return render (request, 'registration/change_password.html', {'form': form})

#password_change_view = PasswordChangeView.as_view(
 #   template_name = 'registration/change_password.html',
  #  success_url = reverse_lazy('password_change_done')
#)



# Create your views here.
#urlpatterns = [
 #   path('login/',LoginView.as_view(),name='login'),
  #  path('logout/',LogoutView.as_view(), name = 'logout')
#]

