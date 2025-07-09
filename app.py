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
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #FEF3C7;
        border-radius: 10px 10px 0px 0px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #EA580C;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>👞 Calzados "Nihjardi"</h1>
        <h2>Diagnóstico Organizacional 2024</h2>
        <p>Análisis integral del proceso de cambio organizacional</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs para navegación
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Dashboard", "📋 Encuesta", "📈 Análisis", "🔄 Curva Kübler-Ross", "💡 Recomendaciones"])
    
    with tab1:
        show_dashboard()
    
    with tab2:
        show_survey()
    
    with tab3:
        show_analysis()
    
    with tab4:
        show_kubler_ross()
    
    with tab5:
        show_recommendations()

def show_dashboard():
    st.header("📊 Dashboard Ejecutivo")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="👥 Participantes",
            value="8/8",
            delta="100% participación"
        )
    
    with col2:
        st.metric(
            label="🤝 Cohesión del Equipo",
            value="4.2/5",
            delta="84%"
        )
    
    with col3:
        st.metric(
            label="🔄 Disposición al Cambio",
            value="3.4/5",
            delta="68%"
        )
    
    with col4:
        st.metric(
            label="⭐ Identidad Empresarial",
            value="4.5/5",
            delta="90%"
        )
    
    # Gráfico de radar
    st.subheader("🎯 Perfil Organizacional")
    
    categories = ['Ambiente<br>Familiar', 'Calidad<br>Artesanal', 'Organización', 
                 'Comunicación', 'Disposición<br>al Cambio', 'Identidad<br>Empresarial']
    values = [84, 90, 62, 78, 68, 90]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Calzados Nihjardi',
        line=dict(color='#EA580C', width=3),
        fillcolor='rgba(234, 88, 12, 0.3)',
        marker=dict(size=8, color='#EA580C')
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            ),
            angularaxis=dict(
                tickfont=dict(size=12)
            )
        ),
        showlegend=True,
        height=500,
        font=dict(size=12)
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Resumen por secciones
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Promedios por Sección")
        
        secciones = ['Ambiente Familiar', 'Proceso Artesanal', 'Cambio y Mejora', 'Identidad Nihjardi']
        promedios = [4.2, 3.1, 3.4, 4.5]
        colores = ['#059669' if p >= 4.0 else '#F59E0B' if p >= 3.5 else '#EF4444' for p in promedios]
        
        fig_bar = go.Figure(data=[
            go.Bar(x=secciones, y=promedios, 
                  marker_color=colores,
                  text=[f"{p:.1f}" for p in promedios],
                  textposition='outside')
        ])
        
        fig_bar.update_layout(
            title="Evaluación por Sección",
            yaxis=dict(range=[0, 5]),
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.subheader("📈 Proyección del Cambio")
        
        meses = ['Actual', 'Mes 1', 'Mes 2', 'Mes 3', 'Mes 6']
        resistencia = [65, 55, 45, 35, 25]
        aceptacion = [35, 45, 55, 65, 75]
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=meses, y=resistencia,
            mode='lines+markers',
            name='Resistencia al Cambio',
            line=dict(color='#DC2626', width=3),
            marker=dict(size=8)
        ))
        fig_line.add_trace(go.Scatter(
            x=meses, y=aceptacion,
            mode='lines+markers',
            name='Aceptación del Cambio',
            line=dict(color='#059669', width=3),
            marker=dict(size=8)
        ))
        
        fig_line.update_layout(
            title="Evolución Esperada",
            yaxis_title="Porcentaje (%)",
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_line, use_container_width=True)

def show_survey():
    st.header("📋 Encuesta de Diagnóstico Organizacional")
    
    st.info("💡 Esta es una simulación de la encuesta aplicada a los 8 participantes de Calzados Nihjardi")
    
    # Datos de ejemplo para mostrar
    with st.expander("🤝 Ambiente Familiar", expanded=True):
        st.write("**¿Cómo sientes el ambiente familiar en Calzados Nihjardi?**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Como en casa", "5", "62.5%")
        with col2:
            st.metric("Buen respeto", "2", "25%")
        with col3:
            st.metric("Con tensiones", "1", "12.5%")
        with col4:
            st.metric("Podría mejorar", "0", "0%")
        
        # Gráfico de la pregunta
        opciones = ["Como en casa", "Buen respeto", "Con tensiones", "Podría mejorar"]
        valores = [5, 2, 1, 0]
        
        fig = px.pie(values=valores, names=opciones, 
                    title="Distribución de Respuestas",
                    color_discrete_sequence=['#059669', '#F59E0B', '#EF4444', '#6B7280'])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("🔨 Proceso Artesanal"):
        st.write("**¿Cómo está organizado nuestro taller actualmente?**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Muy bien", "1", "12.5%")
        with col2:
            st.metric("Bien", "3", "37.5%")
        with col3:
            st.metric("Regular", "3", "37.5%")
        with col4:
            st.metric("Desorganizado", "1", "12.5%")
    
    with st.expander("💡 Cambio y Mejora"):
        st.write("**¿Cuál es tu actitud hacia implementar cambios?**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Me emociona", "2", "25%")
        with col2:
            st.metric("Me parece bien", "3", "37.5%")
        with col3:
            st.metric("Me da nervios", "2", "25%")
        with col4:
            st.metric("Prefiero igual", "1", "12.5%")
    
    with st.expander("⭐ Identidad Nihjardi"):
        st.write("**¿Qué es lo que más valoras de trabajar aquí?**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Ambiente familiar", "4", "50%")
        with col2:
            st.metric("Calidad artesanal", "2", "25%")
        with col3:
            st.metric("Estabilidad", "1", "12.5%")
        with col4:
            st.metric("Conocimiento", "1", "12.5%")

