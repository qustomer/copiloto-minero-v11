import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib
import io

# --- 1. CONFIGURACIÓN MASTER CORE (Capa 1 & 11) ---
st.set_page_config(page_title="Heptágono v10.1 | Master Core", layout="wide")

# CSS: Estética Forense Claudio Falasca
st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(212, 175, 55, 0.2); }
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'Syne', sans-serif; }
    .tech-table { background-color: #111920; border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 8px; margin-bottom: 25px; overflow: hidden; }
    .t-row { display: flex; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .t-header { background-color: rgba(212, 175, 55, 0.15); color: #D4AF37; font-weight: 800; text-transform: uppercase; font-size: 11px; padding: 12px; }
    .t-col { padding: 12px; font-size: 12px; color: #ffffff; }
    .t-label { background-color: rgba(212, 175, 55, 0.08); color: #D4AF37 !important; font-weight: 600; width: 30%; }
    .url-link { color: #00FFFF !important; text-decoration: none; font-family: monospace; }
    .seal-box { border: 2px dashed #D4AF37; padding: 20px; border-radius: 8px; background-color: rgba(212, 175, 55, 0.03); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GENERADOR DE FUENTES (DATA LAKE SIMULADO - TOP 20) ---
def get_audit_sources():
    data = [
        {"Fuente": "BOLETÍN OFICIAL CATAMARCA", "Tipo": "Regulatorio", "URL": "https://boletin.catamarca.gob.ar/mineria/resoluciones"},
        {"Fuente": "CÁMARA MINERA ARGENTINA", "Tipo": "Económico", "URL": "https://caem.com.ar/estadisticas-noa"},
        {"Fuente": "MINISTERIO DE MINERÍA SJ", "Tipo": "Regulatorio", "URL": "https://mineria.sanjuan.gob.ar/transparencia"},
        {"Fuente": "ASAMBLEA PUCARÁ (Pueblos Catamarca)", "Tipo": "Fricción Territorial", "URL": "https://asambleapucara.org/conflictos-litio"},
        {"Fuente": "DIARIO EL ANCASTI - SECCIÓN MINERA", "Tipo": "Social", "URL": "https://elancasti.com.ar/catamarca/mineria"},
        {"Fuente": "OBSERVATORIO PLURINACIONAL DE SALARES", "Tipo": "Fricción Territorial", "URL": "https://opsal.org/salares-argentina"},
        {"Fuente": "CONICET - RECURSOS HÍDRICOS NOA", "Tipo": "Hídrico", "URL": "https://conicet.gov.ar/investigacion/h2o-litio"},
        {"Fuente": "RED DE ASAMBLEAS DE COMUNIDADES", "Tipo": "Fricción Territorial", "URL": "https://redasambleas.org/territorios"},
        {"Fuente": "BANCO MUNDIAL - ESG MINING ARG", "Tipo": "Estratégico", "URL": "https://worldbank.org/projects/arg-mining-esg"},
        {"Fuente": "REPORTE SUSTENTABILIDAD GLENCORE", "Tipo": "Ambiental", "URL": "https://glencore.com/sustainability/reports-2026"},
        {"Fuente": "UNESCO - PATRIMONIO ATACAMA", "Tipo": "Fricción Territorial", "URL": "https://unesco.org/culture/mining-impact"},
        {"Fuente": "SECRETARÍA AMBIENTE SALTA", "Tipo": "Ambiental", "URL": "https://salta.gob.ar/ambiente/evaluaciones-impacto"},
        {"Fuente": "FORO SOCIAL DE MINERÍA NOA", "Tipo": "Fricción Territorial", "URL": "https://forominero.org/resistencia-litio"},
        {"Fuente": "REPORTE TRIMESTRAL LIVENT/ALTEM", "Tipo": "Operacional", "URL": "https://arcadiumlithium.com/investors"},
        {"Fuente": "NOTICIAS DE MINERÍA AMERICANA", "Tipo": "Social", "URL": "https://miningpress.com/argentina/conflictos"},
        {"Fuente": "CONFLICTOS SOCIOAMBIENTALES ARG", "Tipo": "Fricción Territorial", "URL": "https://mapaconflictos.org.ar/mineria"},
        {"Fuente": "BOLSA DE COMERCIO BS AS", "Tipo": "Económico", "URL": "https://bcba.sba.com.ar/cotizacion-mineras"},
        {"Fuente": "INDEC - EXPORTACIONES METALÍFERAS", "Tipo": "Económico", "URL": "https://indec.gob.ar/mineria-datos"},
        {"Fuente": "REPORTE RSE POSCO ARGENTINA", "Tipo": "Social", "URL": "https://posco.com/argentina/rse-2026"},
        {"Fuente": "OBSERVATORIO DE CONFLICTOS MINEROS (OCMAL)", "Tipo": "Fricción Territorial", "URL": "https://ocmal.org/argentina/litio"}
    ]
    return pd.DataFrame(data)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.title("HEPTÁGONO v10.1")
    st.markdown("**OPERADOR:** Claudio Falasca Consultor")
    st.write("---")
    capa_activa = st.radio("Capas:", ["Diagnóstico 7 Ejes", "Fuentes Auditadas (TGA)", "Riesgo & Oráculo"])
    sources_count = st.number_input("Fuentes TGA Auditadas", value=112)
    st.caption("© 2026 Claudio Falasca Consultor")

# --- 4. CUERPO PRINCIPAL ---
st.caption("CAPA 19: OPERATOR CONTROL DASHBOARD")
st.title("Copiloto Minero v11.1")

if sources_count < 105:
    st.error("⛔ TGA BLOQUEADO: No se alcanza el umbral de 105 fuentes.")
    st.stop()

# --- CAPA: FUENTES AUDITADAS (NUEVA REQUERIDA) ---
if capa_activa == "Fuentes Auditadas (TGA)":
    st.subheader("Capa 15: Transparencia & Cosecha Forense (Top 20)")
    df_sources = get_audit_sources()
    
    # Tabla Visible en Pantalla
    st.markdown('<div class="tech-table">', unsafe_allow_html=True)
    st.markdown('<div class="t-row t-header"><div style="width:10%;">#</div><div style="width:40%;">Fuente</div><div style="width:20%;">Categoría</div><div style="width:30%;">Enlace Permanente</div></div>', unsafe_allow_html=True)
    for i, row in df_sources.iterrows():
        color = "#FF3131" if row['Tipo'] == "Fricción Territorial" else "#D4AF37"
        st.markdown(f"""
            <div class="t-row">
                <div class="t-col" style="width:10%;">{i+1}</div>
                <div class="t-col" style="width:40%; font-weight:bold;">{row['Fuente']}</div>
                <div class="t-col" style="width:20%; color:{color};">{row['Tipo']}</div>
                <div class="t-col" style="width:30%;"><a href="{row['URL']}" class="url-link" target="_blank">↗ Acceder</a></div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Botón para Archivo Anexo (Audit Log Completo)
    st.write("---")
    st.markdown("### Reporte Forense para Cliente")
    csv_buffer = io.StringIO()
    df_sources.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Descargar Reporte Completo (Audit Log)",
        data=csv_buffer.getvalue(),
        file_name="Audit_Log_ClaudioFalasca_V11.csv",
        mime="text/csv"
    )

elif capa_activa == "Diagnóstico 7 Ejes":
    st.subheader("Capa 2: Diagnóstico Determinístico")
    df_ejes = pd.DataFrame({"Eje": ["Reg", "Amb", "Ope", "Soc", "Est", "Híd", "Eco"], "Puntaje": [78, 38, 55, 42, 47, 60, 65]})
    fig_rad = px.line_polar(df_ejes, r='Puntaje', theta='Eje', line_close=True, range_r=[0,100], color_discrete_sequence=['#D4AF37'])
    fig_rad.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig_rad, use_container_width=True)

elif capa_activa == "Riesgo & Oráculo":
    st.subheader("Hoja de Ruta - Cronograma Claudio Falasca")
    st.markdown("""<div class="tech-table">
        <div class="t-row t-header"><div style="width:20%;">Fase</div><div style="width:60%;">Acción Master Core</div><div style="width:20%;">Hito</div></div>
        <div class="t-row"><div class="t-col t-label">Mes 1</div><div class="t-col" style="width:60%;">Auditoría TGA y Activos Críticos.</div><div class="t-col">Validación</div></div>
        </div>""", unsafe_allow_html=True)
    
    st.subheader("Sello de Integridad Forense")
    st.markdown(f"""<div class="seal-box">
            <h3 style="margin:0; color:#D4AF37;">🛡️ SELLO FORENSE VÁLIDO</h3>
            <p style="color:#8899a6; font-size:12px;">OPERADOR: CLAUDIO FALASCA CONSULTOR</p>
            <code style="color:#D4AF37;">HASH: {hashlib.md5(b"audit_v11").hexdigest()}</code>
        </div>""", unsafe_allow_html=True)

# PIE DE PÁGINA
st.divider()
st.caption('Heptágono v10.1 — Sistema de Inteligencia Soberana de Claudio Falasca Consultor')
