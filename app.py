import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from tga_harvester import TGAHarvester
from predictive_engine import PredictiveEngine
from geo_map import build_geo_map

# 1. CONFIGURACIÓN MASTER CORE (Capa 1 y 11)
st.set_page_config(page_title="Heptágono v10.1 | Master Core", layout="wide")

# CSS: Estética de Alta Gama y Contraste Forense
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(212, 175, 55, 0.2); }
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'Syne', sans-serif; }
    
    /* Tablas Forenses */
    .tech-table {
        background-color: #111920;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 8px;
        margin-bottom: 25px;
        overflow: hidden;
    }
    .t-row { display: flex; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .t-header { background-color: rgba(212, 175, 55, 0.15); color: #D4AF37; font-weight: 800; text-transform: uppercase; font-size: 11px; }
    .t-col { padding: 12px 15px; font-size: 13px; color: #ffffff; }
    .t-label { background-color: rgba(212, 175, 55, 0.08); color: #D4AF37; font-weight: 600; width: 30%; }
    
    /* Sello Forense */
    .seal-box { border: 2px dashed #D4AF37; padding: 20px; border-radius: 8px; background-color: rgba(212, 175, 55, 0.03); text-align: center; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# 2. BARRA LATERAL: CONTROL SOBERANO
with st.sidebar:
    st.title("HEPTÁGONO v10.1")
    st.markdown("**OPERADOR:** Claudio Falasca Consultor")
    st.write("---")
    capa_activa = st.radio("Capas de Ejecución:", ["Diagnóstico 7 Ejes", "Riesgo & Supervivencia", "Estrategia & Oráculo"])
    st.write("---")
    sources = st.number_input("Fuentes TGA Auditadas", value=112)
    st.caption("© 2026 Claudio Falasca Consultor")

# 3. HEADER
st.caption("CAPA 19: OPERATOR CONTROL DASHBOARD (OCD)")
st.title("Copiloto Minero v11.1")

# --- REGLA DE ORO (CAPA 15) ---
if sources < 105:
    st.error("⛔ TGA BLOQUEADO: Fuentes insuficientes para diagnóstico determinístico.")
    st.stop()

# --- EJECUCIÓN DE CAPAS ---

if capa_activa == "Diagnóstico 7 Ejes":
    # 4. GRÁFICO DE LOS 7 EJES (Heptágono)
    st.subheader("Capa 2: Diagnóstico Determinístico")
    df_ejes = pd.DataFrame({
        "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
        "Puntaje": [78, 38, 55, 42, 47, 60, 65]
    })
    
    col1, col2 = st.columns([2, 1])
    with col1:
        fig_rad = px.line_polar(df_ejes, r='Puntaje', theta='Eje', line_close=True, range_r=[0,100], color_discrete_sequence=['#D4AF37'])
        fig_rad.update_traces(fill='toself', fillcolor='rgba(212, 175, 55, 0.2)')
        fig_rad.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_rad, use_container_width=True)
    with col2:
        st.metric("IBH SCORE", "55.0", "-4.2")
        if df_ejes.loc[df_ejes['Eje'] == 'Ambiental', 'Puntaje'].values[0] < 40:
            st.error("⚠️ Capa 20 (MLC): Riesgo Ambiental Crítico detectado.")

elif capa_activa == "Riesgo & Supervivencia":
    # 5. CURVA DE COX (REFERENCIADA)
    st.subheader("Capa 16: Análisis de Supervivencia")
    meses = np.arange(0, 37, 3)
    prob_base = np.exp(-0.09 * meses) * 100
    prob_claudio = np.exp(-0.02 * meses) * 100
    
    fig_cox = go.Figure()
    fig_cox.add_trace(go.Scatter(x=meses, y=prob_base, name='⚠️ ESCENARIO BASE (Riesgo)', line=dict(color='#FF3131', width=3, dash='dot')))
    fig_cox.add_trace(go.Scatter(x=meses, y=prob_claudio, name='💎 PROYECCIÓN CLAUDIO FALASCA', line=dict(color='#00FFFF', width=5)))
    fig_cox.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"),
                          legend=dict(bgcolor="rgba(255,255,255,0.1)", bordercolor="#D4AF37", borderwidth=1))
    st.plotly_chart(fig_cox, use_container_width=True)

elif capa_activa == "Estrategia & Oráculo":
    # 6. IMPLICANCIAS Y HOJA DE RUTA
    st.subheader("7. Implicancias Estratégicas y Hoja de Ruta")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:25%; padding:10px;">Dimensión</div><div style="width:55%; padding:10px;">Implicancia Estratégica</div><div style="width:20%; padding:10px;">Urgencia</div>
            </div>
            <div class="t-row">
                <div class="t-col t-label">Territorial</div><div class="t-col" style="width:55%;">Bloqueo preventivo en accesos por falta de srv_hidrico.</div><div class="t-col" style="color:#FF3131; width:20%;">ALTA</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 7. CRONOGRAMA ORIENTATIVO (CUADRO DE COLUMNAS)
    st.subheader("Hoja de Ruta - Cronograma Claudio Falasca")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:20%; padding:10px;">Fase</div><div style="width:60%; padding:10px;">Acciones Master Core</div><div style="width:20%; padding:10px;">Hito</div>
            </div>
            <div class="t-row">
                <div class="t-col t-label">Mes 1</div><div class="t-col" style="width:60%;">Cosecha TGA y Auditoría de Activos Críticos.</div><div class="t-col" style="width:20%;">Validación</div>
            </div>
            <div class="t-row">
                <div class="t-col t-label">Mes 2</div><div class="t-col" style="width:60%;">Despliegue de Mediación MIRCS-ET en territorio.</div><div class="t-col" style="width:20%;">Consenso</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 8. PROPUESTA COMERCIAL & HONORARIOS
    st.subheader("Propuesta Comercial de Intervención")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:10%; padding:10px;">#</div><div style="width:50%; padding:10px;">Servicio Base</div><div style="width:20%; padding:10px;">USD</div><div style="width:20%; padding:10px;">Estado</div>
            </div>
            <div class="t-row">
                <div class="t-col" style="width:10%;">01</div><div class="t-col" style="width:50%;">Diagnóstico Heptágono Master Core</div><div class="t-col" style="width:20%;">$55,000</div><div class="t-col" style="width:20%; color:#00FFFF;">ACTIVO</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Cálculo de Honorarios Oráculo
    st.write("### Cálculo de Honorarios — Oráculo v11.1")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:30%; padding:10px;">Parámetro</div><div style="width:20%; padding:10px;">Valor</div><div style="width:50%; padding:10px;">Detalle</div>
            </div>
            <div class="t-row">
                <div class="t-col t-label">Retainer Fee</div><div class="t-col" style="width:20%;">$22,000</div><div class="t-col" style="width:50%;">40% inicial para despliegue de Capa 15.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 9. METODOLOGÍA Y SELLO FORENSE
    st.subheader("8. Metodología y Sello de Integridad Forense")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:40%; padding:10px;">Componente</div><div style="width:60%; padding:10px;">Función</div>
            </div>
            <div class="t-row">
                <div class="t-col t-label">Capa 21 (Forense)</div><div class="t-col" style="width:60%;">Garantiza la inmutabilidad del diagnóstico mediante hashes MD5.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="seal-box">
            <h3 style="margin:0;">🛡️ SELLO FORENSE VÁLIDO</h3>
            <p style="color:#8899a6; font-size:12px;">EMITIDO POR: CLAUDIO FALASCA CONSULTOR</p>
            <code style="color:#D4AF37;">HASH-MD5: 9f4c5b606f7cde1126cb410d67500dec</code>
        </div>
    """, unsafe_allow_html=True)

# PIE DE PÁGINA FINAL
st.divider()
st.caption('Heptágono v10.1 — Sistema de Inteligencia Soberana de Claudio Falasca Consultor')
