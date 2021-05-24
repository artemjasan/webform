from django.contrib import admin

from .models import Form


class BaseReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False


class CustomModelAdmin(BaseReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ("name", "email", "ico")


admin.site.register(Form, CustomModelAdmin)
