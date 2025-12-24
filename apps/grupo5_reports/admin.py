from django.contrib import admin
from .models import MedicalReport


@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "created_at")
    list_filter = ("created_at",)
    search_fields = ("patient__username",)
