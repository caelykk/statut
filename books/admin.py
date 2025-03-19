from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'price', 'stock', 'available', 'publication_date', 'created_at')
	search_fields = ('title', 'slug')
	list_filter = ('available', 'publication_date',)
	prepopulated_fields = {"slug": ("title",)}