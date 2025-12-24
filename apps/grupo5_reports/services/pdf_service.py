from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
import os


def generate_pdf_report(history):
    """
    Gera um PDF médico a partir do histórico de análise
    e retorna o caminho do arquivo.
    """

    output_dir = os.path.join(settings.MEDIA_ROOT, "reports")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(
        output_dir, f"relatorio_{history.id}.pdf"
    )

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    result = history.result or {}

    story.append(Paragraph("<b>RELATÓRIO MÉDICO GERADO POR IA</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Resumo:</b>", styles["Heading2"]))
    story.append(Paragraph(result.get("resumo", "Não informado"), styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Nível de risco:</b>", styles["Heading2"]))
    story.append(Paragraph(result.get("nivel_de_risco", "Não informado"), styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Recomendações:</b>", styles["Heading2"]))
    for rec in result.get("recomendacoes", []):
        story.append(Paragraph(f"- {rec}", styles["Normal"]))

    story.append(Spacer(1, 12))
    story.append(Paragraph(result.get("aviso_legal", ""), styles["Italic"]))

    doc.build(story)

    return file_path
