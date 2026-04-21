import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import hashlib

# --- 1. IDENTIDAD Y GOBERNANZA ---
OWNER = "Claudio Falasca Consultor"
VERSION = "v11.4.1 Master Core (IIF Component Injected)"

st.set_page_config(page_title=f"Terminal {OWNER}", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOTORES DE LÓGICA Y SEGURIDAD ---
def purga_atomica_forense():
    """C14: Purga absoluta de memoria de sesión y datos cacheados"""
    st.session_state.clear()
    st.cache_data.clear()
    st.rerun()

def mlc_guard(icr_score, roi_pct):
    """C20: Motor de Coherencia MLC (Bloqueo de incoherencias)"""
    if icr_score < 55 and roi_pct > 25.0:
        return False, "BLOQUEO MLC: Incoherencia crítica entre ICR regional y ROI proyectado."
    return True, "COHERENTE"

if 'sim_mode' not in st.session_state:
    st.session_state.sim_mode = False

# --- 3. ESTÉTICA FORENSE ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #080c10; color: #e8eaed; font-family: 'IBM Plex Sans', sans-serif; }}
    [data-testid="stSidebar"] {{ background-color: #0d1318; border-right: 2px solid #D4AF37; }}
    h1, h2, h3 {{ color: #D4AF37 !important; font-family: 'Syne', sans-serif; text-transform: uppercase; letter-spacing: 1px; }}
    .kpi-box {{ background: #111920; border-left: 4px solid #D4AF37; padding: 20px; border-radius: 2px; margin-bottom: 10px; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR SOBERANO ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/50/D4AF37/shield.png", width=50)
    st.title("OPERADOR SUPRA")
    st.subheader(OWNER)
    st.write("---")
    sources = st.number_input("Fuentes TGA (Mín. 105)", value=112)
    tga_valid = sources >= 105
    st.write(f"Soberanía: {'✅ VALIDADA' if tga_valid else '❌ INSUFICIENTE'}")
    if st.button("🔥 PURGA PERSEO (C14)"):
        purga_atomica_forense()

if not tga_valid:
    st.warning("BLOQUEO DE SISTEMA: Integridad TGA no alcanzada.")
    st.stop()

# --- 5. COMPONENTE IIF (C16 - INYECCIÓN DIRECTA) ---
# Aquí se integra el código HTML/JS enviado por IA-1 para la Capa 16
iif_html_component = """
<div style="background:#0d1318; padding:10px; border-radius:4px; border:1px solid rgba(255,255,255,0.1);">
    <iframe srcdoc='""" + open("iif_survival_component_v114.html", "r", encoding="utf-8").read().replace("'", "&apos;") + """' 
    style="width:100%; height:550px; border:none;"></iframe>
</div>
"""

# --- 6. DASHBOARD TERMINAL ---
tabs = st.tabs(["I. SUPERVIVENCIA IIF", "II. BLINDAJE", "III. FORENSE", "IV. ORÁCULO", "V. DESPACHO"])

# --- TAB I: SUPERVIVENCIA COX (INTEGRADO) ---
with tabs[0]:
    st.subheader("Visualización Supra: Inercia de Supervivencia (Capa 16)")
    components.html(open("iif_survival_component_v114.html", "r", encoding="utf-8").read(), height=600, scrolling=False)
    st.info("💡 Interpretación: La caída en t=12 (Construcción) es irreversible si no hay blindaje en Factibilidad.")

# --- TAB II: BLINDAJE TERRITORIAL ---
with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<div class='kpi-box'><b>Certeza Jurídica (C8)</b><br>Score: 74.2%</div>", unsafe_allow_html=True)
        st.markdown("<div class='kpi-box'><b>ICR Regional (C12)</b><br>Score: 52/100</div>", unsafe_allow_html=True)
    with col2:
        st.subheader("Mapa de Fricción C17")
        st.image("https://img.icons8.com/ios-filled/100/FF3131/map.png", width=80)
        st.caption("Nodo Crítico: Peñas Negras (Catamarca) - Alerta Activa")

# --- TAB IV: ORÁCULO Y WHAT-IF ---
with tabs[3]:
    st.subheader("Simulador What-If (C5)")
    roi_input = st.slider("ROI Proyectado (%)", 5.0, 45.0, 22.0)
    
    # Validación MLC en tiempo real
    ok, msg = mlc_guard(52, roi_input)
    if not ok:
        st.error(f"⚠️ {msg}")
        st.session_state.sim_mode = True
    else:
        st.success("Coherencia MLC: Validada")
        st.session_state.sim_mode = False

# --- TAB V: DESPACHO ---
with tabs[4]:
    st.subheader("Generación de Artefactos (C4)")
    if st.button("🚀 GENERAR DIRECTORIO DE CAPACIDADES V11.4"):
        st.write("Generando PDF 'Midnight Gold'...")
        st.download_button("Descargar PDF", data="PDF_CONTENT", file_name="Directorio_Falasca_v11.4.pdf")

st.write("---")
st.caption(f"Terminal Soberana {VERSION} | {OWNER}")
