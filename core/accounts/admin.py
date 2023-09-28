from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models.users import User
from accounts.models.profiles import Profile

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active")
    list_filter = ("email", "is_superuser", "is_active")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fields = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2" "is_staff",
                "is_active",
                "is_superuser",
            ),
        },
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
