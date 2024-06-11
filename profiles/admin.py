from django.contrib import admin
from .models import UserProfile, UserAddress, FeedbackForm


class UserAddressAdminInline(admin.TabularInline):
    model = UserAddress
    
    fields = ('street_address1',
              'street_address2', 'town_or_city', 'county', 'postcode', 'country', 'is_primary',)


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (UserAddressAdminInline,)

    readonly_fields = ('user', 'created_on', 
    'updated_on',)

admin.site.register(UserProfile, UserProfileAdmin,)
admin.site.register(UserAddress)
admin.site.register(FeedbackForm)

