from django.contrib import admin

from .models import Category, Task
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'list_categories', 'due_date', 'priority', 'status')
    fields = ('title', 'description', 'user', 'priority', 'due_date', 'status')
    ordering = ['-due_date']
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority', 'categories')

    def list_categories(self , obj):
        categories = obj.categories.all()[:4]
        return ", ".join(category.name for category in categories)
    
    list_categories.short_description = 'categories'