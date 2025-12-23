# apps/grupo6_api/services/orchestrator.py

from apps.grupo3_images.models import UploadedImage as Image
from apps.grupo4_ai.services.ml_api import analyze
from apps.grupo4_ai.models import AnalysisHistory


class AnalysisOrchestrator:
    """
    Classe responsável por orquestrar o processo de análise de imagens:
    1. Salva a imagem no banco (Grupo 3)
    2. Envia para análise via API de ML (Grupo 4)
    3. Salva o histórico da análise
    """

    @staticmethod
    def process(patient, image_file):
        """
        Processa a imagem de um paciente e registra o histórico.

        :param patient: instância do paciente
        :param image_file: arquivo de imagem enviado
        :return: instância de AnalysisHistory
        """

        # 1. Salva a imagem no banco
        image = Image.objects.create(image=image_file)

        # 2. Envia a imagem para a API de ML
        result = analyze(image.image.url)

        # 3. Salva o histórico da análise
        history = AnalysisHistory.objects.create(
            patient=patient,
            image=image,
            result=result
        )

        return history
