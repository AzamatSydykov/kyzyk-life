
from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag, Favorites
from .models import ReviewPost

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(ReviewPost)
admin.site.register(Favorites)