from django.contrib import admin
from register.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')