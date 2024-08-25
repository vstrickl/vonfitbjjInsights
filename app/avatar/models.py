from django.db import models

# Create your models here.
class Avatar(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    # Demographic Information
    age = models.CharField(max_length=50, blank=True, null=True)
    gender = models.TextField(choices=[('female', 'Female'), ('male', 'Male')], blank=True, null=True)
    income_level = models.CharField(max_length=50, blank=True, null=True)
    education_level = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    # Psychographic Information
    interests_hobbies = models.TextField(blank=True, null=True)
    lifestyle = models.TextField(blank=True, null=True)
    values_beliefs = models.TextField(blank=True, null=True)
    personality_traits = models.TextField(blank=True, null=True)
    attitudes = models.TextField(blank=True, null=True)
    
    # Behavioral Information
    buying_behavior = models.TextField(blank=True, null=True)
    brand_loyalty = models.TextField(blank=True, null=True)
    shopping_preferences = models.TextField(choices=[('online', 'Online'), ('offline', 'Offline')], blank=True, null=True)
    purchase_influencers = models.TextField(blank=True, null=True)
    
    # Goals and Challenges
    primary_goals = models.TextField(blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    product_help = models.TextField(blank=True, null=True)
    
    # Sources of Information
    social_media_platforms = models.TextField(blank=True, null=True)
    favorite_websites_blogs = models.TextField(blank=True, null=True)
    influencers_followed = models.TextField(blank=True, null=True)
    content_types = models.TextField(blank=True, null=True)
    
    # Customer Journey
    awareness_stage = models.TextField(blank=True, null=True)
    consideration_stage = models.TextField(blank=True, null=True)
    decision_stage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name