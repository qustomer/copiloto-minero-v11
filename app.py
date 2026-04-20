import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURACIÓN DE INTERFAZ
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. CEREBRO VISUAL (CSS MASTER CORE - Máximo Contraste y Purga de Marca)
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    
    /* Textos y Etiquetas */
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
    .t-label { background-color: rgba(200, 168, 75, 0.08); color: #c8a84b !important; font-weight: 600; width: 35%; }

    /* Forzar visibilidad de leyendas Plotly */
    .js-plotly-plot .plotly .legendtext { fill: #ffffff !important; font-size: 13px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (IDENTIDAD EXCLUSIVA)
with st.sidebar:
    st.markdown("### DATA LAKE v6.1")
    capa_activa = st.radio(
        "Navegación de Capas:",
        ["Capa 1: Estructura TGA", "Capa 2: Diagnóstico & Hoja de Ruta", "Capa 3: Oráculo Claudio Falasca"],
        index=1
    )
    st.write("---")
    st.markdown("**OPERADOR:**")
    st.markdown('<p style="color:#c8a84b; font-weight:bold; font-size:18px;">Claudio Falasca Consultor</p>', unsafe_allow_html=True)
    st.info(f"MODO: {capa_activa.split(':')[0]}")

# 4. CUERPO PRINCIPAL
st.caption("CONSULTA DE OPERACIÓN ACTIVA — MOTOR DETERMINÍSTICO CLAUDIO FALASCA")
st.title("Copiloto Minero v11.1")

# --- LÓGICA DE CAPAS ---

if "Capa 1" in capa_activa:
    st.subheader("1. Identidad & Validación TGA")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row"><div class="t-col t-label">Proyecto</div><div class="t-col">Hombre Muerto Norte</div></div>
            <div class="t-row"><div class="t-col t-label">Analista</div><div class="t-col">Claudio Falasca Consultor</div></div>
            <div class="t-row" style="border-bottom:none;"><div class="t-col t-label">Estado TGA</div><div class="t-col" style="color:#2dd4bf; font-weight:bold;">VALIDADO</div></div>
        </div>
    """, unsafe_allow_html=True)

elif "Capa 2" in capa_activa:
    # --- CURVA DE COX CON NUEVA IDENTIDAD Y ALTA VISIBILIDAD ---
    st.subheader("4.1 Curva de Supervivencia Cox — Licencia Social")
    
    meses = list(range(0, 37, 3))
    prob_base = [100, 92, 80, 65, 45, 30, 20, 15, 10, 5, 2, 1, 0]
    prob_inter = [100, 95, 90, 88, 85, 84, 83, 82, 82, 81, 81, 80, 80]
    
    fig_cox = go.Figure()

    # Escenario Crítico
    fig_cox.add_trace(go.Scatter(
        x=meses, y=prob_base, 
        name='⚠️ ESCENARIO SIN INTERVENCIÓN', 
        line=dict(color='#FF3131', width=3, dash='dot'),
        mode='lines+markers'
    ))

    # Escenario Claudio Falasca (Máximo Contraste)
    fig_cox.add_trace(go.Scatter(
        x=meses, y=prob_inter, 
        name='💎 PROYECCIÓN CLAUDIO FALASCA CONSULTOR', 
        line=dict(color='#00FFFF', width=5),
        mode='lines+markers',
        marker=dict(size=10, symbol='diamond')
    ))

    # Anotaciones de Referencia con Fondo para Legibilidad
    fig_cox.add_annotation(x=36, y=5, text="RIESGO DE CIERRE", showarrow=True, arrowhead=2, bgcolor="#FF3131", font=dict(color="white"))
    fig_cox.add_annotation(x=36, y=85, text="ACTIVO ESTABILIZADO", showarrow=True, arrowhead=2, bgcolor="#00FFFF", font=dict(color="black"))

    fig_cox.update_layout(
        xaxis=dict(title="MESES", color="#ffffff", gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(title="PROBABILIDAD (%)", color="#ffffff", gridcolor="rgba(255,255,255,0.05)", range=[-5, 110]),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        height=450,
        legend=dict(
            orientation="h", yanchor="bottom", y=1.05, xanchor="center", x=0.5,
            bgcolor="rgba(255, 255, 255, 0.1)", bordercolor="#c8a84b", borderwidth=1
        )
    )
    st.plotly_chart(fig_cox, use_container_width=True)

    # --- CRONOGRAMA DE INTERVENCIÓN ---
    st.subheader("7.1 Cronograma Orientativo de Intervención")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header">
                <div style="width:20%; padding:10px 15px;">Fase</div>
                <div style="width:55%; padding:10px 15px;">Hitos de Gestión Claudio Falasca</div>
                <div style="width:25%; padding:10px 15px;">Entregable Forense</div>
            </div>
            <div class="t-row">
                <div class="t-col" style="width:20%; font-weight:bold; color:#c8a84b;">MES 1</div>
                <div class="t-col" style="width:55%;">Auditoría TGA y Apertura de Mesa CLPI.</div>
                <div class="t-col" style="width:25%;">Mapa de Fricción</div>
            </div>
            <div class="t-row" style="border-bottom:none;">
                <div class="t-col" style="width:20%; font-weight:bold; color:#c8a84b;">MES 3</div>
                <div class="t-col" style="width:55%;">Estabilización de Licencia Social y Sello Capa 21.</div>
                <div class="t-col" style="width:25%;">Certificación Final</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif "Capa 3" in capa_activa:
    st.subheader("6. Propuesta Comercial & Oráculo")
    st.markdown('<div style="border:2px solid #c8a84b; padding:40px; text-align:center; border-radius:10px;">'
                '<p style="color:#8899a6;">ORÁCULO v11.1 — PROYECCIÓN FINANCIERA</p>'
                '<h1 style="color:#c8a84b; font-size:48px;">USD 214,693</h1>'
                '<p style="color:#2dd4bf; font-weight:bold;">VALIDADO POR CLAUDIO FALASCA CONSULTOR</p></div>', unsafe_allow_html=True)

# 6. CIERRE SELLO FORENSE
st.write("---")
st.
