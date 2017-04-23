from django.contrib import admin

from .models import Recipe




# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    
admin.site.register(Recipe, RecipeAdmin)
