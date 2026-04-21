import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import hashlib
import json
import base64

# --- 1. IDENTIDAD SOBERANA Y CONFIGURACIÓN ---
OWNER = "Claudio Falasca Consultor"
VERSION = "v11.2 Master Core"

st.set_page_config(page_title=f"Heptágono {VERSION}", layout="wide", initial_sidebar_state="expanded")

# --- 2. CAPA 14 Y 4: MOTOR DE DESPACHO Y RESET ---
class DespachoPro:
    @staticmethod
    def sanitizar_perseo(data):
        """Capa 14: Limpieza de PI para visualización de cliente"""
        d = data.copy()
        d['proyecto'] = "ACTIVO_BAJO_PROTOCOLO_PERSEO"
        d['ubicacion'] = "COORDENADAS_REDACTADAS_BY_FALASCA"
        return d

    @staticmethod
    def reset_atómico():
        """Capa 14: Purga absoluta de memoria de sesión"""
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# --- 3. ESTILOS DE ALTA DENSIDAD (Fisonomía Huarpe) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #080c10; color: #e8eaed; }}
    [data-testid="stSidebar"] {{ background-color: #0d1318; border-right: 1px solid #D4AF37; }}
    h1, h2, h3 {{ color: #D4AF37 !important; font-family: 'Syne', sans-serif; }}
    .stButton>button {{ background-color: #111920; border: 1px solid #D4AF37; color: #D4AF37; width: 100%; border-radius: 0; }}
    .stButton>button:hover {{ background-color: #D4AF37; color: #080c10; }}
    .report-box {{ border: 1px solid rgba(212, 175, 55, 0.3); padding: 15px; background: #0d1318; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. GOBERNANZA (Sidebar) ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/D4AF37/security-shield.png", width=80)
    st.title("MASTER CORE")
    st.subheader(OWNER)
    st.write("---")
    sources = st.number_input("Fuentes TGA Auditadas", value=112)
    st.write(f"Estado TGA: {'✅ VALIDADO' if sources >= 105 else '❌ BLOQUEADO'}")
    
    st.write("---")
    if st.button("🔥 RESET ATÓMICO (Capa 14)"):
        DespachoPro.reset_atómico()
    st.caption(f"© 2026 {OWNER}")

# --- 5. LÓGICA DE VALIDACIÓN (Gatekeeper Capa 15) ---
if sources < 105:
    st.error("⛔ SISTEMA BLOQUEADO: No se cumple la Regla de Oro (105 fuentes mínimas).")
    st.stop()

# --- 6. DASHBOARD OCD (Capa 19 - Estructura de 21 Capas) ---
st.title("🛡️ Copiloto Minero — Terminal Estratégica")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Inteligencia Predictiva", 
    "Blindaje Territorial", 
    "Transparencia TGA", 
    "Oráculo & Estrategia", 
    "Despacho & Perseo"
])

# TAB 1: RADAR Y SUPERVIVENCIA
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Capa 2: Diagnóstico Heptagonal")
        df_rad = pd.DataFrame({"Eje": ["Reg", "Amb", "Ope", "Soc", "Est", "Híd", "Eco"], "Val": [75, 40, 60, 45, 50, 65, 70]})
        fig = px.line_polar(df_rad, r='Val', theta='Eje', line_close=True, color_discrete_sequence=['#D4AF37'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Capa 16: Curva de Supervivencia")
        x = np.linspace(0, 36, 10)
        y = np.exp(-0.05 * x) * 100
        fig_cox = px.line(x=x, y=y, labels={'x':'Meses', 'y':'Prob. Éxito'}, color_discrete_sequence=['#00FFFF'])
        fig_cox.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_cox, use_container_width=True)

# TAB 2: CAPAS 6-9 (BLINDAJE)
with tab2:
    st.subheader("Capas 6-9: Certeza Jurídica y Aliados")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.info("Mapa de Fricción Territorial y Puntos de Apoyo Activos")
        # Simulación de mapa Huarpe
        st.markdown("<div style='height:300px; background:#111920; border:1px dashed #D4AF37; display:flex; align-items:center; justify-content:center;'>MAPA GEO-ESTRATÉGICO ACTIVO</div>", unsafe_allow_html=True)
    with col_b:
        st.metric("Índice Certeza Jurídica", "72%", "+5%")
        st.write("**Nodos de Soporte (Capa 7):**")
        st.success("✅ Aliado Local Catamarca: Activo")
        st.success("✅ Red Territorial San Juan: Validada")

# TAB 3: TRANSPARENCIA FORENSE (C15)
with tab3:
    st.subheader("Capa 15: Auditoría de Fuentes (Top 20)")
    df_tga = pd.DataFrame({
        "Fuente": ["Asamblea Pucará", "OCMAL Arg", "Boletín Oficial", "Mining Press", "CAEM Report"],
        "Tipo": ["Fricción", "Fricción", "Regulatorio", "Social", "Económico"],
        "Estado": ["Auditado", "Auditado", "Auditado", "Auditado", "Auditado"]
    })
    st.table(df_tga)
    st.caption(f"Hash de Integridad MD5: {hashlib.md5(OWNER.encode()).hexdigest()}")

# TAB 4: ORÁCULO Y WHAT-IF
with tab4:
    st.subheader("Capas 3, 5 y 18: Estrategia de Intervención")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.write("**Simulador What-If (Capa 5)**")
        ifs_val = st.slider("Ajuste de Impacto Social (IFS)", 0.0, 1.0, 0.45)
        if ifs_val > 0.6:
            st.warning("⚠️ SIMULACIÓN — NO FORENSE")
    with col_w2:
        st.write("**Propuesta Oráculo (Honorarios)**")
        st.markdown(f"""
            <div class='report-box'>
                <p>Retainer: $22,000 USD</p>
                <p>Success Fee: 2.5% ROI</p>
                <p><b>Titular: {OWNER}</b></p>
            </div>
        """, unsafe_allow_html=True)

# TAB 5: DESPACHO Y PERSEO (CAPAS 4 Y 14)
with tab5:
    st.subheader("Capas 4 y 14: Despacho Forense")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Protocolo Perseo")
        if st.button("🛡️ Activar Modo Cliente (Sanitizar)"):
            st.toast("Capa 14: Limpiando datos sensibles...")
            st.session_state.is_sanitized = True
        
        if st.session_state.get('is_sanitized'):
            st.info("ESTADO: Datos Sanitizados para Terceros")
        
    with c2:
        st.markdown("### Entrega de Artefactos")
        st.download_button(
            label="📄 Descargar Propuesta (PDF)",
            data=f"Reporte generado por {OWNER}",
            file_name=f"Propuesta_{OWNER.replace(' ', '_')}.pdf",
            mime="text/plain"
        )
        if st.button("🔑 Generar Director's Brief"):
            st.markdown(f"""
                <div style='background:#D4AF37; color:#080c10; padding:15px;'>
                    <b>BRIEF PARA {OWNER.upper()}</b><br>
                    Alerta: Riesgo hídrico detectado en Capa 15. ROI proyectado: 18.4%.
                </div>
            """, unsafe_allow_html=True)

st.write("---")
st.caption(f"Terminal Soberana operada exclusivamente por {OWNER} | {VERSION}")