def show_analysis():
    st.header("📈 Análisis Detallado")
    
    # Análisis FODA
    st.subheader("🎯 Análisis FODA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **💪 FORTALEZAS**
        - Ambiente familiar excepcional (87.5%)
        - Alto orgullo por la calidad artesanal
        - Comunicación abierta con el liderazgo
        - Equipo leal y comprometido
        - Identidad empresarial sólida
        """)
        
        st.info("""
        **🌟 OPORTUNIDADES**
        - Mercado limeño en crecimiento
        - Demanda por productos artesanales
        - Posibilidad de mejora en eficiencia
        - Capacitación del equipo
        - Expansión gradual
        """)
    
    with col2:
        st.warning("""
        **⚠️ DEBILIDADES**
        - Organización del taller (50% necesita mejoras)
        - Planificación diaria informal
        - Dependencia del propietario
        - Resistencia inicial al cambio
        - Procesos no documentados
        """)
        
        st.error("""
        **🚨 AMENAZAS**
        - Competencia industrializada
        - Cambios en preferencias del consumidor
        - Presión de precios
        - Dependencia de proveedores
        - Riesgo de estancamiento
        """)
    
    # Matriz de cambio
    st.subheader("🔄 Matriz del Cambio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**SI CAMBIO**")
        st.success("""
        **¿Qué gano?**
        - Mayor eficiencia productiva
        - Mejor organización del taller
        - Reducción de errores
        - Mayor capacidad competitiva
        """)
        
        st.warning("""
        **¿Qué dificultades tendré?**
        - Superar resistencia inicial
        - Tiempo de adaptación
        - Inversión en capacitación
        - Cambio de rutinas
        """)
    
    with col2:
        st.write("**SI NO CAMBIO**")
        st.info("""
        **¿Qué conservo?**
        - Estabilidad operativa inmediata
        - Hábitos conocidos
        - Zona de confort
        - Procesos familiares
        """)
        
        st.error("""
        **¿Qué pierdo?**
        - Competitividad a largo plazo
        - Oportunidades de crecimiento
        - Eficiencia operativa
        - Satisfacción del cliente
        """)

def show_kubler_ross():
    st.header("🔄 Curva del Cambio de Kübler-Ross")
    st.subheader("Aplicada en Calzados 'Nihjardi'")
    
    # Datos de las etapas
    etapas_data = {
        'Etapa': ['Shock', 'Negación', 'Frustración', 'Depresión', 'Experimentación', 'Decisión', 'Integración'],
        'Nivel_Confianza': [80, 70, 45, 25, 55, 80, 95],
        'Tiempo': [0, 1, 2, 3, 4, 5, 6],
        'Color': ['#FCD34D', '#EF4444', '#F97316', '#3B82F6', '#F59E0B', '#10B981', '#8B5CF6'],
        'Descripcion': [
            "Sorpresa inicial ante el anuncio del cambio",
            "Incredulidad sobre la necesidad de cambiar",
            "Incomodidad durante la implementación inicial",
            "Descenso del ánimo durante la adaptación",
            "Disposición a probar nuevas formas de trabajo",
            "Aceptación consciente del nuevo contexto",
            "Integración de nuevos hábitos en la cultura"
        ],
        'Frases_Tipicas': [
            "¿Por qué tenemos que cambiar ahora?",
            "Así siempre se ha trabajado",
            "Esto es más complicado",
            "Esto es muy cansado",
            "Vamos a intentar esto",
            "Ahora entiendo cómo funciona",
            "Así es como trabajamos ahora"
        ],
        'Estrategias': [
            "Conversaciones informales y escucha activa",
            "Reuniones pequeñas con ejemplos concretos",
            "Comunicación incrementada y resolución de dudas",
            "Reconocimiento verbal y recompensas simbólicas",
            "Capacitación breve y participación activa",
            "Intercambio de experiencias exitosas",
            "Anclar nuevos hábitos en la identidad"
        ]
    }
    
    df_etapas = pd.DataFrame(etapas_data)
    
    # Selector de etapa
    etapa_seleccionada = st.selectbox(
        "Selecciona una etapa para ver detalles:",
        options=df_etapas['Etapa'].tolist(),
        index=0
    )
    
    etapa_idx = df_etapas[df_etapas['Etapa'] == etapa_seleccionada].index[0]
    
    # Gráfico de la curva
    st.subheader("📈 Evolución del Equipo a través del Cambio")
    
    fig_curva = go.Figure()
    
    # Línea de la curva
    fig_curva.add_trace(go.Scatter(
        x=df_etapas['Tiempo'],
        y=df_etapas['Nivel_Confianza'],
        mode='lines+markers',
        name='Nivel de Confianza',
        line=dict(color='#EA580C', width=4, shape='spline'),
        marker=dict(size=10, color=df_etapas['Color'], line=dict(width=2, color='white')),
        hovertemplate='<b>%{text}</b><br>Confianza: %{y}%<br>Tiempo: Mes %{x}<extra></extra>',
        text=df_etapas['Etapa']
    ))
    
    # Destacar etapa seleccionada
    fig_curva.add_trace(go.Scatter(
        x=[df_etapas.iloc[etapa_idx]['Tiempo']],
        y=[df_etapas.iloc[etapa_idx]['Nivel_Confianza']],
        mode='markers',
        name='Etapa Actual',
        marker=dict(size=20, color='red', symbol='star'),
        showlegend=False
    ))
    
    # Área bajo la curva
    fig_curva.add_trace(go.Scatter(
        x=df_etapas['Tiempo'],
        y=df_etapas['Nivel_Confianza'],
        fill='tonexty',
        fillcolor='rgba(234, 88, 12, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig_curva.update_layout(
        title="Curva del Cambio de Kübler-Ross - Calzados Nihjardi",
        xaxis_title="Tiempo (Meses)",
        yaxis_title="Nivel de Confianza y Competencia (%)",
        height=500,
        hovermode='closest',
        yaxis=dict(range=[0, 100])
    )
    
    # Añadir anotaciones para cada etapa
    for i, row in df_etapas.iterrows():
        fig_curva.add_annotation(
            x=row['Tiempo'],
            y=row['Nivel_Confianza'] + 8,
            text=row['Etapa'],
            showarrow=False,
            font=dict(size=10, color='black'),
            bgcolor='white',
            bordercolor='gray',
            borderwidth=1
        )
    
    st.plotly_chart(fig_curva, use_container_width=True)
    
    # Detalles de la etapa seleccionada
    st.subheader(f"🔍 Detalle: {etapa_seleccionada}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Nivel de Confianza",
            value=f"{df_etapas.iloc[etapa_idx]['Nivel_Confianza']}%",
            delta=f"Mes {df_etapas.iloc[etapa_idx]['Tiempo']}"
        )
    
    with col2:
        fase = "🔴 Crítica" if etapa_idx < 3 else "🟡 Recuperación" if etapa_idx < 5 else "🟢 Consolidación"
        st.metric(
            label="Fase del Proceso",
            value=fase
        )
    
    with col3:
        progreso = ((etapa_idx + 1) / len(df_etapas)) * 100
        st.metric(
            label="Progreso General",
            value=f"{progreso:.0f}%"
        )
    
    # Información detallada
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **📋 Situación del Equipo**
        
        {df_etapas.iloc[etapa_idx]['Descripcion']}
        """)
        
        st.warning(f"""
        **💬 Frase Típica**
        
        "{df_etapas.iloc[etapa_idx]['Frases_Tipicas']}"
        """)
    
    with col2:
        st.success(f"""
        **🎯 Estrategia Aplicada**
        
        {df_etapas.iloc[etapa_idx]['Estrategias']}
        """)
        
        # Progreso visual
        st.write("**📊 Progreso de la Etapa**")
        progress_bar = st.progress(df_etapas.iloc[etapa_idx]['Nivel_Confianza'] / 100)
    
    # Navegación entre etapas
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Etapa Anterior", disabled=(etapa_idx == 0)):
            st.rerun()
    
    with col2:
        st.write(f"**Etapa {etapa_idx + 1} de {len(df_etapas)}**")
    
    with col3:
        if st.button("Siguiente Etapa ➡️", disabled=(etapa_idx == len(df_etapas) - 1)):
            st.rerun()
    
    # Resumen final si está en la última etapa
    if etapa_idx == len(df_etapas) - 1:
        st.success("""
        ### 🎉 ¡Proceso de Cambio Exitoso!
        
        El equipo de Calzados "Nihjardi" ha completado exitosamente su proceso de transformación organizacional. 
        Los nuevos hábitos y prácticas se han integrado en la cultura empresarial, manteniendo la esencia 
        artesanal mientras se mejora la eficiencia operativa.
        
        **Resultados Finales:**
        - ⏱️ **Tiempo Total:** 6 meses
        - 📈 **Nivel de Integración:** 95%
        - 😊 **Satisfacción del Equipo:** Alta
        - 🎯 **Objetivos Cumplidos:** Exitosamente
        """)

