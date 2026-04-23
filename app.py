import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import hashlib, json, io
from datetime import datetime
from duckduckgo_search import DDGS
from fpdf import FPDF

# =========================================================
# CONFIG INICIAL
# =========================================================
st.set_page_config(page_title="HEPTAGONO Copiloto Minero", layout="wide")

ID_CONSULTOR = "Claudio Falasca Consultor"

# Persistencia real
if "historial" not in st.session_state:
    st.session_state.historial = []
if "pipeline_activo" not in st.session_state:
    st.session_state.pipeline_activo = None

# =========================================================
# ARQUITECTURA 7 EJES / 21 CAPAS
# =========================================================
EJES = {
    "Político-Institucional": ["Marco Regulatorio","Estabilidad Jurídica","Permisos"],
    "Socio-Territorial": ["Licencia Social","Conflictos Activos","Derechos Indígenas"],
    "Económico-Financiero": ["ROI/EBITDA","Proveedores Locales","Costo Oportunidad"],
    "Técnico-Minero": ["Geología","Infraestructura","Logística"],
    "Ambiental-Ecosistémico": ["Biodiversidad","Glaciares","Pasivos"],
    "Hídrico-Soberano": ["Cuencas","Estrés Hídrico","Gobernanza Agua"],
    "Comunicacional": ["Percepción","Crisis","Stakeholders"]
}

# =========================================================
# FUNCIONES MOTOR
# =========================================================
def osint_busqueda(query):
    try:
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=5))
    except:
        return []

def hash_forense(payload):
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

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
    pdf.multi_cell(0,10,f"Hash Forense: {hash_val}")

    buffer = io.BytesIO()
    pdf.output(buffer)
    return buffer.getvalue()

# =========================================================
# SIDEBAR — CABINA CONTROL
# =========================================================
with st.sidebar:
    st.title("Cabina de Control")

    with st.form("form_pipeline"):
        id_caso = st.text_input("ID Proyecto","PRJ-001")
        provincia = st.selectbox("Provincia",["San Juan","Catamarca","Salta","Jujuy","Santa Cruz"])
        roi_obj = st.slider("ROI Objetivo",0,80,25)

        st.divider()
        st.subheader("Activación de 21 capas")

        scores = {}
        for eje,capas in EJES.items():
            with st.expander(eje):
                for capa in capas:
                    scores[capa] = st.slider(capa,0,100,70)

        ejecutar = st.form_submit_button("Ejecutar Pipeline")

# =========================================================
# EJECUCIÓN DEL PIPELINE
# =========================================================
if ejecutar:

    # OSINT REAL
    noticias = osint_busqueda(f"mineria conflicto {provincia}")

    # PROMEDIOS POR EJE
    prom_ejes = {eje: sum(scores[c] for c in capas)/3 for eje,capas in EJES.items()}
    ibh = sum(scores.values())/21

    # ICR OFICIAL (mandato)
    icr = 100 - prom_ejes["Socio-Territorial"]

    # FRICTION INDEX
    friction = (100-prom_ejes["Socio-Territorial"] + 100-prom_ejes["Comunicacional"])/2

    # GUARDIA MLC REAL
    if scores["Licencia Social"] < 30 or scores["Conflictos Activos"] < 30 or scores["Gobernanza Agua"] < 30:
        st.error("BLOQUEO ETICO MLC ACTIVADO")
        st.stop()

    payload = {
        "id":id_caso,
        "provincia":provincia,
        "roi_obj":roi_obj,
        "scores":scores,
        "promedios":prom_ejes,
        "ibh":ibh,
        "icr":icr,
        "friction":friction,
        "osint":noticias
    }

    hash_val = hash_forense(payload)

    st.session_state.pipeline_activo = payload
    st.session_state.historial.append({
        "id":id_caso,
        "fecha":datetime.now().strftime("%Y-%m-%d %H:%M"),
        "ibh":round(ibh,2),
        "hash":hash_val[:12]
    })

# =========================================================
# DASHBOARD PRINCIPAL
# =========================================================
if st.session_state.pipeline_activo:

    p = st.session_state.pipeline_activo
    hash_val = hash_forense(p)

    st.title("Centro de Operaciones Heptagono")

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("IBH",f"{p['ibh']:.1f}")
    c2.metric("ICR",f"{p['icr']:.1f}%")
    c3.metric("Friction",f"{p['friction']:.1f}")
    c4.metric("ROI Ajustado",f"{p['roi_obj']*(p['ibh']/100):.1f}%")

    # RADAR
    fig = go.Figure(go.Scatterpolar(
        r=list(p["promedios"].values()),
        theta=list(p["promedios"].keys()),
        fill='toself'
    ))
    st.plotly_chart(fig,use_container_width=True)

    # OSINT
    st.subheader("Alertas OSINT")
    for n in p["osint"]:
        st.write(f"• {n['title']}")

    # HISTORIAL
    st.subheader("Historial Auditorías")
    st.dataframe(pd.DataFrame(st.session_state.historial))

    # PDF REAL
    pdf_bytes = generar_pdf(p,hash_val)
    st.download_button("Descargar Reporte PDF",pdf_bytes,"reporte.pdf")

else:
    st.info("Configure el caso y ejecute el pipeline")
