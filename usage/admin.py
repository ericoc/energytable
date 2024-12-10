from django.contrib import admin
from django.contrib.auth.admin import Group

from .models import EnergyUsage

# Set admin header and title text.
admin.site.site_header = admin.site.site_title = "Energy Usage"
admin.site.index_title = "Administration"

# Disable original admin Group model.
admin.site.unregister(Group)

# Create and register energy usage admin model.
@admin.register(EnergyUsage)
class EnergyUsageAdmin(admin.ModelAdmin):
    """Energy usage administration."""

    date_hierarchy = "hour"
    fieldsets = (
        ("Hour", {"fields": ("hour",)},),
        ("Usage", {"fields": ("kwh",)},)
    )
    list_display = readonly_fields = ("hour", "kwh",)
    model = EnergyUsage
    ordering = ("-hour",)
    show_facets = admin.ShowFacets.ALWAYS
    show_full_result_count = True
    verbose_name = verbose_name_plural = "Energy Usage"

    def has_module_permission(self, request) -> bool:
        if request.user and not request.user.is_anonymous:
            return request.user.is_superuser
        return False

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_view_permission(self, request, obj=None) -> bool:
        return self.has_module_permission(request)
