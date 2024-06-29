from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=300, null=False, blank=False)
    image = models.URLField(max_length=1024, null=True, blank=True)
    detail = models.TextField(null=False, blank=False)
    rule = models.TextField(null=False, blank=False)
    price = models.TextField(null=False, blank=False)

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

class Vows(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    partner_name = models.CharField(max_length=50, blank=False, null=False)
    wedding_date = models.DateField(blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    history = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
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
        db_table = "vows"


class Spouse(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    partner_name = models.CharField(max_length=50, blank=False, null=False)
    wedding_date = models.DateField(blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    history = models.TextField(blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "spouse"


class Parent(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    related = models.CharField(max_length=50, blank=False, null=False)
    relationship = models.CharField(max_length=50, blank=False, null=False)
    couple_name = models.CharField(max_length=80, blank=False, null=False)
    wedding_date = models.DateField(blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    history = models.TextField(blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "parent"


class Weddingparty(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    couple_name = models.CharField(max_length=50, blank=False, null=False)
    wedding_party = models.CharField(max_length=50, blank=False, null=False)
    wedding_date = models.DateField(blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    history = models.TextField(blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "weddingparty"


class Anniversary(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    couple_name = models.CharField(max_length=50, blank=False, null=False)
    anniversary_date = models.CharField(max_length=50, blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    history = models.TextField(blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "anniversary"


class Birthday(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    birthday_person = models.CharField(max_length=50, blank=False, null=False)
    milestone = models.CharField(max_length=50, blank=False, null=False)
    birthday = models.CharField(max_length=50, blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    history = models.TextField(blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    ages = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "birthday"

class Retirements(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    retired = models.CharField(max_length=50, blank=False, null=False)
    company_name = models.CharField(max_length=50, blank=False, null=False)
    years = models.CharField(max_length=50, blank=False, null=False)
    date = models.CharField(max_length=50, blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "retirements"


class Occasions(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    occasion = models.CharField(max_length=50, blank=False, null=False)
    date = models.CharField(max_length=50, blank=False, null=False)
    speech_length = models.CharField(max_length=50, blank=False, null=False)
    mentions = models.TextField(blank=True, null=True)
    thanks = models.TextField(blank=True, null=True)
    additonal_preferences = models.TextField(blank=True, null=True)
    dos_donts = models.TextField(blank=True, null=True)
    attendees = models.CharField(max_length=50, blank=True, null=True)
    tone_emotional = models.BooleanField(default=False)
    tone_heartfelt = models.BooleanField(default=False)
    tone_inspirational = models.BooleanField(default=False)
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
        db_table = "occasions"


