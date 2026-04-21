import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib
import json

# --- 1. IDENTIDAD Y GOBERNANZA (CAPAS 1, 10, 11) ---
OWNER = "Claudio Falasca Consultor"
VERSION = "v11.2.9 Master Core"

st.set_page_config(page_title=f"Terminal {OWNER}", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOTOR DE CAPA 14 (PERSEO & PURGA) ---
def protocolo_purga_total():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- 3. ESTÉTICA HUARPE_V6 (CSS DE ALTA DENSIDAD) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #080c10; color: #e8eaed; font-family: 'IBM Plex Sans', sans-serif; }}
    [data-testid="stSidebar"] {{ background-color: #0d1318; border-right: 2px solid #D4AF37; }}
    h1, h2, h3 {{ color: #D4AF37 !important; font-family: 'Syne', sans-serif; text-transform: uppercase; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 10px; }}
    .stTabs [data-baseweb="tab"] {{ background-color: #111920; border: 1px solid rgba(212,175,55,0.2); color: #8899a6; padding: 10px 20px; }}
    .stTabs [aria-selected="true"] {{ border: 1px solid #D4AF37 !important; color: #D4AF37 !important; }}
    .forense-card {{ border: 1px solid rgba(212,175,55,0.3); background: #0d1318; padding: 15px; border-radius: 4px; }}
    .status-cyan {{ color: #00FFFF; font-family: monospace; font-weight: bold; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. GATEKEEPER Y SEGURIDAD (CAPA 15, 20) ---
with st.sidebar:
    st.markdown(f"### {OWNER}")
    st.caption(f"MODO: OPERADOR SOBERANO")
    st.write("---")
    sources = st.number_input("Fuentes TGA Auditadas (C15)", value=112)
    tga_ok = sources >= 105
    mlc_coherence = "VALIDADA" if tga_ok else "DISRUPCIÓN" # Capa 20
    
    st.write(f"**TGA Status:** {'✅ OK' if tga_ok else '❌ BLOQUEADO'}")
    st.write(f"**MLC Coherence (C20):** {mlc_coherence}")
    
    st.write("---")
    if st.button("🔥 RESET ATÓMICO (C14)"):
        protocolo_purga_total()
    st.caption(f"Identidad Unificada: {OWNER}")

if not tga_ok:
    st.error("⛔ SISTEMA BLOQUEADO: Capa 15 no validada (Fuentes < 105).")
    st.stop()

# --- 5. ESTRUCTURA DE 21 CAPAS (DASHBOARD OCD) ---
st.title("🛡️ Copiloto Minero — Terminal Master Core")

tabs = st.tabs([
    "I. Diagnóstico (C2, 16)", 
    "II. Blindaje (C6-C9, 17)", 
    "III. Forense (C15, 20, 21)", 
    "IV. Oráculo (C3, 5, 12, 18)", 
    "V. Despacho (C4, 14)"
])

# --- TAB I: INTELIGENCIA PREDICTIVA ---
with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Radar Heptagonal (Capa 2)")
        df_rad = pd.DataFrame({"Eje": ["Reg", "Amb", "Ope", "Soc", "Est", "Hid", "Eco"], "Val": [82, 38, 58, 44, 49, 61, 72]})
        fig_rad = px.line_polar(df_rad, r='Val', theta='Eje', line_close=True, color_discrete_sequence=['#D4AF37'])
        fig_rad.update_traces(fill='toself', fillcolor='rgba(212,175,55,0.1)')
        fig_rad.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_rad, use_container_width=True)
    with col2:
        st.subheader("Decaimiento Temporal (Capa 16)")
        x = np.arange(0, 37, 1)
        y = np.exp(-0.035 * x) * 100
        fig_cox = go.Figure()
        fig_cox.add_trace(go.Scatter(x=x, y=y, name='Curva Falasca', line=dict(color='#00FFFF', width=4)))
        fig_cox.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), xaxis_title="Meses", yaxis_title="Supervivencia %")
        st.plotly_chart(fig_cox, use_container_width=True)

# --- TAB II: BLINDAJE Y PROXIMIDAD ---
with tabs[1]:
    st.subheader("Mapa de Riesgo y Aliados (C6, 7, 8, 9, 17)")
    c_map, c_risk = st.columns([2, 1])
    with c_map:
        # Capa 17: Riesgo por Proximidad
        st.markdown(f"""
            <div style='height:400px; border:1px solid #D4AF37; background:#111920; position:relative; display:flex; align-items:center; justify-content:center;'>
                <div style='text-align:center;'>
                    <p style='color:#D4AF37; font-family:monospace;'>[ CAPA 17: MAPA DE PROXIMIDAD ACTIVO ]</p>
                    <p style='color:#FF3131; font-size:12px;'>● 3 Focos de Fricción detectados < 50km</p>
                    <p style='color:#00FFFF; font-size:12px;'>★ 2 Nodos de Apoyo (C7) en radio operativo</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with c_risk:
        st.metric("Certeza Jurídica (C8)", "74%", "+2.1%")
        st.metric("ICR Regional (C12)", "0.68", "-0.05")
        st.write("**Protocolo Capa 9:**")
        st.warning("⚠️ Mitigación Hídrica Nivel 2 requerida.")

# --- TAB III: INTEGRIDAD FORENSE ---
with tabs[2]:
    st.subheader("Capa 21: Sello de Integridad Forense")
    st.markdown(f"""
        <div class='forense-card'>
            <code>HASH_SESSION: {hashlib.sha256(str(np.random.random()).encode()).hexdigest()}</code><br>
            <code>OPERADOR: {OWNER}</code><br>
            <code>STATUS: TGA_CERTIFIED (C15)</code>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.write("**Evidencia TGA (Top 20 URLs):**")
    st.caption("1. https://asambleapucara.org/conflictos-litio (Fricción Territorial)")
    st.caption("2. https://boletin.catamarca.gob.ar (Regulatorio)")
    st.caption("3. https://ocmal.org/argentina (Conflictos Socioambientales)")

# --- TAB IV: ORÁCULO Y WHAT-IF ---
with tabs[3]:
    st.subheader("Capas 3, 5 y 18: Estrategia y Pricing")
    cw1, cw2 = st.columns(2)
    with cw1:
        st.write("**Simulador What-If (Capa 5)**")
        val = st.slider("Modificar Factor de Riesgo Social", 0.0, 1.0, 0.42)
        if val > 0.55:
            st.error("⚠️ SELLO CAPA 21 ROTO: MODO SIMULACIÓN")
    with cw2:
        st.markdown(f"""
            <div class='forense-card'>
                <p style='color:#D4AF37;'><b>ESTRATEGIA ORÁCULO</b></p>
                <p>Retainer: $22,500 USD</p>
                <p>Éxito: 2.0% EBITDA Proyectado</p>
                <p><small>Marca: {OWNER}</small></p>
            </div>
        """, unsafe_allow_html=True)

# --- TAB V: DESPACHO ---
with tabs[4]:
    st.subheader("Despacho de Artefactos (C4, 14)")
    cd1, cd2 = st.columns(2)
    with cd1:
        st.markdown("**Ventana de Perseo (C14)**")
        if st.button("🛡️ Sanitizar para Cliente"):
            st.toast("Protocolo Perseo activado.")
            st.session_state.sanitized = True
        if st.session_state.get('sanitized'):
            st.success("Modo Cliente: Identidad de activos protegida.")
    with cd2:
        st.markdown("**Entrega (C4)**")
        st.download_button("Descargar Propuesta Comercial (PDF)", data="PDF_DATA", file_name="Propuesta_Falasca.pdf")
        if st.button("🔑 Director's Brief"):
            st.markdown(f"<div style='background:#D4AF37; color:#080c10; padding:10px; font-weight:bold;'>ROI Proyectado: 22.4% | Alerta Aliados: Catamarca Ready</div>", unsafe_allow_html=True)

st.write("---")
st.caption(f"Terminal Soberana {VERSION} | {OWNER}")
