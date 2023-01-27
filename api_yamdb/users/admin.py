from django.contrib import admin

from .models import User


class CustomUserAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'username',
        'bio',
        'role',
    )
    search_fields = ('username', 'role')
    list_filter = ('username',)
    empty_value_display = '-пусто-'

    def get_model_perms(self, request):
        return {
            'add': self.has_add_permission(request),
            'delete': self.has_delete_permission(request),
            'view': self.has_view_permission(request),
        }


admin.site.register(User, CustomUserAdmin)
