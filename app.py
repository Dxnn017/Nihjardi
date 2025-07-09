import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Diagnóstico Organizacional - Calzados Nihjardi",
    page_icon="👞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #D97706 0%, #EA580C 50%, #DC2626 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #EA580C;
    }
    .section-header {
        background: linear-gradient(90deg, #FEF3C7 0%, #FED7AA 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Datos simulados basados en el estudio
@st.cache_data
def load_data():
    # Datos de la encuesta (8 participantes)
    participantes = 8
    
    # Resultados por sección
    resultados = {
        'Ambiente Familiar': {
            'promedio': 4.2,
            'preguntas': {
                'Ambiente de trabajo': [5, 2, 1, 0],
                'Comunicación con Don Carlos': [4, 3, 1, 0],
                'Apoyo entre compañeros': [3, 4, 1, 0]
            }
        },
        'Proceso Artesanal': {
            'promedio': 3.1,
            'preguntas': {
                'Organización del taller': [1, 3, 3, 1],
                'Planificación diaria': [2, 2, 3, 1],
                'Orgullo del producto': [4, 3, 1, 0]
            }
        },
        'Cambio y Mejora': {
            'promedio': 3.4,
            'preguntas': {
                'Actitud hacia cambios': [2, 3, 2, 1],
                'Reacción a nuevas formas': [1, 4, 2, 1],
                'Ideas de mejora': [2, 3, 2, 1]
            }
        },
        'Identidad Nihjardi': {
            'promedio': 4.5,
            'preguntas': {
                'Lo que más valoro': [4, 2, 1, 1],
                'Nunca cambiar': [3, 3, 1, 1],
                'Futuro de la empresa': [3, 4, 1, 0]
            }
        }
    }
    
    return participantes, resultados

def main():
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>👞 Calzados "Nihjardi"</h1>
        <h2>Diagnóstico Organizacional 2024</h2>
        <p>Análisis integral del proceso de cambio organizacional</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar para navegación
    st.sidebar.title("🧭 Navegación")
    page = st.sidebar.selectbox(
        "Selecciona una sección:",
        ["📊 Dashboard Ejecutivo", "📋 Encuesta Interactiva", "📈 Análisis Detallado", "💡 Recomendaciones"]
    )
    
    participantes, resultados = load_data()
    
    if page == "📊 Dashboard Ejecutivo":
        show_dashboard(participantes, resultados)
    elif page == "📋 Encuesta Interactiva":
        show_survey()
    elif page == "📈 Análisis Detallado":
        show_detailed_analysis(resultados)
    elif page == "💡 Recomendaciones":
        show_recommendations()

def show_dashboard(participantes, resultados):
    st.header("📊 Dashboard Ejecutivo")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="👥 Participantes",
            value=f"{participantes}/8",
            delta="100% participación"
        )
    
    with col2:
        st.metric(
            label="🤝 Cohesión del Equipo",
            value="4.2/5",
            delta="84% - Fortaleza"
        )
    
    with col3:
        st.metric(
            label="🔄 Disposición al Cambio",
            value="3.4/5",
            delta="68% - Oportunidad"
        )
    
    with col4:
        st.metric(
            label="⭐ Identidad Empresarial",
            value="4.5/5",
            delta="90% - Excelente"
        )
    
    # Gráfico de radar
    st.subheader("🎯 Perfil Organizacional")
    
    categories = ['Ambiente Familiar', 'Calidad Artesanal', 'Organización', 
                 'Comunicación', 'Disposición al Cambio', 'Identidad Empresarial']
    values = [84, 90, 62, 78, 68, 90]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Calzados Nihjardi',
        line_color='#EA580C',
        fillcolor='rgba(234, 88, 12, 0.3)'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        height=500
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Resumen por secciones
    st.subheader("📋 Resumen por Secciones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras con promedios
        secciones = list(resultados.keys())
        promedios = [resultados[s]['promedio'] for s in secciones]
        
        fig_bar = px.bar(
            x=secciones,
            y=promedios,
            title="Promedio por Sección",
            color=promedios,
            color_continuous_scale=['#FEE2E2', '#DC2626'],
            text=[f"{p:.1f}" for p in promedios]
        )
        fig_bar.update_traces(textposition='outside')
        fig_bar.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Proyección del cambio
        meses = ['Actual', 'Mes 1', 'Mes 2', 'Mes 3', 'Mes 6']
        resistencia = [65, 55, 45, 35, 25]
        aceptacion = [35, 45, 55, 65, 75]
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=meses, y=resistencia,
            mode='lines+markers',
            name='Resistencia al Cambio',
            line=dict(color='#DC2626', width=3)
        ))
        fig_line.add_trace(go.Scatter(
            x=meses, y=aceptacion,
            mode='lines+markers',
            name='Aceptación del Cambio',
            line=dict(color='#059669', width=3)
        ))
        fig_line.update_layout(
            title="Proyección del Cambio",
            yaxis_title="Porcentaje (%)",
            height=400
        )
        st.plotly_chart(fig_line, use_container_width=True)

