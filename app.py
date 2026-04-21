import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib

# --- 1. IDENTIDAD Y GOBERNANZA (Soberanía Falasca) ---
OWNER = "Claudio Falasca Consultor"
VERSION = "v11.4 Master Core (Cox-Cycle Update)"

st.set_page_config(page_title=f"Terminal {OWNER}", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOTORES DE LÓGICA ---
def purga_atomica_forense():
    st.session_state.clear()
    st.cache_data.clear()
    st.rerun()

def mlc_guard(icr_score, roi_pct):
    if icr_score < 55 and roi_pct > 25.0:
        return False, "BLOQUEO MLC: ROI irrealista para el contexto regional."
    return True, "COHERENTE"

if 'sim_mode' not in st.session_state:
    st.session_state.sim_mode = False

# --- 3. ESTÉTICA DE ALTA DENSIDAD ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #080c10; color: #e8eaed; font-family: 'IBM Plex Sans', sans-serif; }}
    [data-testid="stSidebar"] {{ background-color: #0d1318; border-right: 2px solid #D4AF37; }}
    h1, h2, h3 {{ color: #D4AF37 !important; font-family: 'Syne', sans-serif; text-transform: uppercase; }}
    .kpi-box {{ background: #111920; border-left: 4px solid #D4AF37; padding: 15px; margin-bottom: 10px; border-radius: 2px; }}
    @keyframes pulseRed {{
      0% {{ box-shadow: inset 0 0 0px #FF3131; }}
      50% {{ box-shadow: inset 0 0 15px rgba(255,49,49,0.4); }}
      100% {{ box-shadow: inset 0 0 0px #FF3131; }}
    }}
    .sim-active {{ animation: pulseRed 2s infinite; border: 1px solid #FF3131 !important; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR E IDENTIDAD ---
with st.sidebar:
    st.title("MASTER CORE")
    st.subheader(OWNER)
    st.write("---")
    sources = st.number_input("Fuentes TGA Auditadas (C15)", value=112)
    tga_ok = sources >= 105
    st.markdown(f"**TGA Status:** {'<span style=\"color:#00FFFF\">VALIDADO</span>' if tga_ok else '<span style=\"color:#FF3131\">FALLO</span>'}", unsafe_allow_html=True)
    if st.button("🔥 PURGA ATÓMICA (C14)"):
        purga_atomica_forense()

if not tga_ok:
    st.error("ACCESO DENEGADO: El sistema requiere integridad de fuentes TGA.")
    st.stop()

# --- 5. DASHBOARD TERMINAL ---
tabs = st.tabs(["I. SUPERVIVENCIA COX", "II. BLINDAJE", "III. FORENSE", "IV. ORÁCULO", "V. DESPACHO"])

# --- TAB I: CAPA 16 ACTUALIZADA (COX VS CICLO MINERO) ---
with tabs[0]:
    st.subheader("Análisis de Supervivencia Estratégica (Capa 16)")
    
    # Definición de Fases del Ciclo Minero
    fases = {
        0: "Exploración", 
        5: "Factibilidad", 
        12: "Construcción", 
        22: "Operación", 
        30: "Optimización",
        35: "Cierre"
    }
    
    t = np.arange(0, 38, 1)
    # Curva Roja: Escenario Base (Hazard alto / Caída en Factibilidad)
    s_base = np.exp(-0.075 * t) * 100 
    # Curva Cyan: Proyección Claudio Falasca (Intervención en t=5)
    s_cf = np.exp(-0.022 * t) * 100 

    fig = go.Figure()
    
    # Sombreado de Zonas de Riesgo
    fig.add_vrect(x0=5, x1=12, fillcolor="rgba(255,49,49,0.1)", layer="below", line_width=0, annotation_text="ZONA CRÍTICA: FACTIBILIDAD")
    
    fig.add_trace(go.Scatter(x=t, y=s_base, name='Escenario Base (Sin Intervención)', 
                             line=dict(color='#FF3131', width=2, dash='dot')))
    fig.add_trace(go.Scatter(x=t, y=s_cf, name='Proyección Falasca (Gestión CF)', 
                             line=dict(color='#00FFFF', width=4)))

    fig.update_layout(
        xaxis=dict(
            tickvals=list(fases.keys()), 
            ticktext=list(fases.values()), 
            title="Ciclo de Proyecto Minero",
            gridcolor='rgba(255,255,255,0.05)'
        ),
        yaxis=dict(title="Probabilidad de Supervivencia S(t) %", gridcolor='rgba(255,255,255,0.05)'),
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)', 
        font=dict(color="white"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 Insight: La divergencia entre curvas en t=5 (Factibilidad) valida que la supervivencia se decide antes de la construcción.")

# --- TAB II: BLINDAJE TERRITORIAL ---
with tabs[1]:
    st.subheader("Certeza y Blindaje (C6-C9)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Certeza Jurídica (C6)", "72%", "+4%")
    c2.metric("ICR Regional (C12)", "52/100", "Riesgo Medio")
    c3.metric("Fricción Social (C17)", "Alta", delta_color="inverse")
    
    st.markdown("<div style='height:200px; border:1px solid #D4AF37; background:#111920; display:flex; align-items:center; justify-content:center;'>[ MAPA DE PROXIMIDAD C17 ACTIVO ]</div>", unsafe_allow_html=True)

# --- TAB IV: ORÁCULO Y WHAT-IF ---
with tabs[3]:
    st.subheader("Simulación What-If (C5)")
    col_w1, col_w2 = st.columns(2)
    
    with col_w1:
        ifs = st.slider("Ajuste Índice de Relacionamiento (IFS)", 0.0, 1.0, 0.40)
        if ifs != 0.40:
            st.session_state.sim_mode = True
            
    with col_w2:
        roi = 18.5 if not st.session_state.sim_mode else 29.0
        sello_class = "sim-active" if st.session_state.sim_mode else ""
        st.markdown(f"""
            <div class='kpi-box {sello_class}'>
                <b>ESTADO DEL SELLO C21</b><br>
                {'MODO SIMULACIÓN — NO FORENSE' if st.session_state.sim_mode else 'AUDITADO POR FALASCA'}
            </div>
        """, unsafe_allow_html=True)
        st.metric("ROI Proyectado", f"{roi}%")

# --- TAB V: DESPACHO ---
with tabs[4]:
    st.subheader("Entrega de Artefactos (C4)")
    valid, msg = mlc_guard(52, 29.0 if st.session_state.sim_mode else 18.5)
    
    if not valid:
        st.error(f"⚠️ {msg}")
        st.button("Generar Reporte PDF", disabled=True)
    else:
        st.success("Coherencia MLC Validada.")
        st.download_button("Descargar Master Report", data="DATA", file_name="Reporte_Falasca.pdf")

st.write("---")
st.caption(f"Terminal Operativa {VERSION} | Propiedad de {OWNER}")
