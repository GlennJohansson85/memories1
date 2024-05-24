from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'user')  # Customize the columns displayed in the admin list view
    list_filter = ('created_on', 'user')  # Add filters to the admin list view


admin.site.register(Post, PostAdmin)
