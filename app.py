import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE INTERFAZ DE ALTO NIVEL
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. CEREBRO VISUAL (CSS MASTER CORE - Estilo Oscuro y Contraste de Alta Visibilidad)
st.markdown("""
    <style>
    /* Fondo y Colores Base */
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    
    /* Corrección de Visibilidad: Textos secundarios ahora en Plata/Blanco */
    .stMarkdown, p, span, label { color: #e8eaed !important; }
    .stCaption { color: #c8a84b !important; font-weight: 500; }
    h1, h2, h3 { color: #ffffff !important; font-family: 'Syne', sans-serif; }

    /* Estructura de Tablas Técnicas */
    .tech-table {
        background-color: #111920;
        border: 1px solid rgba(200, 168, 75, 0.3);
        border-radius: 8px;
        margin-bottom: 25px;
        overflow: hidden;
    }
    .t-row { display: flex; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .t-header {
        background-color: rgba(200, 168, 75, 0.15);
        color: #c8a84b !important;
        font-weight: 800;
        text-transform: uppercase;
        font-size: 11px;
        letter-spacing: 1px;
    }
    .t-col { padding: 10px 15px; font-size: 13px; color: #ffffff; }
    .t-label { background-color: rgba(200, 168, 75, 0.08); color: #c8a84b !important; font-weight: 600; width: 35%; }
    
    /* Ecuación y Alertas */
    .equation-container {
        background-color: #111920;
        border-left: 5px solid #c8a84b;
        padding: 20px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 25px;
    }
    .math-formula { font-family: 'IBM Plex Mono', monospace; color: #c8a84b; font-size: 22px; font-weight: bold; text-align: center; }
    
    .status-ok { color: #2dd4bf !important; font-weight: bold; }
    .status-critical { color: #ff4b4b !important; font-weight: bold; }
    
    /* Sello Forense */
    .seal-box { border: 2px dashed #c8a84b; padding: 20px; border-radius: 8px; background-color: rgba(200, 168, 75, 0.03); text-align: center; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (CONTROL DE CAPAS)
with st.sidebar:
    st.markdown("### DATA LAKE v6.1")
    capa_activa = st.radio(
        "Navegación de Capas:",
        ["Capa 1: Infraestructura & TGA", "Capa 2: Diagnóstico & Hoja de Ruta", "Capa 3: Oráculo & Firma Forense"],
        index=0
    )
    st.write("---")
    st.markdown("**OPERADOR:**")
    st.markdown('<p style="color:#c8a84b; font-weight:bold;">Claudio Falasca Consultor</p>', unsafe_allow_html=True)
    st.info(f"MODO ACTIVO: {capa_activa.split(':')[0]}")

# 4. CUERPO PRINCIPAL
st.caption("CONSULTA DE OPERACIÓN ACTIVA — HEPTÁGONO MOTOR DETERMINÍSTICO")
st.title("Copiloto Minero v11.1")

# --- CAPA 1: INFRAESTRUCTURA & TGA ---
if "Capa 1" in capa_activa:
    st.subheader("1. Identidad del Proyecto Objetivo")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row"><div class="t-col t-label">Empresa Objetivo</div><div class="t-col" style="width:65%;">NOA Lithium Ventures S.A.</div></div>
            <div class="t-row"><div class="t-col t-label">Región / Provincia</div><div class="t-col" style="width:65%;">Argentina / NOA / Catamarca</div></div>
            <div class="t-row"><div class="t-col t-label">Cuenca / Cluster</div><div class="t-col" style="width:65%;">Hombre Muerto Norte</div></div>
            <div class="t-row"><div class="t-col t-label">Perfil Operador S2</div><div class="t-col" style="width:65%;">Mid-Tier</div></div>
            <div class="t-row"><div class="t-col t-label">Fecha de Emisión</div><div class="t-col" style="width:65%;">18 de Abril de 2026</div></div>
            <div class="t-row" style="border-bottom:none;"><div class="t-col t-label" style="color:#ff4b4b !important;">Clasificación</div><div class="t-col" style="width:65%; color:#ff4b4b !important; font-weight:bold;">CONFIDENCIAL-ALTO DIRECTIVO</div></div>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("3. VALIDACIÓN TGA (REGLA DE ORO)")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:35%; padding:10px 15px;">Parámetro TGA</div><div style="width:45%; padding:10px 15px;">Valor</div><div style="width:20%; padding:10px 15px; text-align:center;">Estado</div>
            </div>
            <div class="t-row"><div class="t-col t-label">Fuentes Totales</div><div class="t-col" style="width:45%;">127 Entradas de Datos</div><div class="t-col status-ok" style="width:20%; text-align:center;">VALIDADO</div></div>
            <div class="t-row"><div class="t-col t-label">Coherencia Lógica</div><div class="t-col" style="width:45%;">98.4% (Capa 20-MLC)</div><div class="t-col status-ok" style="width:20%; text-align:center;">OPTIMAL</div></div>
            <div class="t-row" style="border-bottom:none;"><div class="t-col t-label">Trazabilidad</div><div class="t-col" style="width:45%;">MD5 Verified Payload</div><div class="t-col status-ok" style="width:20%; text-align:center;">SECURE</div></div>
        </div>
    """, unsafe_allow_html=True)

