from distutils.sysconfig import customize_compiler
from email.policy import default
from itertools import product
from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from django.core.signals import ready
from django.apps import apps

# Create your models here.


#if apps.ready:
  #  Cart = apps.get_model('Cart', 'Cart')




class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one field - a user can only have one profile
	date_modified = models.DateTimeField(User, auto_now=True)
	phone = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=200, blank=True)
	#address2 = models.CharField(max_length=200, blank=True)
	#city = models.CharField(max_length=200, blank=True)
	#state = models.CharField(max_length=200, blank=True)
	#zipcode = models.CharField(max_length=200, blank=True)
	#country = models.CharField(max_length=200, blank=True)
	old_cart = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)




#categories of product
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'



#customer
class Customer (models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)


    def __str__(self):
        return f'{self.first_name}{self.last_name}'


#all of our product
class Product (models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(default = 0, decimal_places = 2, max_digits = 9)
    category = models.ForeignKey(Category,on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length = 250, default = '', blank = True, null = True)
    image = models.ImageField(upload_to = 'uploads/product/')

    #add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits = 6)




    def __str__(self):
        return self.name






#Customer Order
class Order (models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product






class DeliveryStatus(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Delivered', 'Delivered')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    cart_info = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    message = models.CharField(max_length=250)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default = 0.0)

    	# Don't pluralize address
    class Meta:
        verbose_name_plural = "DeliveryStatus"

    def __str__(self):
        return f'DeliveryStatus - {str(self.id)}'

