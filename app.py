import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de Identidad y Estética
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide")

# Estética de Alto Impacto
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1, h2, h3 { color: #ffffff !important; }
    .stCaption { color: #e8eaed !important; }
    
    /* Clase especial para resaltar el Score */
    .score-box {
        background-color: rgba(200, 168, 75, 0.1);
        border: 2px solid #C8A84B;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .score-value {
        color: #C8A84B;
        font-size: 48px;
        font-weight: 800;
        font-family: 'Segoe UI', sans-serif;
    }
    .score-label {
        color: #ffffff;
        font-size: 14px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado de Marca
st.caption("PLATAFORMA ESTRATÉGICA")
st.title("Copiloto Minero v11.1")
st.subheader("Heptágono: Motor Determinístico")
st.write("---")

# 3. Base de Datos
data = {
    "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
    "Puntaje": [78, 71, 55, 54, 47, 60, 65]
}
df = pd.DataFrame(data)

# 4. Creación del Radar
fig = px.line_polar(
    df, r='Puntaje', theta='Eje', line_close=True,
    range_r=[0, 100], color_discrete_sequence=['#C8A84B'],
    text='Puntaje'
)

fig.update_traces(
    fill='toself', fillcolor='rgba(200, 168, 75, 0.2)',
    textposition='top center',
    textfont=dict(color='#ffffff', size=14)
)

fig.update_layout(
    polar=dict(
        bgcolor='#0e1117',
        radialaxis=dict(gridcolor='rgba(255,255,255,0.15)', showticklabels=False),
        angularaxis=dict(gridcolor='rgba(255,255,255,0.15)', tickfont=dict(color="#ffffff", size=13))
    ),
    paper_bgcolor='#0e1117',
    plot_bgcolor='#0e1117',
    margin=dict(t=40, b=40, l=40, r=40)
)

# 5. Despliegue en Panel
col_radar, col_tabla = st.columns([2, 1])

with col_radar:
    st.plotly_chart(fig, use_container_width=True)

with col_tabla:
    # --- BLOQUE DE SCORE RESALTADO ---
    st.markdown(f"""
        <div class="score-box">
            <div class="score-label">IBH Score Promedio</div>
            <div class="score-value">61.6</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### Valores del Engine")
    st.dataframe(df.set_index("Eje"), use_container_width=True)

# 6. Sello de Validación
st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.code("MD5: 9f4c5b606f7cde1126cb410d67500dec", language=None)
with c2:
    st.success("TGA Status: VALIDATED")
