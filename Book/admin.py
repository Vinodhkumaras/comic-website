from django.contrib import admin
from .models import Comic, Author
# from .models import Comic,ComicPage

# Register your models here.

admin.site.register(Comic)

admin.site.register(Author)

# class ComicPageInline(admin.TabularInline):
#     model = ComicPage
#     extra = 1

# class ComicAdmin(admin.ModelAdmin):
#     inlines = [ComicPageInline]
#     list_display = ['title', 'created_at']



