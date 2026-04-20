import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide")

# 2. CSS MASTER CORE (Optimización de Contraste)
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    /* Forzar visibilidad de textos de Plotly que Streamlit a veces opaca */
    .js-plotly-plot .plotly .legendtext { fill: #ffffff !important; font-size: 14px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("Consola de Mando: Análisis de Supervivencia")

# --- GRÁFICO DE COX CON ALTA VISIBILIDAD ---
st.subheader("Curva de Supervivencia Cox — Referencias de Alto Contraste")

meses = list(range(0, 37, 3))
prob_base = [100, 92, 80, 65, 45, 30, 20, 15, 10, 5, 2, 1, 0]
prob_inter = [100, 95, 90, 88, 85, 84, 83, 82, 82, 81, 81, 80, 80]

fig_cox = go.Figure()

# ESCENARIO CRÍTICO (Rojo Brillante)
fig_cox.add_trace(go.Scatter(
    x=meses, y=prob_base, 
    name='⚠️ ESCENARIO SIN INTERVENCIÓN', 
    line=dict(color='#FF3131', width=4, dash='dot'),
    mode='lines+markers',
    marker=dict(size=8)
))

# ESCENARIO SF (Celeste Neón)
fig_cox.add_trace(go.Scatter(
    x=meses, y=prob_inter, 
    name='💎 PROYECCIÓN SUSANA FIGUEROA', 
    line=dict(color='#00FFFF', width=5),
    mode='lines+markers',
    marker=dict(size=10, symbol='diamond')
))

# ANOTACIONES DE REFERENCIA AL FINAL DE LA CURVA (Para lectura inmediata)
fig_cox.add_annotation(x=36, y=0, text="FALLO TOTAL", showarrow=True, arrowhead=2, bgcolor="#FF3131", font=dict(color="white"))
fig_cox.add_annotation(x=36, y=80, text="ÉXITO SF", showarrow=True, arrowhead=2, bgcolor="#00FFFF", font=dict(color="black"))

fig_cox.update_layout(
    xaxis=dict(
        title="TIEMPO (MESES)", 
        color="#c8a84b", 
        gridcolor="rgba(200, 168, 75, 0.1)",
        tickfont=dict(color="#ffffff", size=12)
    ),
    yaxis=dict(
        title="PROBABILIDAD DE CONTINUIDAD (%)", 
        color="#c8a84b", 
        gridcolor="rgba(200, 168, 75, 0.1)",
        tickfont=dict(color="#ffffff", size=12)
    ),
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    height=500,
    # Leyenda con fondo para máxima visibilidad
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.1,
        xanchor="center",
        x=0.5,
        bgcolor="rgba(255, 255, 255, 0.1)",
        bordercolor="#c8a84b",
        borderwidth=1,
        font=dict(color="#ffffff", size=14)
    )
)

st.plotly_chart(fig_cox, use_container_width=True)

# PIE DE PÁGINA
st.write("---")
st.caption('Sello Forense Digital - Contraste Validado para Operación Nocturna/Oscura')
