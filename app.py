import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURACIÓN DE INTERFAZ
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. CEREBRO VISUAL (Estilos Master Core)
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    .stMarkdown, p, span, label { color: #e8eaed !important; }
    .stCaption { color: #c8a84b !important; font-weight: 500; }
    h1, h2, h3 { color: #ffffff !important; font-family: 'Syne', sans-serif; }

    /* Tablas Técnicas */
    .tech-table {
        background-color: #111920;
        border: 1px solid rgba(200, 168, 75, 0.3);
        border-radius: 8px;
        margin-bottom: 25px;
        overflow: hidden;
    }
    .t-row { display: flex; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .t-header { background-color: rgba(200, 168, 75, 0.15); color: #c8a84b !important; font-weight: 800; text-transform: uppercase; font-size: 11px; }
    .t-col { padding: 12px 15px; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGACIÓN LATERAL
with st.sidebar:
    st.markdown("### DATA LAKE v6.1")
    capa_activa = st.radio("Capas de Análisis:", ["Capa 1: Estructura TGA", "Capa 2: Diagnóstico & Hoja de Ruta", "Capa 3: Oráculo Comercial"], index=1)
    st.write("---")
    st.markdown('<p style="color:#c8a84b; font-weight:bold;">Claudio Falasca Consultor</p>', unsafe_allow_html=True)

# 4. CUERPO PRINCIPAL
st.caption("CONSULTA DE OPERACIÓN ACTIVA")
st.title("Copiloto Minero v11.1")

if "Capa 2" in capa_activa:
    # --- 1. CURVA DE COX CON REFERENCIAS ---
    st.subheader("4.1 Curva de Supervivencia Cox — Licencia Social (Referenciada)")
    
    meses = list(range(0, 37, 3))
    prob_base = [100, 92, 80, 65, 45, 30, 20, 15, 10, 5, 2, 1, 0]
    prob_inter = [100, 95, 90, 88, 85, 84, 83, 82, 82, 81, 81, 80, 80]
    
    fig_cox = go.Figure()

    # Línea Roja: Sin Intervención
    fig_cox.add_trace(go.Scatter(
        x=meses, y=prob_base, 
        name='ESCENARIO BASE: Sin Intervención (Riesgo de Cierre)', 
        line=dict(color='#ff4b4b', width=3, dash='dash'),
        mode='lines+markers'
    ))

    # Línea Celeste/Aqua: Con Intervención
    fig_cox.add_trace(go.Scatter(
        x=meses, y=prob_inter, 
        name='PROYECCIÓN SF: Con Intervención Heptágono (Estabilización)', 
        line=dict(color='#2dd4bf', width=4),
        mode='lines+markers'
    ))
    
    fig_cox.update_layout(
        xaxis=dict(title="Meses de Operación", gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(title="Probabilidad de Continuidad (%)", gridcolor="rgba(255,255,255,0.05)", range=[0, 105]),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#ffffff"), height=400,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=12))
    )
    st.plotly_chart(fig_cox, use_container_width=True)

    # --- 2. CRONOGRAMA DE INTERVENCIÓN ---
    st.subheader("7.1 Cronograma Orientativo de Intervención")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:15%; padding:10px 15px;">Fase</div>
                <div style="width:20%; padding:10px 15px;">Periodo</div>
                <div style="width:40%; padding:10px 15px;">Hitos Clave</div>
                <div style="width:25%; padding:10px 15px;">Entregable Forense</div>
            </div>
            <div class="t-row">
                <div class="t-col" style="width:15%; font-weight:bold; color:#c8a84b;">FASE I: Seteo</div>
                <div class="t-col" style="width:20%;">Días 1 a 30</div>
                <div class="t-col" style="width:40%;">Auditoría TGA, Apertura Mesa Diálogo, Mapeo CLPI.</div>
                <div class="t-col" style="width:25%;">Dashboard Identidad</div>
            </div>
            <div class="t-row">
                <div class="t-col" style="width:15%; font-weight:bold; color:#c8a84b;">FASE II: Acción</div>
                <div class="t-col" style="width:20%;">Días 31 a 60</div>
                <div class="t-col" style="width:40%;">Implementación MIRCS-ET, Consenso de Territorio.</div>
                <div class="t-col" style="width:25%;">Protocolo de Mitigación</div>
            </div>
            <div class="t-row" style="border-bottom:none;">
                <div class="t-col" style="width:15%; font-weight:bold; color:#c8a84b;">FASE III: Cierre</div>
                <div class="t-col" style="width:20%;">Días 61 a 90</div>
                <div class="t-col" style="width:40%;">Certificación IBH > 75, Transferencia de activos.</div>
                <div class="t-col" style="width:25%;">Sello Forense Capa 21</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# PIE DE PÁGINA
st.write("---")
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
