from django.urls import path
from .views import analysis_list, analysis_stats, export_csv

urlpatterns = [
    path("analyses/", analysis_list),
    path("stats/", analysis_stats),
    path("export/csv/", export_csv),
]
