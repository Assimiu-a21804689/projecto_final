from django.contrib import admin
from .models import User, Foto
from django.contrib.auth import admin as controle
# Register your models here.
admin.site.register(User, controle.UserAdmin)
admin.site.register(Foto)
