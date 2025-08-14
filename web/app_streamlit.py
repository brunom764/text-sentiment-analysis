import streamlit as st
import requests
from datetime import datetime

METRIC_CARD_OPEN = '<div class="metric-card">'
DIV_CLOSE = '</div>'
RESULT_CONTAINER_OPEN = '<div class="result-container">'


st.set_page_config(
    page_title="Análise de Sentimentos",
    page_icon="https://i.imgur.com/GlOVGYh.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        text-align: left;
        padding: 2rem 2.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 1.5rem;
    }
            
    .title-wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 0.3rem; 
        margin: 0;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
        margin: 0;
    }
    
    .stTextArea textarea {
        height: 120px !important;
        border-radius: 12px !important;
        border: 2px solid #e1e8ed !important;
        font-size: 16px !important;
        font-family: 'Inter', sans-serif !important;
        padding: 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none !important;
        border-radius: 8px !important;
        color: white !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.2) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background: #2563eb !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
        border: none !important;
    }
    
    .stButton > button:focus {
        background: #2563eb !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
    }
    
    .result-container {
        background: #f8fafc;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-left: 4px solid #667eea;
    }
    
    .positive { 
        color: #10b981; 
        font-weight: 600;
        font-size: 1.1rem;
    }
    .negative { 
        color: #ef4444; 
        font-weight: 600;
        font-size: 1.1rem;
    }
    .neutral { 
        color: #f59e0b; 
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border: 1px solid #f0f2f6;
    }
    
    .sidebar-content {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

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