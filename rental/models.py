from django.db import models
from multiselectfield import MultiSelectField
from django.utils.text import slugify

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    detailed_location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    gmail = models.EmailField()
    phone = models.CharField(max_length=20)
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    negotiable = models.BooleanField(default=False)
    advance_deposit = models.DecimalField(max_digits=8, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    description = models.TextField()
    kitchen = models.BooleanField(default=False)
    floor_number = models.PositiveIntegerField()
    CONDITION_CHOICES = [
        ('brand_new', 'Brand New'),
        ('furnished', 'Furnished'),
        ('old', 'Old'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    bachelor_allowed = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    security_guard = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    images = models.ImageField(upload_to='property_images', blank=True)
    title_slug = models.SlugField(max_length=255, unique=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images')

    def __str__(self):
        return self.property.title + " Image"
