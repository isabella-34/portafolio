import streamlit as st
from PIL import Image
import base64
import os

def get_base64(img_file):
    with open(img_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_img_tag(img_path):
    ext = os.path.splitext(img_path)[-1].replace(".", "")
    base64_img = get_base64(img_path)
    return f'<img src="data:image/{ext};base64,{base64_img}" width="110">'
    
st.set_page_config(layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

/* Centrar todo */
.block-container {
    padding-top: 2rem;
}

/* Imágenes redondas + hover */
.portfolio-item img {
    border-radius: 50%;
    transition: transform 0.3s ease;
}

.portfolio-item img:hover {
    transform: scale(1.1);
}

/* Quitar subrayado de links */
a {
    text-decoration: none;
    color: inherit;
}

/* Texto centrado */
.center {
    text-align: center;
}

/* Títulos */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.image("deco.png", width=220)

with col2:
    st.markdown("<div class='title'>PORTAFOLIO DE APPS</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Interfaces Multimodales<br>2026-1</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; max-width: 700px; margin: auto;">
        <h2>¡Bienvenidx a mi repositorio!</h2></div>
    """, unsafe_allow_html=True)

with col3:
    st.image("deco.png", width=220)


# ---------- BIENVENIDA ----------
st.markdown("""
<div style="text-align: center; max-width: 700px; margin: auto;">
    <h3>
        Aquí te presento las apps que he desarrollado en estos últimos meses 
        con herramientas de IA.
    </h3>
    <h5>
        Puedes hacer clic en cada imagen para explorar cada proyecto.
    </h5>
</div>
""", unsafe_allow_html=True)


# ---------- APPS ----------
apps = [
    {"img": "txt_to_audio2.png", "titulo": "Texto a Voz", "url": "https://imultimod.streamlit.app/"},
    {"img": "OIG8.jpg", "titulo": "Voz a Texto", "url": "https://traductorw.streamlit.app/"},
    {"img": "txt_to_audio.png", "titulo": "YOLO", "url": "https://yolov5cmc.streamlit.app/"},
    {"img": "data_analisis.png", "titulo": "Análisis de Datos", "url": "https://dataagente.streamlit.app/"},
    {"img": "Chat_pdf.png", "titulo": "RAG", "url": "https://chatpdf-cc.streamlit.app/"},
    {"img": "OIG4.jpg", "titulo": "Visión", "url": "https://vision2-gpt4o.streamlit.app/"},
    {"img": "OIG3.jpg", "titulo": "Transcriptor", "url": "https://transcript-whisper.streamlit.app/"},
    {"img": "OIG5.jpg", "titulo": "Modelos", "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"},
    {"img": "OIG6.jpg", "titulo": "Sistema Físico", "url": "https://vision2-gpt4o.streamlit.app/"}
]


# ---------- GRID ----------
import math

cols_per_row = 5
rows = math.ceil(len(apps) / cols_per_row)

for i in range(rows):
    cols = st.columns(cols_per_row)
    
    for j in range(cols_per_row):
        index = i * cols_per_row + j
        
        if index < len(apps):
            app = apps[index]
            
            with cols[j]:
                st.markdown(f"""
                <div class="portfolio-item center">
                    <a href="{app['url']}" target="_blank">
                        {get_img_tag(app['img'])}
                        <p>{app['titulo']}</p>
                    </a>
                </div>
                """, unsafe_allow_html=True)
