"""
URL configuration for Demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from register import views as v
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
   # path("register/", v.register, name = "register" ),
    path ("change-password/",v.change_password, name= 'change_password'),
    #path('change-password/', PasswordChangeView.as_view(template_name='registration/change_password.html'),name ='change_password'),
   # path('logout/',auth_views.LogoutView.as_view(), name='logout' ),
    path('', include ('Unnapp.urls')),
    path('', include("django.contrib.auth.urls")),
    path('cart/', include('Cart.urls')),
    path('payment/', include('payment.urls')),

]    
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    #allows to upload images
   
