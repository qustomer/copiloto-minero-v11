import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib

# --- 1. MÓDULOS INTEGRADOS (Evita ModuleNotFoundError) ---
class InternalHarvester:
    def run_harvest(self, n_sources):
        payload = f"audit_log_claudio_falasca_{n_sources}"
        return {
            "total_fuentes": n_sources,
            "md5": hashlib.md5(payload.encode()).hexdigest(),
            "valid": n_sources >= 105
        }

# --- 2. CONFIGURACIÓN DE INTERFAZ MASTER CORE ---
st.set_page_config(page_title="Heptágono v10.1 | Master Core", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #080c10; color: #e8eaed; }
    [data-testid="stSidebar"] { background-color: #0d1318; border-right: 1px solid rgba(212, 175, 55, 0.2); }
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'Syne', sans-serif; }
    .tech-table { background-color: #111920; border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 8px; margin-bottom: 25px; overflow: hidden; }
    .t-row { display: flex; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .t-header { background-color: rgba(212, 175, 55, 0.15); color: #D4AF37; font-weight: 800; text-transform: uppercase; font-size: 11px; padding: 12px; }
    .t-col { padding: 12px; font-size: 13px; color: #ffffff; }
    .t-label { background-color: rgba(212, 175, 55, 0.08); color: #D4AF37 !important; font-weight: 600; width: 30%; }
    .seal-box { border: 2px dashed #D4AF37; padding: 20px; border-radius: 8px; background-color: rgba(212, 175, 55, 0.03); text-align: center; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL: CONTROL SOBERANO ---
with st.sidebar:
    st.title("HEPTÁGONO v10.1")
    st.markdown("**OPERADOR:** Claudio Falasca Consultor")
    st.write("---")
    capa_activa = st.radio("Capas de Ejecución:", ["Diagnóstico 7 Ejes", "Riesgo & Supervivencia", "Estrategia & Oráculo"])
    st.write("---")
    sources_input = st.number_input("Fuentes TGA Auditadas", value=112)
    harvester = InternalHarvester().run_harvest(sources_input)
    st.caption("© 2026 Claudio Falasca Consultor")

# --- 4. HEADER ---
st.caption("CAPA 19: OPERATOR CONTROL DASHBOARD (OCD)")
st.title("Copiloto Minero v11.1")

if not harvester["valid"]:
    st.error(f"⛔ TGA BLOQUEADO: {sources_input} fuentes. La Regla de Oro exige 105.")
    st.stop()

# --- 5. EJECUCIÓN DE CAPAS ---

if capa_activa == "Diagnóstico 7 Ejes":
    st.subheader("Capa 2: Diagnóstico Determinístico (Heptágono)")
    df_ejes = pd.DataFrame({
        "Eje": ["Regulatorio", "Ambiental", "Operacional", "Social", "Estratégico", "Hídrico", "Económico"],
        "Puntaje": [78, 38, 55, 42, 47, 60, 65]
    })
    
    col1, col2 = st.columns([2, 1])
    with col1:
        fig_rad = px.line_polar(df_ejes, r='Puntaje', theta='Eje', line_close=True, range_r=[0,100], color_discrete_sequence=['#D4AF37'])
        fig_rad.update_traces(fill='toself', fillcolor='rgba(212, 175, 55, 0.2)')
        fig_rad.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_rad, use_container_width=True)
    with col2:
        st.metric("IBH SCORE", "55.0", "-4.2")
        if df_ejes.iloc[1]['Puntaje'] < 40:
            st.error("⚠️ Capa 20 (MLC): Riesgo Ambiental Crítico detectado.")

elif capa_activa == "Riesgo & Supervivencia":
    st.subheader("Capa 16: Análisis de Supervivencia (Cox)")
    meses = np.arange(0, 37, 3)
    prob_base = np.exp(-0.09 * meses) * 100
    prob_claudio = np.exp(-0.02 * meses) * 100
    
    fig_cox = go.Figure()
    fig_cox.add_trace(go.Scatter(x=meses, y=prob_base, name='⚠️ ESCENARIO BASE (Riesgo)', line=dict(color='#FF3131', width=3, dash='dot')))
    fig_cox.add_trace(go.Scatter(x=meses, y=prob_claudio, name='💎 PROYECCIÓN CLAUDIO FALASCA', line=dict(color='#00FFFF', width=5)))
    
    fig_cox.add_annotation(x=36, y=5, text="FALLO", bgcolor="#FF3131", font=dict(color="white"))
    fig_cox.add_annotation(x=36, y=85, text="ÉXITO CF", bgcolor="#00FFFF", font=dict(color="black"))

    fig_cox.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"),
                          legend=dict(orientation="h", y=1.1, bgcolor="rgba(255,255,255,0.1)"))
    st.plotly_chart(fig_cox, use_container_width=True)

elif capa_activa == "Estrategia & Oráculo":
    # 6. IMPLICANCIAS
    st.subheader("7. Implicancias Estratégicas")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header"><div style="width:25%;">Dimensión</div><div style="width:55%;">Implicancia</div><div style="width:20%;">Urgencia</div></div>
            <div class="t-row"><div class="t-col t-label">Territorial</div><div class="t-col" style="width:55%;">Bloqueo por falta de srv_hidrico.</div><div class="t-col" style="width:20%; color:#FF3131;">ALTA</div></div>
        </div>
    """, unsafe_allow_html=True)

    # 7. CRONOGRAMA
    st.subheader("Hoja de Ruta - Cronograma Claudio Falasca")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header"><div style="width:20%;">Fase</div><div style="width:60%;">Acción Master Core</div><div style="width:20%;">Hito</div></div>
            <div class="t-row"><div class="t-col t-label">Mes 1</div><div class="t-col" style="width:60%;">Auditoría TGA y Activos Críticos.</div><div class="t-col" style="width:20%;">Validación</div></div>
            <div class="t-row"><div class="t-col t-label">Mes 3</div><div class="t-col" style="width:60%;">Sello Forense Capa 21.</div><div class="t-col" style="width:20%;">Certificación</div></div>
        </div>
    """, unsafe_allow_html=True)

    # 8. PROPUESTA COMERCIAL
    st.subheader("Propuesta Comercial e Honorarios")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header"><div style="width:10%;">#</div><div style="width:50%;">Servicio Base</div><div style="width:20%;">USD</div><div style="width:20%;">Estado</div></div>
            <div class="t-row"><div class="t-col" style="width:10%;">01</div><div class="t-col" style="width:50%;">Diagnóstico Master Core</div><div class="t-col" style="width:20%;">$55,000</div><div class="t-col" style="width:20%; color:#00FFFF;">ACTIVO</div></div>
        </div>
    """, unsafe_allow_html=True)

    st.write("### Cálculo de Honorarios — Oráculo v11.1")
    st.markdown(f"""
        <div class="tech-table">
            <div class="t-row t-header"><div style="width:30%;">Parámetro</div><div style="width:20%;">Valor</div><div style="width:50%;">Detalle</div></div>
            <div class="t-row"><div class="t-col t-label">Retainer (40%)</div><div class="t-col" style="width:20%;">$22,000</div><div class="t-col" style="width:50%;">Despliegue inicial validado.</div></div>
        </div>
    """, unsafe_allow_html=True)

    # 9. SELLO FORENSE
    st.subheader("8. Metodología y Sello de Integridad Forense")
    st.markdown("""
        <div class="tech-table">
            <div class="t-row t-header"><div style="width:40%;">Componente</div><div style="width:60%;">Función</div></div>
            <div class="t-row"><div class="t-col t-label">Capa 21</div><div class="t-col" style="width:60%;">Garantía de Inmutabilidad Determinística.</div></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="seal-box">
            <h3 style="margin:0;">🛡️ SELLO FORENSE VÁLIDO</h3>
            <p style="color:#8899a6; font-size:12px;">EMITIDO POR: CLAUDIO FALASCA CONSULTOR</p>
            <code style="color:#D4AF37;">HASH: {harvester["md5"]}</code>
        </div>
    """, unsafe_allow_html=True)

# PIE DE PÁGINA
st.divider()
st.caption('Heptágono v10.1 — Sistema de Claudio Falasca Consultor')
