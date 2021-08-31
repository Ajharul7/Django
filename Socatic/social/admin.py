from django.contrib import admin
from .models import Post, Comment, UserProfile, Post1, Comment1

admin.site.register(Post)
admin.site.register(Post1)
admin.site.register(Comment)
admin.site.register(Comment1)
admin.site.register(UserProfile)
