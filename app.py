import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE INTERFAZ DE ALTO NIVEL
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. CEREBRO VISUAL (CSS Personalizado - Estilo Master Core)
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    
    /* Contenedor de la Tabla de Identidad */
    .identity-table {
        background-color: #111920;
        border: 1px solid rgba(200, 168, 75, 0.3);
        border-radius: 8px;
        padding: 0px;
        margin-bottom: 25px;
    }
    .id-row {
        display: flex;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .id-label {
        background-color: rgba(200, 168, 75, 0.05);
        color: #c8a84b;
        padding: 10px 15px;
        width: 35%;
        font-weight: 600;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .id-value {
        padding: 10px 15px;
        width: 65%;
        font-size: 14px;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (SIDEBAR)
with st.sidebar:
    st.markdown("### COPILOTO MINERO")
    st.caption("Heptágono Motor Determinístico")
    st.write("---")
    st.markdown("**OPERADOR:**")
    st.markdown('<p style="color:#c8a84b; font-weight:bold;">Claudio Falasca Consultor</p>', unsafe_allow_html=True)
    st.write("---")
    st.success("SISTEMA ONLINE v11.1")

# 4. CUERPO PRINCIPAL
st.caption("CONSULTA DE OPERACIÓN ACTIVA")
st.title("Panel de Control: Litio NOA")

# --- PUNTO 1: TABLA DE IDENTIDAD (VENTANA DE DATOS) ---
st.markdown("""
    <div class="identity-table">
        <div class="id-row">
            <div class="id-label">Empresa Objetivo</div>
            <div class="id-value">NOA Lithium Ventures S.A.</div>
        </div>
        <div class="id-row">
            <div class="id-label">Región / Provincia</div>
            <div class="id-value">Argentina / NOA / Catamarca</div>
        </div>
        <div class="id-row">
            <div class="id-label">Cuenca / Cluster</div>
            <div class="id-value">Hombre Muerto Norte</div>
        </div>
        <div class="id-row">
            <div class="id-label">Perfil Operador</div>
            <div class="id-value">S2-Mid-Tier</div>
        </div>
        <div class="id-row">
            <div class="id-label">Fuentes TGA</div>
            <div class="id-value">127 fuentes auditadas (VALIDADA)</div>
        </div>
        <div class="id-row">
            <div class="id-label">Fecha de Emisión</div>
            <div class="id-value">18 de Abril de 2026</div>
        </div>
        <div class="id-row" style="border-bottom:none;">
            <div class="id-label">Clasificación</div>
            <div class="id-value" style="color:#ff4b4b; font-weight:bold;">CONFIDENCIAL-ALTO DIRECTIVO</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 5. PREVISUALIZACIÓN DE GRÁFICOS (PARA SEGUIR CONSTRUYENDO)
col_radar, col_insights = st.columns([2, 1])

with col_radar:
    st.write("### Matriz Heptágono")
    # Gráfico de radar simplificado (Referencia)
    df = pd.DataFrame({
        "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
        "Puntaje": [78, 71, 55, 54, 47, 60, 65]
    })
    fig = px.line_polar(df, r='Puntaje', theta='Eje', line_close=True, range_r=[0, 100], color_discrete_sequence=['#c8a84b'])
    fig.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col_insights:
    st.write("### Estado de Capas")
    st.info("Capa 1: Infraestructura (OK)")
    st.info("Capa 2: Diagnóstico (OK)")
    st.info("Capa 3: Pricing (STANDBY)")

# 6. CIERRE
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
