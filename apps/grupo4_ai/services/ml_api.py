import json
import re
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")


class MLApiClient:

    @staticmethod
    def _extract_json(text: str) -> dict:
        match = re.search(r"\{[\s\S]*\}", text)
        if not match:
            return {
                "resumo": "Relatório indisponível.",
                "achados_visuais": {},
                "nivel_de_risco": "indefinido",
                "recomendacoes": ["Reenvie a imagem para nova análise."],
                "aviso_legal": "Este relatório não substitui avaliação médica profissional."
            }

        try:
            return json.loads(match.group())
        except Exception:
            return {
                "resumo": "Erro ao interpretar o relatório.",
                "achados_visuais": {},
                "nivel_de_risco": "indefinido",
                "recomendacoes": ["Erro interno na análise automática."],
                "aviso_legal": "Este relatório não substitui avaliação médica profissional."
            }

    @staticmethod
    def predict(image_url: str) -> dict:
        prompt = """
Você é uma inteligência artificial de apoio à área médica.

Analise a imagem fornecida e gere um RELATÓRIO EM JSON com a seguinte estrutura:

{
  "resumo": "...",
  "achados_visuais": {...},
  "nivel_de_risco": "baixo | medio | alto",
  "recomendacoes": [...],
  "aviso_legal": "..."
}

Regras:
- NÃO faça diagnóstico definitivo
- NÃO cite doenças específicas
- Linguagem técnica, ética e objetiva
"""

        response = model.generate_content([prompt, image_url])
        return MLApiClient._extract_json(response.text)


def analyze(image_url):
    return MLApiClient.predict(image_url)
