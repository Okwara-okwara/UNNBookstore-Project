from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DeliveryStatus
from payment.models import Order

@receiver(post_save, sender=Order)
def create_delivery_status(sender, instance, created, **kwargs):
    if created:
        DeliveryStatus.objects.create(user=instance.user, status='Pending')