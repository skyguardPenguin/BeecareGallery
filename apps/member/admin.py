from django.contrib import admin
from apps.member.models import memberphoto

@admin.register(memberphoto)
class MemberphotoAdmin(admin.ModelAdmin):
    list_display = ["id"]
# Register your models here.
