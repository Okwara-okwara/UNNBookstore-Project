from django.contrib import admin
from .models import DeliveryInfo, Order, OrderItem



#Register the model on the admin section
admin.site.register(DeliveryInfo)
admin.site.register(Order)
admin.site.register(OrderItem)
