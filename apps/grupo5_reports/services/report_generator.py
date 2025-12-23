from apps.grupo4_ai.models import AnalysisHistory
from django.db.models import Avg, Count

class ReportService:

    @staticmethod
    def analysis_stats():
        total = AnalysisHistory.objects.count()

        by_class = (
            AnalysisHistory.objects
            .values("classification")
            .annotate(count=Count("id"))
        )

        avg_confidence = (
            AnalysisHistory.objects.aggregate(
                avg=Avg("confidence")
            )["avg"]
        )

        last_analysis = (
            AnalysisHistory.objects
            .order_by("-created_at")
            .first()
        )

        return {
            "total": total,
            "by_classification": list(by_class),
            "average_confidence": avg_confidence,
            "last_analysis": last_analysis.id if last_analysis else None
        }
