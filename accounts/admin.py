from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    pass
