from django.contrib import admin

# Register your models here.
from . models import Author,Post,Tag,Comment


class pgadmin(admin.ModelAdmin):
    list_filter=("author","tags","date",)
    list_display=("title","date","author",)
    prepopulated_fields={"slug":("title",)}
admin.site.register(Author)
admin.site.register(Post, pgadmin)
admin.site.register(Tag)
admin.site.register(Comment)
