# =========================================================
# COPILOTO MINERO — HEPTÁGONO v12.6 FINAL
# Claudio Falasca Consultor
# Deploy Ready para Streamlit Cloud
# =========================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import hashlib, json
from duckduckgo_search import DDGS
from fpdf import FPDF

# =========================================================
# CONFIGURACIÓN GLOBAL
# =========================================================
st.set_page_config(page_title="Copiloto Minero", layout="wide")

st.markdown("""
<style>
.stApp {background-color:#0a0e14;color:white}
.stMetric {border:1px solid #D4AF37;padding:10px;border-radius:8px;background:#161b22}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE (CLAVE PARA QUE NO SE ROMPA EL DASHBOARD)
# =========================================================
if "analisis_ejecutado" not in st.session_state:
    st.session_state.analisis_ejecutado = False
    st.session_state.payload = None
    st.session_state.firma = None

# =========================================================
# BASE DE PROYECTOS (DATOS REALES DE EJEMPLO)
# =========================================================
CARTERA = {
    "Josemaría": {"roi":22,"icr_base":45,"opex":150,"prov":"San Juan"},
    "Veladero": {"roi":18,"icr_base":30,"opex":200,"prov":"San Juan"},
    "Peñas Negras": {"roi":35,"icr_base":85,"opex":90,"prov":"Catamarca"},
    "Taca Taca": {"roi":28,"icr_base":50,"opex":180,"prov":"Salta"},
    "Huarpe SRL": {"roi":15,"icr_base":15,"opex":50,"prov":"Multi"}
}

EJES = [
    "Político-Institucional","Socio-Territorial","Económico-Financiero",
    "Técnico-Minero","Ambiental-Ecosistémico","Hídrico-Soberano","Comunicacional-Estratégico"
]

# =========================================================
# MOTOR OSINT REAL
# =========================================================
def ejecutar_osint(proyecto):
    noticias=[]
    try:
        with DDGS() as ddgs:
            resultados = ddgs.text(f"conflicto mineria {proyecto}", max_results=5)
            for r in resultados:
                noticias.append(r["title"])
    except:
        noticias.append("No se pudieron obtener noticias OSINT.")
    return noticias

# =========================================================
# GENERADOR PDF REAL (C22)
# =========================================================
class PDF(FPDF):
    def header(self):
        self.set_font("Arial","B",12)
        self.cell(0,10,"Claudio Falasca Consultor — Executive Summary",0,1,"C")

def generar_pdf(payload,firma):
    pdf=PDF()
    pdf.add_page()
    pdf.set_font("Arial",size=11)
    pdf.multi_cell(0,8,json.dumps(payload,indent=2))
    pdf.ln(5)
    pdf.cell(0,10,f"Firma MD5: {firma}")
    return pdf.output(dest="S").encode("latin-1")

# =========================================================
# SIDEBAR — CABINA DE CONTROL
# =========================================================
st.title("🏛️ Copiloto Minero — Heptágono")

with st.sidebar:
    st.header("Configuración del Caso")

    proyecto=st.selectbox("Proyecto", list(CARTERA.keys()))
    roi=st.slider("ROI esperado (%)",0,60,CARTERA[proyecto]["roi"])

    st.divider()
    st.subheader("Auditoría de Ejes")

    scores={}
    for eje in EJES:
        scores[eje]=st.slider(eje,0,100,70)

    if st.button("🚀 EJECUTAR ANÁLISIS"):
        noticias=ejecutar_osint(proyecto)
        icr=100-scores["Socio-Territorial"]

        # Guardia ética MLC
        if icr>70 and roi>30:
            st.error("🚫 BLOQUEO MLC — Riesgo reputacional alto")
            st.stop()

        avg=sum(scores.values())/7
        impacto_ebitda=(icr/100)*CARTERA[proyecto]["opex"]*0.2
        roi_ajustado=roi*(avg/100)

        payload={
            "proyecto":proyecto,
            "scores":scores,
            "icr":icr,
            "roi_original":roi,
            "roi_ajustado":roi_ajustado,
            "impacto_ebitda_musd":impacto_ebitda,
            "alertas_osint":noticias
        }

        firma=hashlib.md5(json.dumps(payload,sort_keys=True).encode()).hexdigest()

        st.session_state.analisis_ejecutado=True
        st.session_state.payload=payload
        st.session_state.firma=firma

# =========================================================
# EVITA DASHBOARD VACÍO
# =========================================================
if not st.session_state.analisis_ejecutado:
    st.info("Configure el caso en la barra lateral y presione EJECUTAR ANÁLISIS.")
    st.stop()

payload=st.session_state.payload
firma=st.session_state.firma
scores=payload["scores"]

# =========================================================
# DASHBOARD PRINCIPAL
# =========================================================
col1,col2=st.columns([2,1])

# Radar Heptágono
with col1:
    st.subheader("Radar Estratégico")
    fig=go.Figure(go.Scatterpolar(
        r=list(scores.values()),
        theta=list(scores.keys()),
        fill="toself",
        line_color="#D4AF37"
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0,100])))
    st.plotly_chart(fig,use_container_width=True)

# Métricas ejecutivas
with col2:
    st.subheader("Indicadores Clave")
    st.metric("ICR",f"{payload['icr']}%")
    st.metric("ROI Ajustado",f"{payload['roi_ajustado']:.1f}%")
    st.metric("Impacto EBITDA",f"USD {payload['impacto_ebitda_musd']:.1f} M")

# Tabla de auditoría
st.subheader("Tabla de Auditoría de Ejes")
df=pd.DataFrame({"Eje":scores.keys(),"Score":scores.values()})
st.table(df)

# Alertas OSINT
st.subheader("Alertas OSINT")
for n in payload["alertas_osint"]:
    st.warning(n)

# PDF descargable
if st.button("📄 Generar PDF Ejecutivo"):
    pdf_bytes=generar_pdf(payload,firma)
    st.download_button("Descargar Reporte",pdf_bytes,file_name="reporte_heptagono.pdf")

st.caption(f"Sello Forense MD5: {firma}")
