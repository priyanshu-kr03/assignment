from django.contrib import admin
from .models import Group, Member
# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Member)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('user', )