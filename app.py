import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib

# --- 1. IDENTIDAD Y GOBERNANZA ---
OWNER = "Claudio Falasca Consultor"
VERSION = "v11.3 Master Core"

st.set_page_config(page_title=f"Terminal {OWNER}", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOTORES DE LÓGICA (C14 y C20) ---
def purga_atomica_forense():
    """C14: Limpieza absoluta de cliente preservando el motor ML"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.cache_data.clear() # Limpia datos de cliente, mantiene recursos del sistema
    st.rerun()

def mlc_guard(icr_score, roi_pct):
    """C20: Detección de Incoherencia Territorio-Retorno"""
    if icr_score < 55 and roi_pct > 25.0:
        return False, "BLOQUEO MLC: ROI > 25% es irrealista con ICR < 55."
    return True, "COHERENTE"

# Inicializar variables de sesión para el Simulador
if 'sim_mode' not in st.session_state:
    st.session_state.sim_mode = False
if 'roi_proyectado' not in st.session_state:
    st.session_state.roi_proyectado = 22.4 # Base ROI

# --- 3. ESTÉTICA HUARPE_V6 Y CSS DINÁMICO ---
sim_css = """
    @keyframes pulseRed {
      0% { box-shadow: inset 0 0 0px #FF3131, 0 0 0px #FF3131; }
      50% { box-shadow: inset 0 0 10px #FF3131, 0 0 15px rgba(255,49,49,0.5); }
      100% { box-shadow: inset 0 0 0px #FF3131, 0 0 0px #FF3131; }
    }
    .sim-alert { animation: pulseRed 2s infinite; border: 1px solid #FF3131 !important; }
""" if st.session_state.sim_mode else ""

st.markdown(f"""
    <style>
    .stApp {{ background-color: #080c10; color: #e8eaed; font-family: 'IBM Plex Sans', sans-serif; }}
    [data-testid="stSidebar"] {{ background-color: #0d1318; border-right: 2px solid #D4AF37; }}
    h1, h2, h3 {{ color: #D4AF37 !important; font-family: 'Syne', sans-serif; }}
    .kpi-box {{ background: #111920; border-left: 4px solid #D4AF37; padding: 15px; margin-bottom: 10px; }}
    {sim_css}
    </style>
""", unsafe_allow_html=True)

# Banner de Simulación Global
if st.session_state.sim_mode:
    st.markdown("<div style='background:#FF3131; color:white; text-align:center; padding:5px; font-weight:bold; letter-spacing:2px;'>⚠️ MODO SIMULACIÓN ACTIVO — SELLO NO FORENSE ⚠️</div>", unsafe_allow_html=True)

# --- 4. GATEKEEPER TGA (C15) ---
with st.sidebar:
    st.markdown(f"### {OWNER}")
    st.caption("OPERADOR SOBERANO")
    st.write("---")
    sources = st.number_input("Fuentes TGA Auditadas (C15)", value=112)
    tga_ok = sources >= 105
    
    # Parámetros Base para MLC
    icr_actual = 48 # Índice de Competitividad Regional (Ejemplo)
    
    st.write(f"**TGA Status:** {'✅ OK' if tga_ok else '❌ BLOQUEADO'}")
    
    st.write("---")
    if st.button("🔥 PURGA ATÓMICA (C14)", type="primary"):
        purga_atomica_forense()

if not tga_ok:
    st.error("⛔ SISTEMA BLOQUEADO: Capa 15 no validada (Fuentes < 105).")
    st.stop()

# --- 5. DASHBOARD TERMINAL ---
st.title("🛡️ Copiloto Minero — Master Core")

tabs = st.tabs(["I. Diagnóstico", "II. Blindaje", "III. Forense", "IV. Oráculo", "V. Despacho"])

# --- TAB I: DIAGNÓSTICO ---
with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Radar Heptagonal (C2)")
        df_rad = pd.DataFrame({"Eje": ["Reg", "Amb", "Ope", "Soc", "Est", "Hid", "Eco"], "Val": [82, 38, 58, 44, 49, 61, 72]})
        fig_rad = px.line_polar(df_rad, r='Val', theta='Eje', line_close=True, color_discrete_sequence=['#D4AF37'])
        fig_rad.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_rad, use_container_width=True)
    with c2:
        st.subheader("Curva de Supervivencia (C16)")
        x = np.arange(0, 37, 1)
        y = np.exp(-0.035 * x) * 100
        fig_cox = go.Figure(data=go.Scatter(x=x, y=y, line=dict(color='#00FFFF', width=3)))
        fig_cox.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_cox, use_container_width=True)

# --- TAB II: BLINDAJE TERRITORIAL ---
with tabs[1]:
    st.subheader("Estructura de Riesgo y Apoyo (C6-C9, C12, C17)")
    # KPIs Superiores
    k1, k2, k3 = st.columns(3)
    k1.markdown(f"<div class='kpi-box'><b>ICR Regional (C12)</b><br><span style='font-size:24px; color:#00FFFF;'>{icr_actual}/100</span></div>", unsafe_allow_html=True)
    k2.markdown("<div class='kpi-box'><b>Certeza Jurídica (C8)</b><br><span style='font-size:24px; color:#D4AF37;'>68%</span></div>", unsafe_allow_html=True)
    k3.markdown("<div class='kpi-box'><b>Fricción Activa (C17)</b><br><span style='font-size:24px; color:#FF3131;'>Nivel Alto</span></div>", unsafe_allow_html=True)
    
    # Dual Layout: Riesgo vs Apoyo
    cm1, cm2 = st.columns(2)
    with cm1:
        st.markdown("<div style='background:#111920; border:1px solid #FF3131; padding:20px; text-align:center;'><h4 style='color:#FF3131;'>MAPA DE FRICCIÓN</h4><p>● Zona de Conflicto Activa</p></div>", unsafe_allow_html=True)
    with cm2:
        st.markdown("<div style='background:#111920; border:1px solid #00FFFF; padding:20px; text-align:center;'><h4 style='color:#00FFFF;'>NODOS DE APOYO</h4><p>◆ Aliado Logístico Validado</p></div>", unsafe_allow_html=True)

# --- TAB III: FORENSE ---
with tabs[2]:
    st.subheader("Integridad y Evidencia (C15, C21)")
    sello_class = "sim-alert" if st.session_state.sim_mode else ""
    st.markdown(f"""
        <div class='kpi-box {sello_class}'>
            <h4 style='margin:0;'>SELLO FORENSE C21</h4>
            <code>HASH: {hashlib.sha256(str(np.random.random()).encode()).hexdigest()}</code><br>
            <code>ESTADO: {'NO FORENSE (SIMULACIÓN)' if st.session_state.sim_mode else 'AUDITADO'}</code>
        </div>
    """, unsafe_allow_html=True)
    st.write("**Top URLs Auditadas:**")
    st.caption("1. https://asambleapucara.org/conflictos (Riesgo Social)")

# --- TAB IV: ORÁCULO Y WHAT-IF ---
with tabs[3]:
    st.subheader("Estrategia y Simulación (C3, C5)")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.write("**Simulador What-If (C5)**")
        ifs = st.slider("Ajuste de Impacto Social", 0.0, 1.0, 0.45)
        
        # Lógica de ruptura de sello
        if ifs != 0.45 and not st.session_state.sim_mode:
            st.session_state.sim_mode = True
            st.session_state.roi_proyectado = 28.5 # Sube el ROI por simulación
            st.rerun()
        elif ifs == 0.45 and st.session_state.sim_mode:
            st.session_state.sim_mode = False
            st.session_state.roi_proyectado = 22.4
            st.rerun()
            
    with col_w2:
        st.markdown(f"<div class='kpi-box'><b>Honorarios Oráculo</b><br>Retainer: $22,500<br>ROI Proyectado: {st.session_state.roi_proyectado}%</div>", unsafe_allow_html=True)

# --- TAB V: DESPACHO ---
with tabs[4]:
    st.subheader("Despacho y Soberanía (C4, C14, C20)")
    
    # Motor MLC (Coherencia)
    mlc_valid, mlc_msg = mlc_guard(icr_actual, st.session_state.roi_proyectado)
    
    cd1, cd2 = st.columns(2)
    with cd1:
        st.markdown("**Ventana de Perseo (C14)**")
        if st.button("🛡️ Sanitizar Visibilidad"):
            st.success("Modo Cliente Activo. Identidad protegida.")
    with cd2:
        st.markdown("**Artefactos (C4)**")
        if not mlc_valid:
            st.error(mlc_msg)
            st.button("Descargar PDF", disabled=True, help="Bloqueado por MLC")
        elif st.session_state.sim_mode:
            st.warning("⚠️ El PDF saldrá con marca de agua 'SIMULACIÓN'.")
            st.download_button("Descargar PDF (Simulado)", data="PDF", file_name="Propuesta.pdf")
        else:
            st.download_button("Descargar Propuesta Oficial (PDF)", data="PDF", file_name="Propuesta_Falasca.pdf")

st.write("---")
st.caption(f"Propiedad Intelectual y Operación Exclusiva: {OWNER}")
