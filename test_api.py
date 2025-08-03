import requests 

url = "http://localhost:8000/predict"
data = {"text": "I still remember the look on your face,"
                "Lit through the darkness at 1:58,"
                "You told me you loved me, so why did you go away?"
                "Away"
}

try:
    response = requests.post(url, json=data)
    print("\nResposta da API:")
    print(f"Status Code: {response.status_code}")
    print(f"Sentimento: {response.json()['sentiment']}")
    print(f"Confiança: {response.json()['confidence']:.2%}")
except Exception as e:
    print(f"\nErro ao chamar a API: {e}")