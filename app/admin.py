from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib import admin
import datetime
from .models import Account
# Register your models here.
class Filter (admin.ModelAdmin) :
    list_display = ("name","phonenumber","box","month","year","paid","active")
    list_filter = ("box","month","year","paid","active")
    search_fields=('name',"phonenumber")
    actions = ['update',]

    @admin.action(description='Mark selected accounts as updated')
    
    def update(self, request, queryset):
        #def get_paid(self):
         #   if (int(queryset.month)) == int(datetime.datetime.now().month):
          #      return True
           # else:
            #    return False
        for item in queryset:
            item.save()
       # updated = queryset.update(year=2022)
        #self.message_user(request, ngettext(
         #   '%d story was successfully marked as published.',
          #  '%d stories were successfully marked as published.',
           # updated,
       # ) % updated, messages.SUCCESS)
admin. site. register(Account, Filter)  