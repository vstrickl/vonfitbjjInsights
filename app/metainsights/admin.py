from django.contrib import admin
from .models import FacebookToken
from .models import FacebookPage

# Register your models here.
admin.site.register(FacebookToken)

class FacebookPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_id', 'ig_user_id', 'category', 'cli_name')
admin.site.register(FacebookPage, FacebookPageAdmin)