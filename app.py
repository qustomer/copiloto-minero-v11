import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import hashlib
import json
from datetime import datetime
from fpdf import FPDF
from duckduckgo_search import DDGS

# =========================================================
# ESTADO PERSISTENTE
# =========================================================
if 'historial_casos' not in st.session_state:
    st.session_state.historial_casos = []

if 'pipeline_activo' not in st.session_state:
    st.session_state.pipeline_activo = None

# =========================================================
# IDENTIDAD
# =========================================================
ID_SOBERANA = "Claudio Falasca Consultor"
SISTEMA = "HEPTÁGONO Copiloto Minero v14.1"

# 7 EJES / 21 CAPAS
EJES_CAPAS = {
    "Político-Institucional": ["Marco Regulatorio","Estabilidad Jurídica","Permisos"],
    "Socio-Territorial": ["Licencia Social","Conflictos Activos","Derechos Indígenas"],
    "Económico-Financiero": ["ROI/EBITDA","Proveedores Locales","Costo Oportunidad"],
    "Técnico-Minero": ["Geología","Infraestructura","Logística"],
    "Ambiental-Ecosistémico": ["Biodiversidad","Glaciares","Pasivos"],
    "Hídrico-Soberano": ["Cuencas","Estrés Hídrico","Derecho Agua"],
    "Comunicacional": ["Percepción","Crisis","Stakeholders"]
}

st.set_page_config(page_title=SISTEMA, layout="wide")

# =========================================================
# CSS WAR ROOM
# =========================================================
st.markdown("""
<style>
.stApp { background:#080c10; color:#e0e0e0; }
.stMetric { background:#0d1318; border:1px solid #c8a84b; padding:10px; border-radius:6px; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# MOTORES BACKEND
# =========================================================
def motor_osint(query):
    try:
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=4))
    except:
        return []

def generar_hash(payload):
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

# ⭐⭐⭐ FUNCIÓN PDF CORREGIDA STREAMLIT ⭐⭐⭐
def generar_pdf(payload, hash_val):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,"Reporte C22 Heptagono",0,1)

    pdf.set_font("Arial","",12)
    pdf.cell(0,10,f"Proyecto: {payload['id']}",0,1)
    pdf.cell(0,10,f"Provincia: {payload['provincia']}",0,1)
    pdf.cell(0,10,f"IBH: {payload['ibh']:.2f}",0,1)
    pdf.cell(0,10,f"ICR: {payload['icr']:.2f}",0,1)
    pdf.cell(0,10,f"Friction Index: {payload['friction']:.2f}",0,1)
    pdf.multi_cell(0,10,f"Hash Forense: {hash_val}")

    # FIX STREAMLIT CLOUD
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    return pdf_bytes

# =========================================================
# SIDEBAR — CABINA CONTROL
# =========================================================
with st.sidebar:
    st.title("🏛️ HEPTÁGONO")
    st.subheader("Auditoría de Caso")

    with st.form("form"):
        id_caso = st.text_input("ID Proyecto", "PRJ-2026-X")
        provincia = st.selectbox("Provincia", ["San Juan","Catamarca","Salta","Jujuy","Santa Cruz"])
        roi_target = st.slider("ROI objetivo (%)", 0, 80, 25)

        st.divider()
        st.write("⚙️ Activación 21 capas")

        scores_temp = {}
        for eje, capas in EJES_CAPAS.items():
            for capa in capas:
                scores_temp[capa] = st.slider(capa,0,100,70)

        ejecutar = st.form_submit_button("🚀 EJECUTAR PIPELINE")

# =========================================================
# PIPELINE EJECUCIÓN
# =========================================================
if ejecutar:

    noticias = motor_osint(f"conflicto mineria {id_caso} {provincia}")

    icr = 100 - (sum([scores_temp[c] for c in EJES_CAPAS["Socio-Territorial"]]) / 3)
    ibh = sum(scores_temp.values()) / 21
    friction = icr * 0.6 + (100-ibh) * 0.4

    # GUARDIA MLC
    if icr > 70 and roi_target > 30:
        st.error("🚫 BLOQUEO ÉTICO MLC")
        st.stop()

    payload = {
        "id": id_caso,
        "provincia": provincia,
        "roi": roi_target,
        "scores": scores_temp,
        "icr": icr,
        "ibh": ibh,
        "friction": friction,
        "osint_hits": len(noticias)
    }

    hash_val = generar_hash(payload)

    st.session_state.pipeline_activo = payload
    st.session_state.historial_casos.append({"id":id_caso,"hash":hash_val,"ibh":ibh})

# =========================================================
# DASHBOARD
# =========================================================
if st.session_state.pipeline_activo:

    p = st.session_state.pipeline_activo
    hash_val = generar_hash(p)

    st.title("Centro de Mando Heptágono")

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("IBH", f"{p['ibh']:.1f}")
    c2.metric("ICR", f"{p['icr']:.1f}%")
    c3.metric("Friction Index", f"{p['friction']:.1f}")
    c4.metric("ROI Ajustado", f"{p['roi']*(p['ibh']/100):.1f}%")

    # Radar por eje
    promedios_eje = {eje: sum([p['scores'][c] for c in capas])/3 for eje, capas in EJES_CAPAS.items()}

    fig = go.Figure(go.Scatterpolar(
        r=list(promedios_eje.values()),
        theta=list(promedios_eje.keys()),
        fill='toself'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])))
    st.plotly_chart(fig, use_container_width=True)

    # OSINT REAL
    st.subheader("Alertas OSINT")
    noticias = motor_osint(f"conflicto mineria {p['id']} {p['provincia']}")
    for n in noticias:
        st.write("•", n["title"])

    # HISTORIAL
    st.subheader("Historial Auditorías")
    st.table(pd.DataFrame(st.session_state.historial_casos).tail(5))

    # PDF REAL
    pdf_bytes = generar_pdf(p, hash_val)
    st.download_button("📄 Descargar Reporte PDF", pdf_bytes, "reporte_heptagono.pdf")

else:
    st.info("Configure el caso y ejecute el pipeline desde la barra lateral.")
