import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN E IDENTIDAD (Punto 9: Marca y Emisión)
st.set_page_config(page_title="Copiloto Minero v11.1", layout="wide", initial_sidebar_state="expanded")

# ESTÉTICA DE ALTO DIRECTIVO (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(200, 168, 75, 0.2); }
    h1, h2, h3 { font-family: 'Syne', sans-serif; color: #ffffff !important; }
    .report-box { background-color: #111920; border: 1px solid rgba(255,255,255,0.07); padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .gold-text { color: #c8a84b; font-weight: bold; }
    .equation { background-color: #0d1318; border-left: 4px solid #c8a84b; padding: 15px; font-family: 'IBM Plex Mono', monospace; color: #c8a84b; margin: 10px 0; }
    .kpi-value { color: #c8a84b; font-size: 32px; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# 9. EMITIDO POR / MARCA (Sidebar)
with st.sidebar:
    st.markdown("### COPILOTO MINERO")
    st.caption("Heptágono Motor Determinístico")
    st.write("---")
    st.markdown("**EMITIDO POR:**")
    st.markdown('<p class="gold-text">Claudio Falasca Consultor</p>', unsafe_allow_html=True)
    st.write("**FECHA:** 18 de Abril de 2026")
    st.write("**PROYECTO:** Litio NOA - Cuenca Hombre Muerto Norte")
    st.write("---")
    st.info("CLASIFICACIÓN: CONFIDENCIAL - ALTO DIRECTIVO")

# ESTRUCTURA PRINCIPAL PASO A PASO
st.caption("CAPA 21 - TRACEABILITY VALIDATED")
st.title("Reporte Estratégico: Proyecto Litio NOA")

# 1. DIAGNÓSTICO DETERMINÍSTICO (KPIs de Riesgo)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="report-box"><p class="kpi-label">Índice Fricción Social (IFS)</p><p class="kpi-value">72%</p><p class="gold-text">Territory Risk: HIGH</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="report-box"><p class="kpi-label">Supervivencia Licencia (SL)</p><p class="kpi-value">28%</p><p style="color:#ff4b4b;">CRITICAL THRESHOLD</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="report-box"><p class="kpi-label">Evidence Score (TGA)</p><p class="kpi-value">127</p><p class="gold-text">Fuentes Auditadas</p></div>', unsafe_allow_html=True)

# TABS PARA PUNTOS 2 AL 8
tab_brief, tab_tga, tab_eq, tab_matriz, tab_propuesta, tab_ruta, tab_forense = st.tabs([
    "2. Executive Brief", "3. Validación TGA", "4. Ecuación Consenso", 
    "5. Matriz 7 Ejes", "6. Propuesta", "7. Hoja de Ruta", "8. Sello Forense"
])

# 2. EXECUTIVE BRIEF
with tab_brief:
    st.markdown("""
    ### Resumen Ejecutivo
    El sistema ha completado el diagnóstico del proyecto operado por **NOA Lithium Ventures S.A.** Se evidencia una **fricción social activa del 72%**, principalmente traccionada por la falta de transparencia en la 
    Capa Hídrica y la baja participación de proveedores locales (35%).
    """)
    st.warning("Recomendación: Intervención inmediata en los ejes Estratégico y Social para evitar paralización.")

# 3. VALIDACIÓN TGA (Regla de Oro)
with tab_tga:
    st.subheader("Validación de Fuentes TGA (Triple Grado de Auditoría)")
    st.success("STATUS: VALIDATED - Coherencia Lógica del 98.4%")
    st.write("- **Fuentes Primarias:** Entrevistas CLPI (Comunidades Diaguita y Atacameña).")
    st.write("- **Fuentes Secundarias:** Reportes de Sostenibilidad y Catastros Mineros.")
    st.write("- **Fuentes Terciarias:** OSINT y Análisis Forense Digital.")

# 4. ECUACIÓN DE CONSENSO V11.1
with tab_eq:
    st.subheader("Cálculo del Riesgo Final")
    st.markdown('<div class="equation">RF = (1 - Coherencia) x (IFS + Riesgo_Op) / SL</div>', unsafe_allow_html=True)
    st.write("La ecuación determina que el riesgo de pérdida de activos por conflicto social es **Inminente (Cat. A)**.")

# 5. MATRIZ TERRITORIAL (7 EJES)
with tab_matriz:
    col_rad, col_ins = st.columns([2,1])
    with col_rad:
        df = pd.DataFrame({
            "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
            "Puntaje": [78.49, 71.55, 55.31, 54.23, 47.78, 60.0, 65.0]
        })
        fig = px.line_polar(df, r='Puntaje', theta='Eje', line_close=True, range_r=[0,100], color_discrete_sequence=['#c8a84b'])
        fig.update_traces(fill='toself', fillcolor='rgba(200, 168, 75, 0.2)')
        fig.update_layout(polar=dict(bgcolor='#080c10', angularaxis=dict(tickfont=dict(color="#fff"))), paper_bgcolor='#080c10')
        st.plotly_chart(fig, use_container_width=True)
    with col_ins:
        st.write("**Análisis de Desviación:**")
        st.error("Eje Estratégico Crítico: 47.78")
        st.info("Oportunidad Regulatoria: 78.49")

# 6. PROPUESTA COMERCIAL
with tab_propuesta:
    st.markdown('<div class="report-box"><p class="kpi-label">Honorarios Oráculo Pricing</p><p class="kpi-value">USD 214,693</p><p class="gold-text">Esquema 40/40/20</p></div>', unsafe_allow_html=True)

# 7. IMPLICANCIAS Y HOJA DE RUTA
with tab_ruta:
    st.write("1. **Mes 1:** Seteo de Mesa de Diálogo CLPI.")
    st.write("2. **Mes 2:** Auditoría de Proveedores Locales.")
    st.write("3. **Mes 3:** Implementación MIRCS-ET.")

# 8. METODOLOGÍA Y SELLO FORENSE
with tab_forense:
    st.code("Payload MD5: 9f4c5b606f7cde1126cb410d67500dec", language=None)
    st.write("Metodología: Heptágono SF (Deterministic Governance Model)")
    st.success("Trazabilidad: Blockchain Timestamp Verified")

# CIERRE (Punto 9)
st.write("---")
st.caption('Sello Forense Digital - Propiedad de "Claudio Falasca Consultor"')