def show_survey():
    st.header("📋 Encuesta Interactiva")
    st.info("Esta es una simulación de la encuesta aplicada a los 8 participantes de Calzados Nihjardi")
    
    # Secciones de la encuesta
    secciones = {
        "🤝 Ambiente Familiar": {
            "preguntas": [
                "¿Cómo sientes el ambiente familiar en Calzados Nihjardi?",
                "¿Cómo describes la comunicación con Don Carlos?",
                "¿Cómo reaccionan tus compañeros cuando tienes dificultades?"
            ],
            "opciones": [
                ["Como en casa, somos familia", "Buen ambiente con respeto", "Agradable con tensiones", "Podría mejorar"],
                ["Excelente, siempre escucha", "Buena disponibilidad", "Solo temas de trabajo", "Difícil acercarse"],
                ["Siempre me ayudan", "Me ayudan si pido", "A veces ayudan", "Cada uno en lo suyo"]
            ]
        },
        "🔨 Proceso Artesanal": {
            "preguntas": [
                "¿Cómo está organizado nuestro taller?",
                "¿Cómo te sientes con la planificación diaria?",
                "¿Qué tan orgulloso te sientes del calzado que producimos?"
            ],
            "opciones": [
                ["Muy bien organizado", "Bien, puede mejorar", "Regular, perdemos tiempo", "Desorganizado"],
                ["Me gusta la flexibilidad", "Está bien", "Más claridad", "Mejor planificación"],
                ["Muy orgulloso", "Orgulloso", "Moderadamente", "Poco orgulloso"]
            ]
        }
    }
    
    # Mostrar encuesta interactiva
    for seccion, contenido in secciones.items():
        with st.expander(seccion, expanded=True):
            for i, pregunta in enumerate(contenido["preguntas"]):
                st.write(f"**{pregunta}**")
                respuesta = st.radio(
                    "Selecciona tu respuesta:",
                    contenido["opciones"][i],
                    key=f"{seccion}_{i}",
                    horizontal=True
                )
                st.write("---")
    
    if st.button("🎯 Ver Resultados Simulados", type="primary"):
        st.success("¡Gracias por completar la encuesta! Los resultados se muestran en el Dashboard Ejecutivo.")

def show_detailed_analysis(resultados):
    st.header("📈 Análisis Detallado por Sección")
    
    for seccion, datos in resultados.items():
        st.subheader(f"📊 {seccion}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Crear gráficos para cada pregunta
            for pregunta, respuestas in datos['preguntas'].items():
                opciones = ["Muy Positivo", "Positivo", "Regular", "Negativo"]
                
                fig = px.bar(
                    x=opciones,
                    y=respuestas,
                    title=f"{pregunta}",
                    color=respuestas,
                    color_continuous_scale='RdYlGn_r'
                )
                fig.update_layout(height=300, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.metric(
                label="Promedio Sección",
                value=f"{datos['promedio']}/5",
                delta=f"{(datos['promedio']/5)*100:.0f}%"
            )
            
            # Interpretación
            if datos['promedio'] >= 4.0:
                st.success("🟢 Fortaleza identificada")
            elif datos['promedio'] >= 3.5:
                st.info("🟡 Área con potencial")
            else:
                st.warning("🟠 Requiere atención")
        
        st.write("---")

def show_recommendations():
    st.header("💡 Recomendaciones Estratégicas")
    
    # Conclusiones principales
    st.subheader("🎯 Conclusiones Principales")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **🟢 Fortalezas**
        - Ambiente familiar excepcional (87.5%)
        - Orgullo artesanal alto (87.5%)
        - Identidad empresarial sólida (90%)
        - Comunicación abierta con liderazgo
        """)
    
    with col2:
        st.warning("""
        **🟡 Oportunidades**
        - Organización del taller (50% necesita mejoras)
        - Planificación diaria (50% requiere claridad)
        - Disposición moderada al cambio (68%)
        """)
    
    with col3:
        st.info("""
        **🔵 Recomendaciones**
        - Implementar cambios graduales
        - Mantener comunicación constante
        - Preservar identidad artesanal
        - Capacitación en organización
        """)
    
    # Plan de implementación
    st.subheader("📅 Plan de Implementación Sugerido")
    
    fases = {
        "Fase 1 (Mes 1-2)": {
            "objetivo": "Preparación y sensibilización",
            "acciones": [
                "Reuniones de sensibilización sobre la necesidad del cambio",
                "Formación del equipo guía (propietario + 2 colaboradores clave)",
                "Comunicación clara de la visión del cambio"
            ]
        },
        "Fase 2 (Mes 2-4)": {
            "objetivo": "Implementación gradual",
            "acciones": [
                "Reorganización física del taller",
                "Implementación de planificación diaria simple",
                "Capacitación en organización del espacio"
            ]
        },
        "Fase 3 (Mes 4-6)": {
            "objetivo": "Consolidación",
            "acciones": [
                "Rutinas de mantenimiento preventivo",
                "Sistema básico de control de pedidos",
                "Evaluación y ajustes del proceso"
            ]
        }
    }
    
    for fase, contenido in fases.items():
        with st.expander(fase, expanded=True):
            st.write(f"**Objetivo:** {contenido['objetivo']}")
            st.write("**Acciones:**")
            for accion in contenido['acciones']:
                st.write(f"• {accion}")
    
    # Métricas de éxito
    st.subheader("📊 Métricas de Éxito Proyectadas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Probabilidad de Éxito",
            value="78%",
            delta="Alto potencial"
        )
    
    with col2:
        st.metric(
            label="Tiempo Estimado",
            value="4-6 meses",
            delta="Implementación gradual"
        )
    
    with col3:
        st.metric(
            label="Riesgo General",
            value="Bajo",
            delta="Equipo cohesionado"
        )

if __name__ == "__main__":
    main()
