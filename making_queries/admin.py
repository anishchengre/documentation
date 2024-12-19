from django.contrib import admin
from .models import Blog, Author, Dog, Entry


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    search_fields = ('name', 'tagline')
    ordering = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 20


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'blog', 'pub_date', 'mod_date', 'number_of_comments',  'number_of_pingbacks', 'rating')
    list_filter = ('pub_date', 'mod_date', 'blog', 'rating')
    search_fields = ('headline', 'body_text', 'authors__name', 'blog__name')
    date_hierarchy = 'pub_date'
    filter_horizontal = ('authors',)
    # readonly_fields = ('mod_date',)
    list_editable = ('number_of_comments', 'rating')
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('blog', 'headline', 'body_text', 'pub_date', 'mod_date', 'rating')
        }),
        ('Additional Info', {
            'fields': ('number_of_comments', 'number_of_pingbacks', 'authors'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'data')
    search_fields = ('name',)
    list_per_page = 20
    
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Additional Info', {
            'fields': ('data',),
            'classes': ('collapse',),
        }),
    )







