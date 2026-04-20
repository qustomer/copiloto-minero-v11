import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# 2. ESTILOS MASTER CORE
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
    .t-label { background-color: rgba(200, 168, 75, 0.08); color: #c8a84b !important; font-weight: 600; width: 30%; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("### DATA LAKE v6.1")
    capa_activa = st.radio("Capas:", ["Capa 1: Infra", "Capa 2: Diagnóstico & Hoja de Ruta", "Capa 3: Oráculo"], index=1)
    st.write("---")
    st.markdown('<p style="color:#c8a84b; font-weight:bold;">Claudio Falasca Consultor</p>', unsafe_allow_html=True)

# 4. CUERPO PRINCIPAL
st.caption("CONSULTA DE OPERACIÓN ACTIVA")
st.title("Copiloto Minero v11.1")

if "Capa 2" in capa_activa:
    # --- 1. PROBABILIDAD DE SUPERVIVENCIA (GRÁFICO X e Y) ---
    st.subheader("4.1 Curva de Supervivencia Cox — Licencia Social")
    
    # Simulación de datos de supervivencia a 36 meses
    meses = list(range(0, 37, 3))
    prob_base = [100, 92, 80, 65, 45, 30, 20, 15, 10, 5, 2, 1, 0]
    prob_intervencion = [100, 95, 90, 88, 85, 84, 83, 82, 82, 81, 81, 80, 80]
    
    fig_cox = go.Figure()
    fig_cox.add_trace(go.Scatter(x=meses, y=prob_base, name='Sin Intervención (Riesgo)', line=dict(color='#ff4b4b', width=3, dash='dash')))
    fig_cox.add_trace(go.Scatter(x=meses, y=prob_intervencion, name='Con Intervención SF', line=dict(color='#2dd4bf', width=4)))
    
    fig_cox.update_layout(
        xaxis_title="Tiempo (Meses)", yaxis_title="Probabilidad de Supervivencia (%)",
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#ffffff"), margin=dict(t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_cox, use_container_width=True)

    # --- 2. CRONOGRAMA DE INTERVENCIÓN (CUADRO DE COLUMNAS) ---
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
                <div class="t-col" style="width:15%; font-weight:bold; color:#c8a84b;">Seteo</div>
                <div class="t-col" style="width:20%;">Mes 1 (Días 1-30)</div>
                <div class="t-col" style="width:40%;">Apertura Mesa CLPI, Auditoría TGA Prov.</div>
                <div class="t-col" style="width:25%;">Mapa de Fricción Inicial</div>
            </div>
            <div class="t-row">
                <div class="t-col" style="width:15%; font-weight:bold; color:#c8a84b;">Acción</div>
                <div class="t-col" style="width:20%;">Mes 2 (Días 31-60)</div>
                <div class="t-col" style="width:40%;">Despliegue MIRCS-ET, Firma de Acuerdos.</div>
                <div class="t-col" style="width:25%;">Protocolo de Consenso</div>
            </div>
            <div class="t-row" style="border-bottom:none;">
                <div class="t-col" style="width:15%; font-weight:bold; color:#c8a84b;">Cierre</div>
                <div class="t-col" style="width:20%;">Mes 3 (Días 61-90)</div>
                <div class="t-col" style="width:40%;">Certificación de Licencia, Exit Strategy.</div>
                <div class="t-col" style="width:25%;">Sello Forense Capa 21</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Radar de Diagnóstico (Se mantiene para referencia)
    st.write("---")
    st.subheader("Matriz Territorial (IBH Score)")
    df_ejes = pd.DataFrame({"Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"], "Puntaje": [78, 71, 55, 54, 47, 60, 65]})
    fig_rad = px.line_polar(df_ejes, r='Puntaje', theta='Eje', line_close=True, range_r=[0,100], color_discrete_sequence=['#c8a84b'])
    fig_rad.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_rad, use_container_width=True)

# PIE DE PÁGINA
st.write("---")
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
