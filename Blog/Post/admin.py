from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'imagen_portada',)
    list_per_page = 10




# Register your models here.
#admin.site.register(Post)