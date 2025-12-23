import requests
import time


class MLApiClient:
    BASE_URL = "http://localhost:5000/predict"  # ajuste se necessário
    TIMEOUT = 5
    RETRIES = 3

    @classmethod
    def predict(cls, image_url):
        for attempt in range(cls.RETRIES):
            try:
                response = requests.post(
                    cls.BASE_URL,
                    json={"image_url": image_url},
                    timeout=cls.TIMEOUT
                )
                response.raise_for_status()
                return response.json()

            except requests.RequestException as e:
                if attempt == cls.RETRIES - 1:
                    raise Exception(f"Erro na API de ML: {str(e)}")
                time.sleep(1)


# 🔥 FUNÇÃO QUE O GRUPO 6 ESPERA
def analyze(image_url):
    return MLApiClient.predict(image_url)
