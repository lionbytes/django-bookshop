from django.contrib import admin
from .models import Book, BookNumber, Character, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	# fields = ['title', 'description', 'price', 'published', 'is_published', 'cover']
	list_display = ['title', 'description', 'price']
	list_filter = ['published']
	search_fields = ['title', 'description']

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
