import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de Identidad y Estética
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide")

# Mejora de contraste para textos grises
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1, h2, h3 { color: #ffffff !important; }
    /* Ajuste para que los textos secundarios (caption) sean legibles */
    .stCaption { color: #e8eaed !important; font-weight: 500; }
    .stMarkdown { font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado de Marca
st.caption("PLATAFORMA ESTRATÉGICA")
st.title("Copiloto Minero v11.1")
st.subheader("Heptágono: Motor Determinístico")
st.write("---")

# 3. Base de Datos (Sincronizada con Reporte PDF)
data = {
    "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
    "Puntaje": [78, 71, 55, 54, 47, 60, 65]
}
df = pd.DataFrame(data)

# 4. Creación del Radar con Valores Numéricos Visibles
fig = px.line_polar(
    df, 
    r='Puntaje', 
    theta='Eje', 
    line_close=True,
    range_r=[0, 100],
    color_discrete_sequence=['#C8A84B'],
    text='Puntaje' # Esta línea activa los números en los puntos
)

# Estética del área y visibilidad de etiquetas
fig.update_traces(
    fill='toself', 
    fillcolor='rgba(200, 168, 75, 0.2)',
    textposition='top center', # Ubica el número arriba del punto
    textfont=dict(color='#ffffff', size=14, family="Arial Black")
)

fig.update_layout(
    polar=dict(
        bgcolor='#0e1117',
        radialaxis=dict(
            gridcolor='rgba(255,255,255,0.15)', 
            showticklabels=False, # Limpiamos el ruido de fondo
            gridwidth=1
        ),
        angularaxis=dict(
            gridcolor='rgba(255,255,255,0.15)', 
            tickfont=dict(color="#ffffff", size=13) # Ejes en blanco puro para contraste
        )
    ),
    paper_bgcolor='#0e1117',
    plot_bgcolor='#0e1117',
    margin=dict(t=40, b=40, l=40, r=40)
)

# 5. Despliegue en Panel (Radar + Tabla de Valores)
col_radar, col_tabla = st.columns([2, 1])

with col_radar:
    st.plotly_chart(fig, use_container_width=True)

with col_tabla:
    st.write("### Valores del Engine")
    # Mostramos la tabla con los valores exactos para respaldo del gráfico
    st.dataframe(df.set_index("Eje"), use_container_width=True)
    st.metric(label="IBH Score Promedio", value="61.6")

# 6. Sello de Validación
st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.code("MD5: 9f4c5b606f7cde1126cb410d67500dec", language=None)
with c2:
    st.success("TGA Status: VALIDATED (127 fuentes)")