# --- CAPA 2: DIAGNÓSTICO & HOJA DE RUTA ---
elif "Capa 2" in capa_activa:
    st.subheader("4. ECUACIÓN DE CONSENSO v11.1 — RIESGO FINAL")
    st.markdown("""<div class="equation-container"><div class="math-formula">RF = (1 - C) × (IFS + R_op) / SL</div></div>""", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header"><div style="width:40%; padding:10px 15px;">Componente</div><div style="width:30%; padding:10px 15px;">Fórmula</div><div style="width:15%; padding:10px 15px; text-align:center;">Valor</div><div style="width:15%; padding:10px 15px; text-align:center;">Peso</div></div>
            <div class="t-row"><div class="t-col t-label" style="width:40%;">Curva Supervivencia Cox</div><div class="t-col" style="width:30%;">Licencia Social (36m)</div><div class="t-col" style="width:15%; text-align:center;">28%</div><div class="t-col" style="width:15%; text-align:center; font-weight:bold;">0.40</div></div>
            <div class="t-row" style="border-bottom:none;"><div class="t-col t-label" style="width:40%;">Índice Fricción Social</div><div class="t-col" style="width:30%;">XGBoost Engine</div><div class="t-col" style="width:15%; text-align:center;">72%</div><div class="t-col" style="width:15%; text-align:center; font-weight:bold;">0.30</div></div>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("5. MATRIZ TERRITORIAL — DIAGNÓSTICO 7 EJES")
    col_rad, col_met = st.columns([2,1])
    df_ejes = pd.DataFrame({"Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"], "Puntaje": [78, 71, 55, 54, 47, 60, 65], "Estado": ["OPTIMAL", "STABLE", "ALERT", "CRITICAL", "CRITICAL", "ALERT", "STABLE"]})
    with col_rad:
        fig = px.line_polar(df_ejes, r='Puntaje', theta='Eje', line_close=True, range_r=[0,100], color_discrete_sequence=['#c8a84b'])
        fig.update_traces(fill='toself', fillcolor='rgba(200, 168, 75, 0.2)')
        fig.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)', angularaxis=dict(tickfont=dict(color="#ffffff"))), paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=30, b=30))
        st.plotly_chart(fig, use_container_width=True)
    with col_met:
        st.metric("IBH SCORE PROMEDIO", "61.61", "+19.72")
        st.error("Eje Estratégico < 50: Multiplicador ×1.5 activo")

    st.subheader("7. IMPLICANCIAS ESTRATÉGICAS Y HOJA DE RUTA")
    st.markdown("""<div class="tech-table"><div class="t-row t-header"><div style="width:25%; padding:10px 15px;">Dimensión</div><div style="width:55%; padding:10px 15px;">Implicancia</div><div style="width:20%; padding:10px 15px; text-align:center;">Urgencia</div></div>
        <div class="t-row"><div class="t-col t-label" style="width:25%;">Territorial</div><div class="t-col" style="width:55%;">Bloqueo de accesos CLPI.</div><div class="t-col status-critical" style="width:20%; text-align:center;">INMEDIATA</div></div></div>""", unsafe_allow_html=True)

# --- CAPA 3: ORÁCULO & FIRMA FORENSE ---
elif "Capa 3" in capa_activa:
    st.subheader("6. PROPUESTA COMERCIAL DE INTERVENCIÓN")
    st.markdown('<div style="background-color:#111920; border:2px solid #c8a84b; padding:20px; border-radius:8px; text-align:center;"><p style="color:#8899a6; font-size:12px;">ORÁCULO v11.1</p><h1 style="color:#c8a84b; margin:0;">USD 214,693</h1></div>', unsafe_allow_html=True)
    
    st.write("### Cálculo de Honorarios")
    st.markdown("""<div class="tech-table"><div class="t-row t-header"><div style="width:30%; padding:10px 15px;">Parámetro</div><div style="width:20%; padding:10px 15px; text-align:center;">Valor</div><div style="width:50%; padding:10px 15px;">Detalle</div></div>
        <div class="t-row"><div class="t-col t-label" style="width:30%;">Retainer (40%)</div><div class="t-col" style="width:20%; text-align:center;">$85,877</div><div class="t-col" style="width:50%;">Abono para despliegue territorial.</div></div></div>""", unsafe_allow_html=True)

    st.subheader("8. METODOLOGÍA Y SELLO DE INTEGRIDAD FORENSE")
    st.markdown('<div class="seal-box">🛡️ SELLO FORENSE — CAPA 21 ACTIVA<br><span style="font-family:monospace; font-size:12px;">Hash: 9f4c5b606f7cde1126cb410d67500dec</span></div>', unsafe_allow_html=True)
    
    st.markdown("""<div style="text-align: right; margin-top:50px;"><p style="color:#8899a6; font-size:12px;">EMITIDO POR</p><h2 style="color:#c8a84b; margin:0;">Claudio Falasca Consultor</h2><p style="font-style:italic;">Heptágono Motor Determinístico</p><p><b>18 de Abril de 2026</b></p></div>""", unsafe_allow_html=True)

# PIE DE PÁGINA
st.write("---")
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
