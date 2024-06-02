from django.contrib import admin
from .models import FacebookToken
from .models import FacebookPage

# Register your models here.
admin.site.register(FacebookToken)

class FacebookPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_id', 'category')
admin.site.register(FacebookPage, FacebookPageAdmin)