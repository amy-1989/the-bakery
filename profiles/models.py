from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    #Existing users: just save the profile
    instance.userprofile.save()


class UserAddress(models.Model):
    """
    A model for maintaining user
    delivery addresses
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    profile = models.ForeignKey(UserProfile, default='', on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='address')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    is_primary = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return f'Address for user profile {self.profile}'


class FeedbackForm(models.Model):
    order_number = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback for order number {self.order_number} from {self.customer_name}"




   

