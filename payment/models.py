from django.db import models
from django.contrib.auth.models import User
from Unnapp.models import Product
from django.db.models.signals import post_save

#from Cart.cart import Cart





class DeliveryInfo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	Delivery_full_name = models.CharField(max_length=255)
	Delivery_email = models.CharField(max_length=255)
	Delivery_address = models.CharField(max_length=255)
	Phone_No = models.CharField(max_length=255, null=True, blank=True )
	Delivery_date = models.DateField(max_length=255, null=True, blank=True )
	Delivery_time = models.TimeField(max_length=255, null=True, blank=True )
	#shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
	#shipping_city = models.CharField(max_length=255)
	#shipping_state = models.CharField(max_length=255, null=True, blank=True)
	#shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
	#shipping_country = models.CharField(max_length=255)


	# Don't pluralize address
	class Meta:
		verbose_name_plural = "Delivery Info"

	def __str__(self):
		return f'Delivery Info - {str(self.id)}'



# Create a user delivery info by default when user signs up
def create_delivery(sender, instance, created, **kwargs):
	if created:
		user_delivery= DeliveryInfo(user=instance)
		user_delivery.save()

# Automate the profile thing
post_save.connect(create_delivery, sender=User)




# Create Order Model
class Order(models.Model):
	# Foreign Key
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	full_name = models.CharField(max_length=250)
	email = models.EmailField(max_length=250)
	delivery_info = models.TextField(max_length=15000)
	amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
	date_ordered = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return f'Order - {str(self.id)}'




#Create Order Items Model

class OrderItem(models.Model):
	# Foreign Keys
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	quantity = models.PositiveBigIntegerField(default=1)
	price = models.DecimalField(max_digits=7, decimal_places=2)


	def __str__(self):
		return f'Order Item - {str(self.id)}'




