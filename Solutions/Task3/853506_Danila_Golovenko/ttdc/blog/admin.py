from django.contrib import admin
from .models import Post, Comment, Fact


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug',  'published_date')
    list_filter = ('author', 'published_date', 'created_date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['published_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

class FactAdmin(admin.ModelAdmin):
    list_display = ('text','use')
    list_filter = ('use',)
    search_fields = ('text',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Fact, FactAdmin)
