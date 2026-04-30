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
    
st.set_page_config(layout="wide")
st.markdown("""
<style>
.block-container {
    max-width: 1230px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

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
        Puedes hacer clic en las imágenes para explorar cada proyecto.
    </h5>
    
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("espacio.png", use_container_width=True)

# ---------- APPS ----------
apps = [
    {"img": "col1.jpg", "titulo": "Mi primera app", "url": "https://multimodal1-app1.streamlit.app/"},
    {"img": "obj2.jpg", "titulo": "Análisis de PDF", "url": "https://chat-pdff.streamlit.app/"},
    {"img": "obj3.jpg", "titulo": "Control por voz", "url": "https://voice---control.streamlit.app/"},
    {"img": "star1.jpg", "titulo": "Análisis de dibujo", "url": "https://draw-recog.streamlit.app/"},
    {"img": "star3.jpg", "titulo": "Dígitos a mano", "url": "https://hand-wr.streamlit.app/"},
    {"img": "star2.jpg", "titulo": "Textos LSTM", "url": "https://lstmnlp.streamlit.app/"},
    {"img": "star1.jpg", "titulo": "Rec. óptico + Audio", "url": "https://ocr-audio-1.streamlit.app/"},
    {"img": "deco.png", "titulo": "Rec. óptico básico", "url": "https://rec-caracteres.streamlit.app/"},
    {"img": "obj2.jpg", "titulo": "Lector MQTT", "url": "https://lector-mqtt.streamlit.app/"},
    {"img": "obj3.jpg", "titulo": "Control MQTT", "url": "https://sendinput-mqtt.streamlit.app/"},
    {"img": "obj2.jpg", "titulo": "Análisis de sentimiento", "url": "https://sentimientooo.streamlit.app/"},
    {"img": "obj3.jpg", "titulo": "Tablerito", "url": "https://tableritooo.streamlit.app/"},
    {"img": "col1.jpg", "titulo": "TF-IDF Español", "url": "https://tdf--espanol.streamlit.app/"},
    {"img": "deco.png", "titulo": "TF-IDF Inglés", "url": "https://tf-idff.streamlit.app/"},
    {"img": "star1.jpg", "titulo": "Texto a voz", "url": "https://textovozcopia.streamlit.app/"},
    {"img": "deco.png", "titulo": "Rec. de gestos", "url": "https://gestosss.streamlit.app/"},
    {"img": "deco.png", "titulo": "Traductor", "url": "https://traductorrr.streamlit.app/"},
    {"img": "star1.jpg", "titulo": "Análisis de imagen", "url": "https://visionapppp.streamlit.app/"},
    {"img": "star2.jpg", "titulo": "Wordcloud", "url": "https://wordclouddd.streamlit.app/"},
    {"img": "col1.jpg", "titulo": "Detección objetos", "url": "https://yolov5v.streamlit.app/"}
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
