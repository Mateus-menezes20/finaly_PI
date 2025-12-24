from apps.grupo4_ai.models import AnalysisHistory
from django.db.models import Count


class ReportService:

    @staticmethod
    def analysis_stats():
        total = AnalysisHistory.objects.count()

        por_risco = (
            AnalysisHistory.objects
            .values("result__nivel_de_risco")
            .annotate(qtd=Count("id"))
        )

        return {
            "total_analises": total,
            "por_nivel_de_risco": list(por_risco)
        }
