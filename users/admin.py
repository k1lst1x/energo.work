from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import UserCreationForm

User = get_user_model()


# @admin.register(User)
# class UserAdmin(UserAdmin):
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2'),
#         }),
#     )

#     add_form = UserCreationForm

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Форма для создания пользователя
    add_form = UserCreationForm

    # Поля, отображаемые в форме добавления пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )

    # Поля, отображаемые в форме редактирования пользователя
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'role')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Поля, отображаемые в списке пользователей
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')

    # Поля для поиска
    search_fields = ('username', 'email')
    ordering = ('email',)
