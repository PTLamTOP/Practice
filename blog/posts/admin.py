from django.contrib import admin
from .models import Post, Author, Editor

admin.site.register(Post)
admin.site.register(Editor)
admin.site.register(Author)