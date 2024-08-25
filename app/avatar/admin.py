from django.contrib import admin
from .models import Avatar

# Register your models here.
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'location', 'interests_hobbies')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'age', 'gender')
        }),
        ('Demographic Information', {
            'fields': ('income_level', 'education_level', 'occupation', 'location')
        }),
        ('Psychographic Information', {
            'fields': ('interests_hobbies', 'lifestyle', 'values_beliefs', 'personality_traits', 'attitudes')
        }),
        ('Behavioral Information', {
            'fields': ('buying_behavior', 'brand_loyalty', 'shopping_preferences', 'purchase_influencers')
        }),
        ('Goals and Challenges', {
            'fields': ('primary_goals', 'challenges', 'product_help')
        }),
        ('Sources of Information', {
            'fields': ('social_media_platforms', 'favorite_websites_blogs', 'influencers_followed', 'content_types')
        }),
        ('Customer Journey', {
            'fields': ('awareness_stage', 'consideration_stage', 'decision_stage')
        }),
    )

admin.site.register(Avatar, AvatarAdmin)