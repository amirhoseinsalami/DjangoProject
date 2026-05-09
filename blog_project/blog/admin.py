from django.contrib import admin

from .models import Post, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'author','list_categories', 'published_at')
    fields = ('title', 'body', 'author', 'categories', 'published_at')
    ordering = ['-published_at']
    search_fields = ('title', 'author__username')
    list_filter = ('published_at', 'categories')


    def list_categories(self , obj):
        categories = obj.categories.all()[:4]
        return ", ".join(category.name for category in categories)
    
    list_categories.short_description = 'categories'


