from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_date',
                    'lost_or_found')

admin.site.register(Post, PostAdmin)
