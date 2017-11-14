from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Curso

class AlunoAdmin(UserAdmin):
    list_display = ('email', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('email', 'nome', 'curso')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'email', 'nome', 'curso')} ),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Register your models here.
admin.site.register(Curso)