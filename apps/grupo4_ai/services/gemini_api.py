import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.AIzaSyAR7aCT4i_9DbO7WVixatWc_9URNIV7DZE)

model = genai.GenerativeModel("gemini-1.5-pro-vision")

def analyze_medical_image(image_url):
    prompt = """
    Você é uma IA de apoio à área médica.
    Analise a imagem e gere um relatório estruturado em JSON contendo:
    - resumo
    - achados_visuais
    - nivel_de_risco (baixo, medio, alto)
    - recomendacoes
    - aviso_legal
    NÃO faça diagnóstico definitivo.
    """

    response = model.generate_content([
        prompt,
        image_url
    ])

    return response.text