def show_recommendations():
    st.header("💡 Recomendaciones Estratégicas")
    
    # Métricas de éxito proyectadas
    st.subheader("🎯 Proyección de Éxito")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Probabilidad de Éxito",
            value="78%",
            delta="Alto potencial",
            help="Basado en la cohesión del equipo y disposición al cambio"
        )
    
    with col2:
        st.metric(
            label="Tiempo Estimado",
            value="4-6 meses",
            delta="Implementación gradual",
            help="Para consolidar los cambios principales"
        )
    
    with col3:
        st.metric(
            label="Riesgo General",
            value="Bajo",
            delta="Equipo cohesionado",
            help="Debido a la cultura familiar y liderazgo cercano"
        )
    
    # Plan de implementación
    st.subheader("📅 Plan de Implementación")
    
    fases = {
        "🚀 Fase 1: Preparación (Mes 1-2)": {
            "objetivo": "Sensibilización y preparación del equipo",
            "acciones": [
                "Reuniones de sensibilización sobre necesidad del cambio",
                "Formación del equipo guía (propietario + 2 colaboradores clave)",
                "Comunicación clara de la visión del cambio",
                "Identificación de líderes naturales en el equipo"
            ],
            "indicadores": ["Nivel de comprensión del cambio", "Participación en reuniones"]
        },
        "⚙️ Fase 2: Implementación (Mes 2-4)": {
            "objetivo": "Cambios operativos graduales",
            "acciones": [
                "Reorganización física del área de trabajo",
                "Implementación de planificación diaria simple",
                "Capacitación en organización del espacio",
                "Establecimiento de rutinas básicas"
            ],
            "indicadores": ["Tiempo de búsqueda de herramientas", "Cumplimiento de planificación"]
        },
        "🎯 Fase 3: Consolidación (Mes 4-6)": {
            "objetivo": "Anclar cambios en la cultura",
            "acciones": [
                "Rutinas de mantenimiento preventivo",
                "Sistema básico de control de pedidos",
                "Evaluación y ajustes del proceso",
                "Reconocimiento de logros del equipo"
            ],
            "indicadores": ["Adopción de nuevas rutinas", "Satisfacción del equipo"]
        }
    }
    
    for fase, contenido in fases.items():
        with st.expander(fase, expanded=True):
            st.write(f"**🎯 Objetivo:** {contenido['objetivo']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**📋 Acciones:**")
                for accion in contenido['acciones']:
                    st.write(f"• {accion}")
            
            with col2:
                st.write("**📊 Indicadores:**")
                for indicador in contenido['indicadores']:
                    st.write(f"• {indicador}")
    
    # Factores críticos de éxito
    st.subheader("🔑 Factores Críticos de Éxito")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **✅ HACER**
        - Mantener comunicación constante y transparente
        - Involucrar al equipo en las decisiones
        - Reconocer y celebrar pequeños logros
        - Preservar la identidad artesanal
        - Implementar cambios de forma gradual
        - Capacitar antes de implementar
        """)
    
    with col2:
        st.error("""
        **❌ EVITAR**
        - Cambios abruptos o radicales
        - Imposición sin explicación
        - Ignorar las preocupaciones del equipo
        - Perder la esencia artesanal
        - Sobrecargar con muchos cambios
        - Falta de seguimiento y apoyo
        """)
    
    # Conclusión final
    st.subheader("🏆 Conclusión")
    
    st.info("""
    **Calzados "Nihjardi" tiene todas las condiciones para un proceso de cambio exitoso:**
    
    ✅ **Base sólida:** Cultura familiar fuerte y orgullo artesanal  
    ✅ **Liderazgo cercano:** Comunicación abierta con el propietario  
    ✅ **Equipo comprometido:** Alta cohesión y lealtad  
    ✅ **Disposición moderada:** 68% abierto al cambio  
    ✅ **Identidad clara:** Saben qué preservar y qué mejorar  
    
    **El éxito dependerá de mantener el equilibrio entre innovación y tradición, 
    implementando mejoras que fortalezcan la eficiencia sin comprometer 
    la esencia artesanal que los distingue.**
    """)

if __name__ == "__main__":
    main()
