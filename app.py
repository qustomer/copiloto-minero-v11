import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# --- 1. IDENTIDAD Y GOBERNANZA (Sello de Autoridad) ---
OWNER = "Claudio Falasca Consultor"
VERSION = "v11.4.2 Master Core (Robust-Link)"

st.set_page_config(page_title=f"Terminal {OWNER}", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOTORES DE SEGURIDAD ---
def purga_atomica():
    st.session_state.clear()
    st.cache_data.clear()
    st.rerun()

# --- 3. ESTÉTICA FORENSE ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #080c10; color: #e8eaed; font-family: 'IBM Plex Sans', sans-serif; }}
    [data-testid="stSidebar"] {{ background-color: #0d1318; border-right: 2px solid #D4AF37; }}
    h1, h2, h3 {{ color: #D4AF37 !important; font-family: 'Syne', sans-serif; text-transform: uppercase; }}
    .kpi-box {{ background: #111920; border-left: 4px solid #D4AF37; padding: 20px; border-radius: 4px; margin-bottom: 15px; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("OPERADOR")
    st.subheader(OWNER)
    st.write("---")
    sources = st.number_input("Fuentes TGA Auditadas", value=112)
    if st.button("🔥 PURGA PERSEO (C14)"):
        purga_atomica()

# --- 5. COMPONENTE IIF INTEGRADO (CON MANEJO DE ERRORES) ---
# He simplificado el JS para evitar bloqueos en el hilo principal de Streamlit
iif_html_core = """
<!DOCTYPE html>
<html>
<body style="background:#080c10; margin:0;">
    <canvas id="cv" width="800" height="400" style="border:1px solid #D4AF37;"></canvas>
    <script>
        const c = document.getElementById('cv');
        const ctx = c.getContext('2d');
        // Dibujo de curvas simplificado para máxima estabilidad
        ctx.strokeStyle="#FF3131"; ctx.setLineDash([5,5]); ctx.moveTo(50,50); ctx.lineTo(750,350); ctx.stroke();
        ctx.beginPath(); ctx.strokeStyle="#00FFFF"; ctx.setLineDash([]); ctx.moveTo(50,50); ctx.quadraticCurveTo(400,50,750,150); ctx.stroke();
        ctx.fillStyle="#D4AF37"; ctx.font="12px Arial"; ctx.fillText("MARGEN DE INTERVENCIÓN FALASCA", 300, 30);
    </script>
</body>
</html>
"""

# --- 6. RENDERIZADO DE CAPAS (TABS) ---
# Separamos los contenidos para asegurar que un error en uno no afecte al resto
tabs = st.tabs(["I. SUPERVIVENCIA IIF", "II. BLINDAJE", "III. FORENSE", "IV. ORÁCULO", "V. DESPACHO"])

with tabs[0]:
    st.subheader("Capa 16: Análisis de Supervivencia")
    try:
        components.html(iif_html_core, height=450)
    except Exception as e:
        st.error("Error al cargar componente visual. Reintente purga C14.")

with tabs[1]:
    st.subheader("Capa 6: Blindaje Territorial")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='kpi-box'><b>ICR Regional:</b> 52/100</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='kpi-box'><b>Fricción Social:</b> Alta</div>", unsafe_allow_html=True)

with tabs[2]:
    st.subheader("Capa 21: Auditoría Forense")
    st.write("Sello de Integridad Hash: `8f92b...3a1`")
    st.info("Estado: FIRMADO Y SELLADO")

with tabs[3]:
    st.subheader("Capa 5: Oráculo What-If")
    roi = st.slider("ROI Objetivo", 0, 50, 25)
    st.metric("Probabilidad de Éxito", f"{100 - (roi/2)}%")

with tabs[4]:
    st.subheader("Capa 4: Despacho de Artefactos")
    st.button("Generar Reporte Midnight Gold")

st.write("---")
st.caption(f"Terminal Soberana {VERSION} | Propiedad de {OWNER}")# ==============================================================================
# UI COPILOTO — CABINA DE CONTROL
# ==============================================================================

st.set_page_config(page_title="Copiloto Heptágono v11.5", layout="wide")

st.title("🧭 Copiloto Estratégico Minero — Heptágono v11.5")

st.sidebar.header("Datos del Proyecto")

proyecto = st.sidebar.text_input("Nombre del Proyecto", "Proyecto Demo")
territorio = st.sidebar.text_input("Territorio", "Argentina")
roi = st.sidebar.slider("ROI esperado (%)", 0, 80, 25)

st.sidebar.markdown("---")
st.sidebar.subheader("Scores base de ejes")

scores = {}
for eje in EJES_OFICIALES:
    scores[eje] = st.sidebar.slider(eje, 0, 100, 70)

st.sidebar.markdown("---")
ejecutar = st.sidebar.button("🚀 Ejecutar análisis")

# ==============================================================================
# EJECUCIÓN DEL PIPELINE
# ==============================================================================

if ejecutar:

    payload = ejecutar_pipeline_certificado(
        proyecto,
        territorio,
        scores,
        roi
    )

    render_dashboard(payload)

    # ==============================
    # MÉTRICAS
    # ==============================
    col1, col2, col3 = st.columns(3)
    col1.metric("ROI", f"{payload['indicadores']['roi']} %")
    col2.metric("ICR", f"{payload['indicadores']['icr']:.2f}")
    col3.metric("MLC", payload["seguridad"]["mlc_status"])

    # ==============================
    # TABLA DE SCORES
    # ==============================
    st.subheader("Scores por eje")
    df = pd.DataFrame.from_dict(
        payload["indicadores"]["scores"],
        orient="index",
        columns=["Score"]
    )
    st.dataframe(df)

    # ==============================
    # RADAR HEPTÁGONO
    # ==============================
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=list(payload["indicadores"]["scores"].values()),
        theta=list(payload["indicadores"]["scores"].keys()),
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,100])),
        showlegend=False,
        title="Radar Estratégico Heptágono"
    )

    st.plotly_chart(fig, use_container_width=True)
