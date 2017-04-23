import json

from django.db import models
from django.template.defaultfilters import slugify

from transliterate import translit

# Create your models here.


class Recipe(models.Model):
    line = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date_released = models.CharField(max_length=255, blank=True)
    date_update = models.CharField(max_length=255, blank=True)
    tools = models.CharField(max_length=255, blank=True)
    serving_dish = models.CharField(max_length=255, blank=True)
    cooking_time = models.CharField(max_length=255, blank=True)

    image_filename = models.CharField(max_length=255, blank=True)
    
    ingridients_headers = models.CharField(max_length=5000, blank=True)
    ingridients = models.CharField(max_length=5000, blank=True)
    dish_output = models.CharField(max_length=5000, blank=True)

    cooking_technology = models.CharField(max_length=5000, blank=True)
    nutrition_caloricity = models.CharField(max_length=255, blank=True)
    nutrition_proteins = models.CharField(max_length=255, blank=True)
    nutrition_fats = models.CharField(max_length=255, blank=True)
    nutrition_carbohydrates = models.CharField(max_length=255, blank=True)
    decor_delivery = models.CharField(max_length=255, blank=True)

    organoleptic_stats = models.CharField(max_length=5000, blank=True)


    slug = models.SlugField(blank=True, unique=True)
    def save(self, *args, **kwargs):
        slug_translit = translit(self.title, 'ru', reversed=True)
        print(slug_translit)
        self.slug = slugify(slug_translit)
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Recipes'
        
    def __str__(self):
        return self.title


