from django.contrib import admin
from .models import Category, Extension, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'version', 'download_count', 'rating']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['extension', 'user', 'rating', 'created_at']