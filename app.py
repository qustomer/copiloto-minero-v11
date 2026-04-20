import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE INTERFAZ DE ALTA FIDELIDAD
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. INYECCIÓN DEL "CEREBRO VISUAL" (CSS Personalizado)
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    h1, h2, h3 { font-family: 'Syne', sans-serif; color: #ffffff !important; }
    
    .kpi-card { background-color: #111920; border: 1px solid rgba(255,255,255,0.07); padding: 15px; border-radius: 8px; text-align: center; }
    .kpi-value { color: #c8a84b; font-size: 24px; font-weight: bold; }
    .kpi-label { color: #8899a6; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }

    .main-score-box { background: linear-gradient(145deg, #111920, #080c10); border: 2px solid #c8a84b; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(200, 168, 75, 0.1); }
    .main-score-value { color: #c8a84b; font-size: 56px; font-weight: 800; }
    
    .pricing-box { background: linear-gradient(145deg, #111920, #080c10); border: 2px solid #2dd4bf; padding: 25px; border-radius: 12px; text-align: center; }
    .pricing-value { color: #2dd4bf; font-size: 48px; font-weight: 800; }
    
    /* Estética de las pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent; border-radius: 4px 4px 0px 0px; gap: 1px; padding-top: 10px; padding-bottom: 10px; color: #8899a6; }
    .stTabs [aria-selected="true"] { color: #c8a84b !important; border-bottom: 2px solid #c8a84b !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (SIDEBAR)
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/50/c8a84b/radar.png", width=50)
    st.markdown("### DATA LAKE v6.1")
    st.markdown("---")
    st.write("**Capas Activas:**")
    st.checkbox("Capa 1: Infraestructura", value=True, disabled=True)
    st.checkbox("Capa 2: Diagnóstico", value=True, disabled=True)
    st.checkbox("Capa 3: Pricing Oráculo", value=True, disabled=True)
    st.markdown("---")
    st.success("Nodes: 111 | Edges: 234")
    st.info("TGA Status: VALIDATED")
    st.caption("MD5: 9f4c5b606f7cde1126cb410d67500dec")

# 4. ENCABEZADO Y KPIs SUPERIORES
st.caption("Huarpe SRL — PIRCYDL CATAMARCA")
st.title("Copiloto Minero v11.1")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1: st.markdown('<div class="kpi-card"><div class="kpi-label">Fricción Social</div><div class="kpi-value">72%</div></div>', unsafe_allow_html=True)
with kpi2: st.markdown('<div class="kpi-card"><div class="kpi-label">Riesgo Paralización</div><div class="kpi-value">Alto</div></div>', unsafe_allow_html=True)
with kpi3: st.markdown('<div class="kpi-card"><div class="kpi-label">Superposición Indígena</div><div class="kpi-value">65%</div></div>', unsafe_allow_html=True)
with kpi4: st.markdown('<div class="kpi-card"><div class="kpi-label">Conflicto Activo (Área)</div><div class="kpi-value" style="color:#ff4b4b;">90%</div></div>', unsafe_allow_html=True)

st.write("---")

# 5. ESTRUCTURA DE 3 CAPAS (TABS)
tab1, tab2, tab3 = st.tabs(["Capa 1: Infraestructura & Hallazgos", "Capa 2: Diagnóstico Heptágono", "Capa 3: Oráculo Pricing"])

# --- CAPA 1 ---
with tab1:
    st.subheader("Key Findings & Mapeo de Sujetos")
    colA, colB = st.columns(2)
    with colA:
        st.info("**Sujetos CLPI Identificados en Zona de Influencia:**\n\n1. **Diaguita Los Chucos** · Pte. Gabriel Chucos\n2. **Atacameña El Coypar II** · Pte. Rosa Mamani")
    with colB:
        st.warning("**Estado de Proveedores Locales:**\n\nRegistro de Proveedor Activo: **35%**\n\n*Requiere intervención inmediata para mitigar fricción económica local.*")

# --- CAPA 2 ---
with tab2:
    col_left, col_right = st.columns([2, 1])
    with col_left:
        df = pd.DataFrame({
            "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
            "Puntaje": [78.49, 71.55, 55.31, 54.23, 47.78, 60.0, 65.0]
        })
        fig = px.line_polar(df, r='Puntaje', theta='Eje', line_close=True, range_r=[0, 100], color_discrete_sequence=['#c8a84b'], text='Puntaje')
        fig.update_traces(fill='toself', fillcolor='rgba(200, 168, 75, 0.15)', textposition='top center')
        fig.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)', radialaxis=dict(showticklabels=False), angularaxis=dict(tickfont=dict(color="#ffffff", size=12))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=30, b=30, l=30, r=30))
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.markdown("""
            <div class="main-score-box">
                <div class="kpi-label">IBH Score Promedio</div>
                <div class="main-score-value">61.61</div>
                <div style="color:#2dd4bf; font-size:14px;">▲ +19.72 vs v6.0</div>
            </div>
        """, unsafe_allow_html=True)
        st.write("### Ranking & Insights")
        st.error("**Eje Débil:** Estratégico (47.78) - Nivel Crítico")
        st.success("**Eje Fuerte:** Regulatorio (78.49) - Oportunidad")

# --- CAPA 3 ---
with tab3:
    st.subheader("Modelo de Pricing 40/40/20")
    st.markdown("""
        <div class="pricing-box">
            <div class="kpi-label" style="color:#8899a6;">Presupuesto Base (Grand Total USD)</div>
            <div class="pricing-value">$214,693</div>
            <div style="color:#e8eaed; font-size:16px; margin-top:10px;">▼ -17,925 USD (-4.5% vs v6.0)</div>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.caption("Nota: El cálculo determinístico se ajusta dinámicamente según el nivel de riesgo de paralización y superposición territorial evidenciado en la Capa 1.")

# 6. SELLO FORENSE Y FIRMA
st.write("---")
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
