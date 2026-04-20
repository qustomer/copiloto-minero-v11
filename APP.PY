import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SF Consulting - Auditoría", layout="wide")

st.title("📊 Heptágono SF: Panel de Control")
st.write("Estado de situación: Proyecto San Juan")

# Datos simplificados para asegurar el arranque
df = pd.DataFrame({
    "Eje": ["Gobernanza", "Social", "Ambiental", "Hídrico", "Legal", "Económico", "Comunitario"],
    "Puntaje": [85, 40, 75, 30, 90, 80, 55]
})

fig = px.line_polar(df, r='Puntaje', theta='Eje', line_close=True)
st.plotly_chart(fig)

st.success("Conexión con repositorio v11 exitosa.")
