from django.contrib import admin
from .models import Category, Post, Tag, SinglePage
from django.contrib.auth.models import User
# Register your models here.

class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'created_time',)
	search_fields = ['title', 'body']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(SinglePage)
