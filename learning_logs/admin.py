from django.contrib import admin
from .models import Post,Entry


# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'date_added',)
    list_filter = ('date_added',)


@admin.register(Post)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'description',)
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('title',)}