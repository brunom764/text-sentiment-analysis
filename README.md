# 📊 Análise de Sentimentos com BERT

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.2-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red)
![Transformers](https://img.shields.io/badge/Transformers-4.34.1-yellow)

Sistema completo para classificação de sentimentos em textos, utilizando BERT fine-tuned, FastAPI e Streamlit.

<img width="1849" height="955" alt="Captura de tela de 2025-08-03 09-25-12" src="https://i.imgur.com/8flyAet.png" />

<img width="1849" height="955" alt="Captura de tela de 2025-08-03 09-26-37" src="https://i.imgur.com/uHCA4sJ.png" />

<img width="1849" height="955" alt="Captura de tela de 2025-08-03 09-26-37" src="https://i.imgur.com/ZoA8Abd.png" />

<img width="1849" height="955" alt="Captura de tela de 2025-08-03 09-26-37" src="https://i.imgur.com/g8a7Xp8.png" />

## 🚀 Funcionalidades

- Classificação em tempo real (positivo/negativo/neutro)
- Exibe confiança da predição (0-100%)
- Interface web intuitiva
- API REST para integração


## 🛠️ Tecnologias

- **Modelo**: BERT-base (Hugging Face Transformers)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Pré-processamento**: Pandas, NLTK

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/brunom764/text-sentiment-analysis.git
   cd text-sentiment-analysis
   ```

2. Faça o download do dataset em csv
   https://www.kaggle.com/datasets/kazanova/sentiment140

3. Faça o download do modelo e adicione no projeto
    https://drive.google.com/drive/folders/1ORG_kFBYfH-5JxEe-l6nF3lfC9HUgcLP?usp=drive_link
   
4. Crie o ambiente virtual
 ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows
 ```

5. Instale as dependências
 ```bash
    pip install -r requirements.txt
 ```

## 🏃 Execução

1.Inicie a API (em um terminal):

 ```bash
uvicorn main:app --reload
```

2. Inicie a interface (em outro terminal):

 ```bash
streamlit run app_streamlit.py
```

3. Acesse no navegador:

 ```bash
API: http://localhost:8000/docs

Interface: http://localhost:8501
```
 
## 📂 Estrutura do Projeto


├── web/                  # Código do frontend

│   ├── app_streamlit.py  # Interface Streamlit

├── main.py               # Endpoints e configuração

├── analise-de-sentimentos.ipynb # Jupyter notebook de treino

├── requirements.txt      # Dependências

└── README.md


## 📄 Licença
MIT License - veja LICENSE para detalhes.
