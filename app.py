import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import hashlib, json
from fpdf import FPDF
from duckduckgo_search import DDGS
import base64

# =========================================================
# 1. IDENTIDAD SOBERANA Y CONFIGURACIÓN (REGLA DE ORO)
# =========================================================
ID_SOBERANA = "Claudio Falasca Consultor"
SISTEMA = "HEPTÁGONO v12.2"  # Identidad corregida
EJES_OFICIALES = [
    "Político-Institucional", "Socio-Territorial", "Económico-Financiero",
    "Técnico-Minero", "Ambiental-Ecosistémico", "Hídrico-Soberano", "Comunicacional-Estratégico"
]

st.set_page_config(page_title=f"{SISTEMA} - {ID_SOBERANA}", layout="wide")

# Estilo OCD Midnight Gold
st.markdown("""
<style>
    .stApp { background:#05070a; color:#e5e7eb }
    [data-testid="stSidebar"] { background:#0e1117; border-right: 1px solid #D4AF37; }
    .stMetric { background:#0e1117; border-bottom: 3px solid #D4AF37; padding: 15px; border-radius: 5px; }
    .hash-footer { color:#4b5563; font-family:monospace; text-align:center; font-size: 11px; margin-top: 30px; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. MOTOR C22 - DESPACHO PDF REAL (NO SIMULACIÓN)
# =========================================================
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"{ID_SOBERANA} - {SISTEMA}", 0, 1, "C")
        self.ln(5)

def generar_pdf_v12(data, firma):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, f"PROYECTO: {data['proyecto']} | TERRITORIO: {data['territorio']}", ln=True)
    pdf.cell(0, 10, f"FECHA: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, "AUDITORÍA DE EJES (HEPTÁGONO):", ln=True)
    pdf.set_font("Arial", size=10)
    for eje, val in data["scores"].items():
        pdf.cell(0, 8, f"- {eje}: {val}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, f"ICR (Índice de Conflicto Relacional): {data['icr']}%", ln=True)
    pdf.cell(0, 10, f"ROI PROYECTADO: {data['roi']}%", ln=True)
    pdf.ln(10)
    pdf.set_font("Courier", "I", 8)
    pdf.multi_cell(0, 10, f"FIRMA FORENSE MD5: {firma}")
    return pdf.output(dest="S").encode("latin-1")

# =========================================================
# 3. MOTOR OSINT - ALERTAS (SIN INFERENCIA DE SCORES)
# =========================================================
def ejecutar_osint_alertas(proyecto, territorio):
    alertas = []
    with DDGS() as ddgs:
        query = f"conflicto minería {proyecto} {territorio}"
        try:
            results = list(ddgs.text(query, max_results=5))
            for r in results:
                alertas.append({"titulo": r["title"], "link": r["href"]})
        except: pass
    return alertas

# =========================================================
# 4. UI - CABINA DE CONTROL INTERACTIVA
# =========================================================
st.title(f"🏛️ {ID_SOBERANA}")
st.caption(f"Terminal de Gestión e Inteligencia Territorial | {SISTEMA}")

with st.sidebar:
    st.header("🕹️ Control de Activos")
    # Preparado para carga de 150+ proyectos
    proyecto_sel = st.selectbox("Cartera de Proyectos", ["Josemaría", "Veladero", "Peñas Negras", "Taca Taca", "Lindero"])
    territorio_sel = st.text_input("Territorio", "Argentina")
    roi_sel = st.slider("ROI Proyectado (%)", 0, 80, 25)
    
    st.divider()
    st.subheader("Auditoría de Ejes (Manual)")
    scores_audit = {}
    for eje in EJES_OFICIALES:
        # EL SISTEMA NO INFIERE: El consultor audita y pone el valor
        scores_audit[eje] = st.slider(eje, 0, 100, 70)
    
    st.divider()
    ejecutar = st.button("🚀 EJECUTAR ESCANEO Y FIRMA")

# =========================================================
# 5. LÓGICA DE PROCESAMIENTO Y GUARDIA MLC
# =========================================================
if ejecutar:
    with st.spinner("SISTEMA: Escaneando entorno OSINT..."):
        alertas_reales = ejecutar_osint_alertas(proyecto_sel, territorio_sel)
        icr = 100 - scores_audit["Socio-Territorial"]
        
        # COLUMNAS TÁCTICAS
        c1, c2, c3 = st.columns([1.5, 1, 1])
        
        with c1:
            st.subheader("📡 Radar Heptágono")
            fig = go.Figure(go.Scatterpolar(
                r=list(scores_audit.values()), theta=EJES_OFICIALES, fill='toself', line_color='#D4AF37'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                              paper_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig, use_container_width=True)
            
        with c2:
            st.subheader("🛡️ Seguridad MLC")
            st.metric("ICR (Conflicto)", f"{icr}%")
            st.metric("ROI", f"{roi_sel}%")
            
            # GUARDIA MLC DURA (Mandato C20)
            if icr > 70 and roi_sel > 30:
                st.error("🚫 BLOQUEO ÉTICO MLC: Inconsistencia detectada.")
                st.stop() # Mata el proceso inmediatamente
            else:
                st.success("✅ DESPACHO AUTORIZADO")
                
        with c3:
            st.subheader("📡 Alertas OSINT")
            for a in alertas_reales:
                st.warning(f"⚠️ [{a['titulo'][:50]}...]({a['link']})")

        # PAYLOAD COMPLETO PARA HASH FORENSE (Mandato C21)
        payload = {
            "owner": ID_SOBERANA, "sistema": SISTEMA, "proyecto": proyecto_sel,
            "territorio": territorio_sel, "scores": scores_audit, "icr": icr,
            "roi": roi_sel, "alertas_count": len(alertas_reales)
        }
        firma_md5 = hashlib.md5(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        
        # BOTÓN C22 PDF REAL
        st.divider()
        pdf_bytes = generar_pdf_v12({"proyecto": proyecto_sel, "territorio": territorio_sel, 
                                     "scores": scores_audit, "icr": icr, "roi": roi_sel}, firma_md5)
        st.download_button("📥 DESPACHAR REPORTE PDF FIRMADO", data=pdf_bytes, 
                           file_name=f"HEPTAGONO_{proyecto_sel}_{firma_md5[:8]}.pdf", mime="application/pdf")
        
        st.markdown(f"<div class='hash-footer'>SELLO FORENSE MD5: {firma_md5}</div>", unsafe_allow_html=True)
else:
    st.info("Utilice la Cabina de Control lateral para iniciar la auditoría del activo.")
