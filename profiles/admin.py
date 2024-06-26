from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, UserProfile
from django.utils.html import format_html


class ProfileAdmin(UserAdmin):
    list_display       = ('email','first_name','last_name','username','last_login','date_joined','is_admin', 'is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields    = ('last_login', 'date_joined')
    ordering           = ('-date_joined',)

    # Added due to custom class
    filter_horizontal  = ()
    list_filter        = ()
    fieldsets          = ()


#___________________________________________________________  UserProfileAdmin
class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail','user', 'address','city','country')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
