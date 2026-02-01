import streamlit as st
import os
from dotenv import load_dotenv

# Cargar variables de entorno si existen
load_dotenv(override=True)

st.set_page_config(
    page_title="Herramienta de Marketing GenAI",
    page_icon="🤖",
    layout="wide"
)

st.title("🚀 Herramienta de Marketing con IA Generativa")

st.markdown("""
### Bienvenido a tu Asistente Creativo

Esta herramienta empodera a tu equipo de marketing para crear y refinar contenido utilizando IA avanzada.

**Características:**
- **🎨 Generación de Imágenes**: Crea visuales impresionantes con Stable Diffusion.
- **📝 Editor de Contenido**: Refina tus textos con la asistencia de Claude.
- **🖼️ Galería**: Ve y gestiona tus activos creativos.

**Comenzando:**
Selecciona una herramienta de la barra lateral para comenzar tu viaje creativo.
""")

# Sidebar info
with st.sidebar:
    st.info("Estado: Sistema en Línea")
    if "user_role" in st.session_state:
        # Translate roles for display if needed, but keeping English internal keys is safer for logic
        roles_es = {"Viewer": "Visualizador", "Editor": "Editor", "Admin": "Administrador"}
        role_display = roles_es.get(st.session_state.user_role, st.session_state.user_role)
        st.write(f"Conectado como: **{role_display}**")
    else:
        st.session_state.user_role = "Viewer" # Default role
        st.write("Conectado como: **Visualizador**")
