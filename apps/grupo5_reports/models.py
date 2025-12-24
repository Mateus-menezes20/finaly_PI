from django.db import models
from apps.grupo3_images.models import UploadedImage
from apps.grupo2_auth.models import User


class MedicalReport(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="medical_reports"
    )

    image = models.ForeignKey(
        UploadedImage,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    report_json = models.JSONField()
    report_pdf = models.FileField(upload_to="reports/pdfs/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Relatório #{self.id} - {self.patient}"
