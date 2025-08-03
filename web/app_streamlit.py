import streamlit as st
import requests
from datetime import datetime


st.set_page_config(
    page_title="Análise de Sentimentos",
    page_icon="😊",
    layout="centered"
)


st.markdown("""
<style>
    .positive { color: #2ecc71; font-weight: bold; }
    .negative { color: #e74c3c; font-weight: bold; }
    .neutral { color: #f39c12; font-weight: bold; }
    .stTextArea textarea { height: 150px; }
</style>
""", unsafe_allow_html=True)


st.title("📊 Analisador de Sentimentos")
st.markdown("Insira um texto para classificar seu sentimento como **positivo**, **negativo** ou **neutro**.")


user_input = st.text_area(
    "Digite seu texto aqui:",
    placeholder="Ex: Adorei o produto! A entrega foi rápida e o atendimento excelente...",
    key="text_input"
)

if st.button("🔍 Analisar Sentimento", type="primary", use_container_width=True):
    if user_input.strip():
        with st.spinner("Processando..."):
            try:
                response = requests.post(
                    "http://localhost:8000/predict",
                    json={"text": user_input},
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    confidence = result['confidence'] * 100
                    sentiment = result['sentiment']
                    
                    st.markdown("---")
                    st.subheader("Resultado:")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Sentimento", sentiment.upper())
                    with col2:
                        st.metric("Confiança", f"{confidence:.2f}%")
                    
                    progress_bar = st.progress(0)
                    for percent_complete in range(int(confidence)):
                        progress_bar.progress(percent_complete + 1)
                    
                    if sentiment == "positivo":
                        st.markdown('<p class="positive">✅ Sentimento positivo detectado!</p>', unsafe_allow_html=True)
                    elif sentiment == "negativo":
                        st.markdown('<p class="negative">⚠️ Sentimento negativo detectado</p>', unsafe_allow_html=True)
                    else:
                        st.markdown('<p class="neutral">🤔 Sentimento neutro</p>', unsafe_allow_html=True)
                    
                    with st.expander("Detalhes técnicos"):
                        st.json(response.json())
                
                else:
                    st.error(f"Erro na API: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Falha ao conectar com a API: {str(e)}")
    else:
        st.warning("Por favor, insira algum texto para análise.")

with st.sidebar:
    st.header("ℹ️ Sobre")
    st.markdown("""
    Esta aplicação utiliza:
    - Modelo BERT fine-tuned
    - API FastAPI para inferência
    - Streamlit para interface
    """)
    st.markdown("---")



st.markdown("---")
st.caption("© 2025 Análise de Sentimentos - {ajof-bmma-gaac-glrm}@cin.ufpe.br")