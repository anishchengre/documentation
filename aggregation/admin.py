from django.contrib import admin
from .models import AggergationAuthor, Publisher, Book, Store


@admin.register(AggergationAuthor)
class AggergationAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'publisher', 'pubdate')
    list_filter = ('pubdate', 'rating', 'publisher')
    search_fields = ('name', 'authors__name', 'publisher__name')
    date_hierarchy = 'pubdate'
    filter_horizontal = ('authors',)
    list_editable = ('price', 'rating')
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name', 'pages', 'price', 'rating', 'publisher', 'pubdate')
        }),
        ('Authors', {
            'fields': ('authors',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'books__name')
    filter_horizontal = ('books',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Books', {
            'fields': ('books',),
            'classes': ('collapse',),
        }),
    )
