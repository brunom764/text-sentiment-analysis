import streamlit as st
import requests
from datetime import datetime
import os

# Constantes para evitar duplicação de strings
METRIC_CARD_OPEN = '<div class="metric-card">'
DIV_CLOSE = '</div>'
RESULT_CONTAINER_OPEN = '<div class="result-container">'

def load_css(file_name):
    """Carrega arquivo CSS externo"""
    css_path = os.path.join(os.path.dirname(__file__), file_name)
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Arquivo CSS não encontrado: {file_name}")
    except Exception as e:
        st.error(f"Erro ao carregar CSS: {str(e)}")

st.set_page_config(
    page_title="Análise de Sentimentos",
    page_icon="https://i.imgur.com/GlOVGYh.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Carrega o CSS externo
load_css('styles.css')

st.markdown("""
<div class="main-header">
    <img src="https://i.imgur.com/XRbAYRH.png" alt="Brain Icon"
         style="width: 120px; height: 120px;">
    <div class="title-wrapper">
        <h1 class="main-title">Análise de Sentimentos</h1>
        <p class="main-subtitle">Inteligência artificial para compreender emoções em textos</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📝 Digite seu texto para análise")
st.markdown("Nosso modelo de IA analisará o sentimento e fornecerá uma classificação detalhada.")

user_input = st.text_area(
    "",
    placeholder="Ex: Adorei o produto! A entrega foi rápida e o atendimento foi excelente. Recomendo para todos!",
    key="text_input",
    label_visibility="collapsed"
)

if st.button("🔍 Analisar Sentimento", type="primary", use_container_width=True, key="analyze_btn"):
    if user_input.strip():
        with st.spinner("🤖 Processando com IA..."):
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
                    
                    st.markdown(RESULT_CONTAINER_OPEN, unsafe_allow_html=True)
                    st.markdown("### 📊 Resultado da Análise")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown(METRIC_CARD_OPEN, unsafe_allow_html=True)
                        st.metric("🎯 Sentimento", sentiment.upper())
                        st.markdown(DIV_CLOSE, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(METRIC_CARD_OPEN, unsafe_allow_html=True)
                        st.metric("📈 Confiança", f"{confidence:.1f}%")
                        st.markdown(DIV_CLOSE, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(METRIC_CARD_OPEN, unsafe_allow_html=True)
                        timestamp = datetime.now().strftime("%H:%M")
                        st.metric("⏰ Processado", timestamp)
                        st.markdown(DIV_CLOSE, unsafe_allow_html=True)
                    
                    st.markdown("#### Nível de Confiança")
                    progress_bar = st.progress(0)
                    progress_bar.progress(confidence / 100)
                    
                    if sentiment == "positivo":
                        st.markdown('<p class="positive">✨ Sentimento positivo detectado! O texto expressa emoções favoráveis.</p>', unsafe_allow_html=True)
                    elif sentiment == "negativo":
                        st.markdown('<p class="negative">⚠️ Sentimento negativo detectado. O texto contém emoções desfavoráveis.</p>', unsafe_allow_html=True)
                    else:
                        st.markdown('<p class="neutral">🤔 Sentimento neutro. O texto não expressa emoções claramente definidas.</p>', unsafe_allow_html=True)
                    
                    with st.expander("🔧 Detalhes Técnicos"):
                        st.json(response.json())
                    
                    st.markdown(DIV_CLOSE, unsafe_allow_html=True)
                
                else:
                    st.error(f"❌ Erro na API: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Falha ao conectar com a API: {str(e)}")
    else:
        st.warning("⚠️ Por favor, insira algum texto para análise.")

st.markdown(DIV_CLOSE, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Sobre o Sistema")
    st.markdown("""
    **Tecnologias utilizadas:**
    - 🤖 Modelo BERT fine-tuned
    - ⚡ API FastAPI para inferência
    - 🎨 Interface Streamlit moderna
    - 🔍 Análise em tempo real
    """)
    
    st.markdown("### 📈 Como funciona")
    st.markdown("""
    1. **Digite** seu texto na área principal
    2. **Clique** em analisar para processar
    3. **Visualize** o resultado com confiança
    4. **Explore** os detalhes técnicos
    """)
    
    st.markdown("### 💡 Dicas")
    st.markdown("""
    - Textos mais longos geram análises mais precisas
    - O modelo foi treinado em português
    - Confiança acima de 80% indica alta precisão
    """)

st.markdown(DIV_CLOSE, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <p>🚀 <strong>Análise de Sentimentos com IA</strong></p>
    <p>Desenvolvido com ❤️ para compreender emoções em textos</p>
    <p><small>© 2025 - {ajof-bmma-gaac-glrm}@cin.ufpe.br</small></p>
</div>
""", unsafe_allow_html=True)