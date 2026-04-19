import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Copiloto Minero - SF Consulting", layout="wide")

st.title("🚀 Copiloto Minero: Auditoría Estratégica")
st.subheader("Análisis de Sostenibilidad - Proyecto Cobre San Juan")

# Datos de simulación (Heptágono SF)
data = {
    "Eje": ["Gobernanza", "Licencia Social", "Ambiental", "Hídrico", "Legal", "Económico", "Comunitario"],
    "Puntaje": [85, 40, 75, 30, 90, 80, 55]
}
df = pd.DataFrame(data)

# Visualización del Radar
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
      r=df['Puntaje'],
      theta=df['Eje'],
      fill='toself',
      name='Estado Actual'
))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)

# Layout de columnas
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.error("⚠️ ALERTA: Fricción hídrica crítica en zona de glaciares.")
    st.warning("Próximo hito: Audiencia pública en 15 días.")
    st.info("Presupuesto proyectado: USD 38,500")

st.success("Sistema Heptágono SF v7.9.1 operativo.")
