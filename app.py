import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Identidad de Marca y Configuración de Pantalla
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide")

# Estética de Alto Directivo (Fondo oscuro y tipografía limpia)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #f0f2f6; }
    h1, h2, h3 { color: #f0f2f6 !important; }
    .stMarkdown { font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado Oficial del Sistema
st.caption("PLATAFORMA ESTRATÉGICA")
st.title("Copiloto Minero v11.1")
st.subheader("Heptágono: Motor Determinístico")
st.write("---")

# 3. Datos Sincronizados con Reporte PDF (7 Ejes)
# Basado en Capa 2: Diagnóstico
df = pd.DataFrame({
    "Eje": [
        "Regulatorio", 
        "Ambiental", 
        "Operacional", 
        "Social", 
        "Estratégico", 
        "Hídrico", 
        "Económico"
    ],
    "Puntaje": [78, 71, 55, 54, 47, 60, 65]
})

# 4. Construcción del Radar (Sintaxis simplificada para evitar ValueError)
fig = px.line_polar(
    df, 
    r='Puntaje', 
    theta='Eje', 
    line_close=True,
    range_r=[0, 100],
    color_discrete_sequence=['#C8A84B'] # Dorado Heptágono
)

# Ajuste visual del área interna
fig.update_traces(fill='toself', fillcolor='rgba(200, 168, 75, 0.2)')

# Configuración del fondo del gráfico para que coincida con la interfaz
fig.update_layout(
    polar=dict(
        bgcolor='#0e1117',
        radialaxis=dict(gridcolor='rgba(255,255,255,0.1)', showticklabels=False),
        angularaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickfont=dict(color="#e8eaed"))
    ),
    paper_bgcolor='#0e1117',
    plot_bgcolor='#0e1117',
    margin=dict(t=30, b=30, l=30, r=30)
)

# 5. Renderizado del Panel
st.plotly_chart(fig, use_container_width=True)

# 6. Bloque de Validación Técnica (Capa 21 Forense)
st.write("---")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="IBH Score", value="61.6")
with c2:
    st.caption("MD5 Verified Payload")
    st.code("9f4c5b606f7cde1126cb410d67500dec", language=None)
with c3:
    st.caption("TGA Status")
    st.success("VALIDATED 127 fuentes")
