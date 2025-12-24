from django.db import models
from apps.grupo3_images.models import UploadedImage


class AnalysisHistory(models.Model):
    patient = models.CharField(max_length=255)
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Análise - {self.patient} - {self.created_at}"
