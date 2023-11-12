from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'friend']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    pass
