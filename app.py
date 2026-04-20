import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE INTERFAZ DE ALTA FIDELIDAD
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. INYECCIÓN DEL "CEREBRO VISUAL" (CSS Personalizado)
st.markdown("""
    <style>
    /* Estética Huarpe v6 - Deep Night & Gold */
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    
    /* Tipografía y Encabezados */
    h1, h2, h3 { font-family: 'Syne', sans-serif; color: #ffffff !important; }
    
    /* Tarjetas de KPI Estilo Data Lake */
    .kpi-card {
        background-color: #111920;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    .kpi-value { color: #c8a84b; font-size: 24px; font-weight: bold; }
    .kpi-label { color: #8899a6; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }

    /* Score Principal Resaltado */
    .main-score-box {
        background: linear-gradient(145deg, #111920, #080c10);
        border: 2px solid #c8a84b;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(200, 168, 75, 0.1);
    }
    .main-score-value { color: #c8a84b; font-size: 56px; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (SIDEBAR) - ESTRUCTURA DATA LAKE
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/50/c8a84b/radar.png", width=50)
    st.markdown("### DATA LAKE v6.1")
    st.markdown("---")
    st.write("**Capas Activas:**")
    st.checkbox("Capa 1: Infraestructura", value=True)
    st.checkbox("Capa 2: Diagnóstico", value=True)
    st.checkbox("Capa 3: Pricing Oráculo", value=True)
    
    st.markdown("---")
    st.markdown("### PIPELINE STATUS")
    st.success("Nodes: 111 | Edges: 234")
    st.info("TGA Status: VALIDATED")
    
    st.markdown("---")
    st.caption("MD5: 9f4c5b606f7cde1126cb410d67500dec")

# 4. CUERPO PRINCIPAL - ESTRUCTURA DE KPIs (FILA SUPERIOR)
st.caption("Huarpe SRL — PIRCYDL CATAMARCA")
st.title("Copiloto Minero v11.1")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.markdown('<div class="kpi-card"><div class="kpi-label">Fricción Social</div><div class="kpi-value">72%</div></div>', unsafe_allow_html=True)
with kpi2:
    st.markdown('<div class="kpi-card"><div class="kpi-label">Riesgo Paralización</div><div class="kpi-value">High</div></div>', unsafe_allow_html=True)
with kpi3:
    st.markdown('<div class="kpi-card"><div class="kpi-label">Fuentes TGA</div><div class="kpi-value">127</div></div>', unsafe_allow_html=True)
with kpi4:
    st.markdown('<div class="kpi-card"><div class="kpi-label">Versión Engine</div><div class="kpi-value">v11.1</div></div>', unsafe_allow_html=True)

st.write("---")

# 5. LAYOUT CENTRAL (RADAR + SCORE)
col_left, col_right = st.columns([2, 1])

with col_left:
    # Datos de los 7 ejes
    df = pd.DataFrame({
        "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
        "Puntaje": [78, 71, 55, 54, 47, 60, 65]
    })
    
    fig = px.line_polar(
        df, r='Puntaje', theta='Eje', line_close=True,
        range_r=[0, 100], color_discrete_sequence=['#c8a84b'], text='Puntaje'
    )
    fig.update_traces(fill='toself', fillcolor='rgba(200, 168, 75, 0.15)', textposition='top center')
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(gridcolor='rgba(255,255,255,0.1)', showticklabels=False),
            angularaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickfont=dict(color="#ffffff", size=11))
        ),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=30, b=30, l=30, r=30)
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown(f"""
        <div class="main-score-box">
            <div class="kpi-label">IBH Score Promedio</div>
            <div class="main-score-value">61.6</div>
            <div style="color:#2dd4bf; font-size:14px;">▲ +19.72 vs v6.0</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### Insights del Motor")
    st.warning("**Eje Estratégico Crítico:** Puntuación por debajo de 50.")
    st.info("**Oportunidad Ambiental:** Coherencia alta en Capa 2.")
    
    with st.expander("Ver Tabla de Datos"):
        st.dataframe(df.set_index("Eje"), use_container_width=True)

st.write("---")
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
