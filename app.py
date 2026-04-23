import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import hashlib, json
from fpdf import FPDF
from duckduckgo_search import DDGS

# =========================================================
# IDENTIDAD INMUTABLE
# =========================================================
ID_SOBERANA = "Claudio Falasca Consultor"
SISTEMA = "COPILOTO MINERO v12.2"

EJES_OFICIALES = [
    "Político-Institucional","Socio-Territorial","Económico-Financiero",
    "Técnico-Minero","Ambiental-Ecosistémico","Hídrico-Soberano","Comunicacional-Estratégico"
]

st.set_page_config(page_title=SISTEMA, layout="wide")

# =========================================================
# ESTILO MIDNIGHT GOLD
# =========================================================
st.markdown("""
<style>
.stApp { background:#05070a; color:#e5e7eb }
[data-testid="stSidebar"] { background:#0e1117; border-right:1px solid #D4AF37 }
.stMetric { background:#0e1117; border-bottom:2px solid #D4AF37; padding:10px }
.hash-footer { color:#6b7280; font-family:monospace; text-align:center; font-size:11px }
</style>
""", unsafe_allow_html=True)

# =========================================================
# OSINT REAL (solo alertas)
# =========================================================
def ejecutar_osint(proyecto, territorio):
    alertas = []
    try:
        with DDGS() as ddgs:
            query = f"conflicto minería {proyecto} {territorio}"
            results = list(ddgs.text(query, max_results=5))
            for r in results:
                alertas.append(r["title"])
    except:
        pass
    return alertas

# =========================================================
# FRiction INDEX
# =========================================================
def calcular_friction(icr, alertas):
    return min(100, icr + len(alertas)*3)

# =========================================================
# PDF REAL
# =========================================================
class PDF(FPDF):
    def header(self):
        self.set_font("Arial","B",12)
        self.cell(0,10,ID_SOBERANA,0,1,"C")

def generar_pdf(payload, firma):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    for k,v in payload.items():
        pdf.multi_cell(0,8,f"{k}: {v}")

    pdf.ln(10)
    pdf.multi_cell(0,8,f"FIRMA MD5: {firma}")

    return pdf.output(dest='S').encode('latin-1')

# =========================================================
# SIDEBAR — CABINA CONTROL
# =========================================================
st.sidebar.header("Cabina de Control")

proyecto = st.sidebar.text_input("Proyecto", "Josemaría")
territorio = st.sidebar.text_input("Territorio", "Argentina")
roi = st.sidebar.slider("ROI proyectado (%)",0,60,25)

st.sidebar.divider()
st.sidebar.subheader("Auditoría Heptágono")

scores = {}
for eje in EJES_OFICIALES:
    scores[eje] = st.sidebar.slider(eje,0,100,70)

ejecutar = st.sidebar.button("EJECUTAR ANALISIS")

# =========================================================
# PANTALLA INICIAL
# =========================================================
st.title(ID_SOBERANA)
st.caption("Terminal de Inteligencia Territorial")

if not ejecutar:
    st.info("Configure el caso en la cabina lateral y presione EJECUTAR.")
    st.stop()

# =========================================================
# EJECUCIÓN
# =========================================================
with st.spinner("Ejecutando OSINT real..."):
    alertas = ejecutar_osint(proyecto, territorio)

icr = 100 - scores["Socio-Territorial"]
friction = calcular_friction(icr, alertas)

# =========================================================
# GUARDIA MLC (bloqueo real)
# =========================================================
if icr > 70 and roi > 30:
    st.error("🚫 BLOQUEO ÉTICO ACTIVADO")
    st.stop()

# =========================================================
# LAYOUT 3 COLUMNAS
# =========================================================
col1,col2,col3 = st.columns([2,1,1])

# Radar
with col1:
    fig = go.Figure(go.Scatterpolar(
        r=list(scores.values()),
        theta=EJES_OFICIALES,
        fill='toself',
        line_color='#D4AF37'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True,range=[0,100])),
                      paper_bgcolor="rgba(0,0,0,0)",font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# Métricas
with col2:
    st.metric("ICR", f"{icr}%")
    st.metric("Friction Index", f"{friction}%")
    st.metric("ROI", f"{roi}%")

# Alertas OSINT
with col3:
    st.subheader("Alertas OSINT")
    for a in alertas:
        st.warning(a)

# =========================================================
# PAYLOAD FORENSE COMPLETO
# =========================================================
payload = {
    "consultor": ID_SOBERANA,
    "proyecto": proyecto,
    "territorio": territorio,
    "roi": roi,
    "icr": icr,
    "friction_index": friction,
    "scores": scores,
    "alertas_osint": alertas
}

firma = hashlib.md5(json.dumps(payload, sort_keys=True).encode()).hexdigest()

# =========================================================
# PDF + DESCARGA
# =========================================================
st.divider()
if st.button("DESPACHAR REPORTE PDF"):
    pdf_bytes = generar_pdf(payload, firma)
    st.download_button("Descargar Reporte",
        data=pdf_bytes,
        file_name=f"Reporte_{firma[:8]}.pdf")

st.markdown(f"<div class='hash-footer'>Firma Forense MD5: {firma}</div>",
            unsafe_allow_html=True)
