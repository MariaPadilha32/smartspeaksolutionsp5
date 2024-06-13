from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=300, null=False, blank=False)
    detail = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Eulogy(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    event_date = models.DateField(blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    preference_narrative = models.CharField(max_length=50, blank=False, null=False)
    relationship = models.CharField(max_length=100, blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additional_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
    relationship_audience = models.CharField(max_length=100, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
    tone_sad = models.BooleanField(default=False)
    tone_happy = models.BooleanField(default=False)
    tone_funny = models.BooleanField(default=False)
    tone_formal = models.BooleanField(default=False)
    tone_casual = models.BooleanField(default=False)
    tone_motivational = models.BooleanField(default=False)
    tone_reflective = models.BooleanField(default=False)
    tone_others = models.CharField(max_length=100, blank=True, null=True)
    user_input = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "eulogy"