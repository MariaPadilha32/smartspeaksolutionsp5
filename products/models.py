from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=300, null=False, blank=False)
    detail = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name

