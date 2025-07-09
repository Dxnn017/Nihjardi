"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import {
  Zap,
  XCircle,
  Frown,
  TrendingDown,
  Lightbulb,
  CheckCircle,
  Target,
  ArrowRight,
  ArrowLeft,
  Users,
  MessageCircle,
  Award,
  Heart,
} from "lucide-react"

export default function CurvaKublerRoss() {
  const [etapaActiva, setEtapaActiva] = useState(0)

  const etapas = [
    {
      id: 0,
      nombre: "Shock",
      icon: <Zap className="w-6 h-6" />,
      color: "from-yellow-400 to-orange-500",
      bgColor: "bg-yellow-50",
      borderColor: "border-yellow-300",
      nivel: 80, // Cambiado para que esté más arriba
      descripcion:
        "Al momento de comunicar el inicio del proceso de cambio, los colaboradores reaccionaron con sorpresa.",
      detalle:
        "La idea de reorganizar el área de trabajo, implementar rutinas de planificación diaria y registrar actividades generó una sensación inicial de desconcierto.",
      accionEstrategica:
        "Se aplicaron estrategias de contención emocional para reducir la ansiedad, como conversaciones informales y espacios de escucha activa, generando un ambiente de apertura.",
      frases: ["¿Por qué tenemos que cambiar ahora?", "Esto es muy repentino...", "No entiendo qué está pasando"],
      estrategias: [
        "Conversaciones informales",
        "Espacios de escucha activa",
        "Ambiente de apertura",
        "Contención emocional",
      ],
    },
    {
      id: 1,
      nombre: "Negación",
      icon: <XCircle className="w-6 h-6" />,
      color: "from-red-400 to-pink-500",
      bgColor: "bg-red-50",
      borderColor: "border-red-300",
      nivel: 70, // Ajustado
      descripcion: "Algunos trabajadores manifestaron incredulidad sobre la necesidad de cambiar.",
      detalle:
        "Frases como 'así siempre se ha trabajado' o 'no hace falta cambiar nada' reflejaron una resistencia basada en la familiaridad con los métodos tradicionales.",
      accionEstrategica:
        "Se fortalecieron los vínculos personales con el equipo mediante reuniones pequeñas, donde se explicó el motivo del cambio con ejemplos concretos y se ofreció un espacio para expresar preocupaciones.",
      frases: ["Así siempre se ha trabajado", "No hace falta cambiar nada", "Esto no va a funcionar aquí"],
      estrategias: ["Reuniones pequeñas", "Ejemplos concretos", "Vínculos personales", "Espacios de expresión"],
    },
    {
      id: 2,
      nombre: "Frustración",
      icon: <Frown className="w-6 h-6" />,
      color: "from-orange-400 to-red-500",
      bgColor: "bg-orange-50",
      borderColor: "border-orange-300",
      nivel: 45, // Ajustado
      descripcion:
        "A medida que los primeros cambios se implementaban, algunos colaboradores expresaron incomodidad o irritación.",
      detalle:
        "Esta fase se manifestó con actitudes defensivas o baja disposición a colaborar durante el control de tareas y reordenamiento del taller.",
      accionEstrategica:
        "Se incrementó la comunicación formal e informal. El líder del equipo guía reforzó la idea de que el cambio no era una imposición, sino una mejora colectiva.",
      frases: ["Esto es más complicado", "Antes era más fácil", "¿Por qué tanto control?"],
      estrategias: ["Comunicación incrementada", "Mejora colectiva", "Resolución de dudas", "Evitar tensiones"],
    },
    {
      id: 3,
      nombre: "Depresión",
      icon: <TrendingDown className="w-6 h-6" />,
      color: "from-blue-400 to-indigo-500",
      bgColor: "bg-blue-50",
      borderColor: "border-blue-300",
      nivel: 25, // Punto más bajo
      descripcion: "Se detectó un descenso en el ánimo del equipo durante la adaptación a nuevos hábitos.",
      detalle:
        "Algunos colaboradores mostraron desmotivación, cansancio o confusión frente a las nuevas tareas como la planificación diaria y el orden sistemático.",
      accionEstrategica:
        "Se impulsaron acciones motivacionales como el reconocimiento verbal, pequeñas recompensas simbólicas y la validación de los esfuerzos individuales.",
      frases: ["Esto es muy cansado", "No sé si vale la pena", "Me siento confundido"],
      estrategias: [
        "Reconocimiento verbal",
        "Recompensas simbólicas",
        "Validación de esfuerzos",
        "Recordar beneficios",
      ],
    },
    {
      id: 4,
      nombre: "Experimentación",
      icon: <Lightbulb className="w-6 h-6" />,
      color: "from-amber-400 to-yellow-500",
      bgColor: "bg-amber-50",
      borderColor: "border-amber-300",
      nivel: 55, // Subiendo
      descripcion: "El equipo comenzó a probar nuevas formas de trabajo con mayor disposición.",
      detalle:
        "Se mostraron dispuestos a realizar tareas bajo planificación, participar en pequeñas mejoras del entorno y mantener registros básicos.",
      accionEstrategica:
        "Se ofrecieron sesiones breves de capacitación en organización del espacio, mantenimiento preventivo básico y manejo de cronogramas.",
      frases: ["Vamos a intentar esto", "Quizás sí funcione", "Tengo una idea para mejorar"],
      estrategias: ["Capacitación breve", "Participación activa", "Reconocer aprendizaje", "Propuestas de mejora"],
    },
    {
      id: 5,
      nombre: "Decisión",
      icon: <CheckCircle className="w-6 h-6" />,
      color: "from-green-400 to-emerald-500",
      bgColor: "bg-green-50",
      borderColor: "border-green-300",
      nivel: 80, // Alto nivel
      descripcion: "El equipo se encuentra en una etapa de aceptación consciente del nuevo contexto operativo.",
      detalle:
        "Los colaboradores han comprendido cómo manejarse en el nuevo contexto, muestran una actitud más abierta y comparten prácticas útiles entre ellos.",
      accionEstrategica:
        "Se ha promovido el intercambio de experiencias exitosas entre compañeros y se han establecido rutinas estables de trabajo.",
      frases: ["Ahora entiendo cómo funciona", "Esto realmente nos ayuda", "Podemos hacerlo mejor"],
      estrategias: ["Intercambio de experiencias", "Rutinas estables", "Sensación de control", "Reconocer avances"],
    },
    {
      id: 6,
      nombre: "Integración",
      icon: <Target className="w-6 h-6" />,
      color: "from-purple-400 to-violet-500",
      bgColor: "bg-purple-50",
      borderColor: "border-purple-300",
      nivel: 95, // Nivel máximo
      descripcion: "Los nuevos comportamientos y hábitos están comenzando a formar parte de la cultura organizacional.",
      detalle:
        "La empresa mantiene su esencia artesanal, pero incorpora prácticas modernas que mejoran su desempeño. El lenguaje organizacional ha cambiado.",
      accionEstrategica:
        "Se está trabajando en anclar los nuevos hábitos en la identidad de la empresa. El equipo guía continúa reforzando estos valores mediante el ejemplo.",
      frases: ["Así es como trabajamos ahora", "Esto es parte de nosotros", "Hemos mejorado mucho"],
      estrategias: ["Anclar nuevos hábitos", "Reforzar valores", "Acompañamiento cercano", "Ejemplo del liderazgo"],
    },
  ]

  const etapaActual = etapas[etapaActiva]

  const siguienteEtapa = () => {
    if (etapaActiva < etapas.length - 1) {
      setEtapaActiva(etapaActiva + 1)
    }
  }

  const etapaAnterior = () => {
    if (etapaActiva > 0) {
      setEtapaActiva(etapaActiva - 1)
    }
  }

  // Función para crear la curva suave
  const createSmoothCurve = () => {
    const points = etapas.map((etapa, index) => ({
      x: (index / (etapas.length - 1)) * 90 + 5, // Margen del 5% a cada lado
      y: 90 - etapa.nivel * 0.8, // Invertir Y y escalar al 80% del alto
    }))

    let path = `M ${points[0].x} ${points[0].y}`

    for (let i = 1; i < points.length; i++) {
      const prevPoint = points[i - 1]
      const currentPoint = points[i]
      const controlPoint1X = prevPoint.x + (currentPoint.x - prevPoint.x) * 0.5
      const controlPoint1Y = prevPoint.y
      const controlPoint2X = prevPoint.x + (currentPoint.x - prevPoint.x) * 0.5
      const controlPoint2Y = currentPoint.y

      path += ` C ${controlPoint1X} ${controlPoint1Y}, ${controlPoint2X} ${controlPoint2Y}, ${currentPoint.x} ${currentPoint.y}`
    }

    return { path, points }
  }

  const { path, points } = createSmoothCurve()

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-amber-50 to-orange-50 p-4">
      {/* Header */}
      <div className="bg-gradient-to-r from-amber-600 via-orange-600 to-red-600 text-white py-6 px-4 rounded-lg mb-6">
        <div className="max-w-6xl mx-auto text-center">
          <h1 className="text-3xl font-bold mb-2">Curva del Cambio de Kübler-Ross</h1>
          <p className="text-amber-100 text-lg">
            Aplicada en Calzados "Nihjardi" - Proceso de Transformación Organizacional
          </p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto">
        {/* Progreso general */}
        <Card className="mb-6 bg-white/80 backdrop-blur">
          <CardContent className="pt-6">
            <div className="flex justify-between items-center mb-3">
              <span className="text-sm font-medium text-gray-700">Progreso del Proceso de Cambio</span>
              <span className="text-sm font-bold text-orange-600">
                Etapa {etapaActiva + 1} de {etapas.length}: {etapaActual.nombre}
              </span>
            </div>
            <Progress value={((etapaActiva + 1) / etapas.length) * 100} className="h-3 bg-gray-200" />
          </CardContent>
        </Card>

        {/* Visualización de la curva */}
        <Card className="mb-6 bg-white shadow-xl">
          <CardHeader>
            <CardTitle className="text-center text-xl">📈 Evolución del Equipo a través del Cambio</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="relative h-80 bg-gradient-to-br from-gray-50 to-gray-100 rounded-lg p-6">
              {/* Ejes */}
              <div className="absolute bottom-6 left-6 right-6 h-px bg-gray-400"></div>
              <div className="absolute bottom-6 left-6 top-6 w-px bg-gray-400"></div>

              {/* Labels de ejes */}
              <div className="absolute bottom-2 right-6 text-sm text-gray-600 font-medium">Tiempo</div>
              <div className="absolute top-6 left-2 text-sm text-gray-600 font-medium transform -rotate-90 origin-left">
                Confianza y Competencia
              </div>

              {/* Grid lines */}
              <div className="absolute inset-6">
                {[25, 50, 75].map((percent) => (
                  <div
                    key={percent}
                    className="absolute w-full h-px bg-gray-200"
                    style={{ bottom: `${percent * 0.8}%` }}
                  />
                ))}
              </div>

              {/* SVG para la curva */}
              <svg className="absolute inset-6 w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
                {/* Área bajo la curva */}
                <path d={`${path} L 95 90 L 5 90 Z`} fill="url(#gradient)" opacity="0.2" />

                {/* Línea de la curva */}
                <path d={path} stroke="#EA580C" strokeWidth="3" fill="none" className="drop-shadow-sm" />

                {/* Puntos en la curva */}
                {points.map((punto, index) => (
                  <circle
                    key={index}
                    cx={punto.x}
                    cy={punto.y}
                    r={index === etapaActiva ? "2.5" : "1.5"}
                    fill={index === etapaActiva ? "#DC2626" : "#EA580C"}
                    className={`cursor-pointer transition-all ${index === etapaActiva ? "animate-pulse" : ""}`}
                    onClick={() => setEtapaActiva(index)}
                    style={{ filter: "drop-shadow(0 2px 4px rgba(0,0,0,0.3))" }}
                  />
                ))}

                {/* Gradiente para el área */}
                <defs>
                  <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stopColor="#EA580C" stopOpacity="0.3" />
                    <stop offset="100%" stopColor="#EA580C" stopOpacity="0.1" />
                  </linearGradient>
                </defs>
              </svg>

              {/* Etiquetas de etapas */}
              {etapas.map((etapa, index) => {
                const punto = points[index]
                return (
                  <div
                    key={index}
                    className={`absolute text-xs font-medium cursor-pointer transition-all transform -translate-x-1/2 ${
                      index === etapaActiva ? "text-red-600 font-bold scale-110" : "text-gray-600"
                    }`}
                    style={{
                      left: `${punto.x}%`,
                      top: `${punto.y * 0.8 + 6}%`,
                    }}
                    onClick={() => setEtapaActiva(index)}
                  >
                    <div className="bg-white px-2 py-1 rounded shadow-sm border">{etapa.nombre}</div>
                  </div>
                )
              })}
            </div>
          </CardContent>
        </Card>

        {/* Navegación por etapas */}
        <div className="grid grid-cols-7 gap-2 mb-6">
          {etapas.map((etapa, index) => (
            <Button
              key={index}
              variant={index === etapaActiva ? "default" : "outline"}
              size="sm"
              onClick={() => setEtapaActiva(index)}
              className={`flex flex-col items-center p-3 h-auto transition-all ${
                index === etapaActiva
                  ? `bg-gradient-to-r ${etapa.color} text-white shadow-lg scale-105`
                  : "hover:bg-gray-50 hover:scale-102"
              }`}
            >
              {etapa.icon}
              <span className="text-xs mt-1">{etapa.nombre}</span>
            </Button>
          ))}
        </div>

        {/* Detalle de la etapa actual */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Información principal */}
          <Card className={`lg:col-span-2 ${etapaActual.bgColor} ${etapaActual.borderColor} border-l-8`}>
            <CardHeader>
              <div className="flex items-center gap-4">
                <div className={`p-4 rounded-full bg-gradient-to-r ${etapaActual.color} text-white shadow-lg`}>
                  {etapaActual.icon}
                </div>
                <div>
                  <CardTitle className="text-2xl text-gray-800">{etapaActual.nombre}</CardTitle>
                  <Badge className={`mt-2 bg-gradient-to-r ${etapaActual.color} text-white`}>
                    Nivel de Confianza: {etapaActual.nivel}%
                  </Badge>
                </div>
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="bg-white/70 p-4 rounded-lg">
                <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                  <Users className="w-4 h-4" />
                  Situación del Equipo
                </h4>
                <p className="text-gray-700 leading-relaxed">{etapaActual.descripcion}</p>
                <p className="text-gray-600 text-sm mt-2 italic">{etapaActual.detalle}</p>
              </div>

              <div className="bg-white/70 p-4 rounded-lg">
                <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                  <Target className="w-4 h-4" />
                  Acción Estratégica Implementada
                </h4>
                <p className="text-gray-700 leading-relaxed">{etapaActual.accionEstrategica}</p>
              </div>

              <div className="bg-white/70 p-4 rounded-lg">
                <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
                  <MessageCircle className="w-4 h-4" />
                  Frases Típicas de esta Etapa
                </h4>
                <div className="space-y-2">
                  {etapaActual.frases.map((frase, index) => (
                    <div
                      key={index}
                      className="bg-gray-100 p-3 rounded-lg italic text-gray-600 text-sm border-l-4 border-orange-300"
                    >
                      "{frase}"
                    </div>
                  ))}
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Panel lateral */}
          <div className="space-y-4">
            {/* Estrategias aplicadas */}
            <Card className="bg-white shadow-lg">
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Award className="w-5 h-5 text-orange-600" />
                  Estrategias Aplicadas
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  {etapaActual.estrategias.map((estrategia, index) => (
                    <div
                      key={index}
                      className="flex items-center gap-2 p-3 bg-orange-50 rounded-lg border border-orange-100"
                    >
                      <CheckCircle className="w-4 h-4 text-green-600 flex-shrink-0" />
                      <span className="text-sm text-gray-700">{estrategia}</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Nivel de progreso */}
            <Card className="bg-white shadow-lg">
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Heart className="w-5 h-5 text-red-600" />
                  Estado del Equipo
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div>
                    <div className="flex justify-between text-sm mb-2">
                      <span className="font-medium">Confianza</span>
                      <span className="font-bold">{etapaActual.nivel}%</span>
                    </div>
                    <Progress value={etapaActual.nivel} className="h-3" />
                  </div>

                  <div>
                    <div className="flex justify-between text-sm mb-2">
                      <span className="font-medium">Progreso General</span>
                      <span className="font-bold">{Math.round(((etapaActiva + 1) / etapas.length) * 100)}%</span>
                    </div>
                    <Progress value={((etapaActiva + 1) / etapas.length) * 100} className="h-3" />
                  </div>

                  <div className="mt-4 p-4 bg-gradient-to-r from-orange-50 to-amber-50 rounded-lg border border-orange-200">
                    <div className="text-sm font-bold text-orange-800">
                      {etapaActiva < 3
                        ? "🔴 Fase Crítica"
                        : etapaActiva < 5
                          ? "🟡 Fase de Recuperación"
                          : "🟢 Fase de Consolidación"}
                    </div>
                    <div className="text-xs text-orange-600 mt-1">
                      {etapaActiva < 3
                        ? "Requiere atención especial y apoyo constante"
                        : etapaActiva < 5
                          ? "Progreso positivo, mantener el impulso"
                          : "Cambio exitoso, consolidar logros"}
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        {/* Navegación */}
        <div className="flex justify-between items-center mt-8">
          <Button
            variant="outline"
            onClick={etapaAnterior}
            disabled={etapaActiva === 0}
            className="flex items-center gap-2 bg-white hover:bg-gray-50"
          >
            <ArrowLeft className="w-4 h-4" />
            Etapa Anterior
          </Button>

          <div className="text-center">
            <div className="text-sm text-gray-600 font-medium">
              Etapa {etapaActiva + 1} de {etapas.length}
            </div>
            <div className="text-xs text-gray-500">{etapaActual.nombre}</div>
          </div>

          <Button
            onClick={siguienteEtapa}
            disabled={etapaActiva === etapas.length - 1}
            className="flex items-center gap-2 bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-600 hover:to-red-600"
          >
            Siguiente Etapa
            <ArrowRight className="w-4 h-4" />
          </Button>
        </div>

        {/* Resumen final */}
        {etapaActiva === etapas.length - 1 && (
          <Card className="mt-8 bg-gradient-to-r from-green-50 to-emerald-50 border-2 border-green-200 shadow-xl">
            <CardContent className="pt-8 pb-8">
              <div className="text-center">
                <div className="bg-gradient-to-r from-green-500 to-emerald-500 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 shadow-lg">
                  <Target className="w-10 h-10 text-white" />
                </div>
                <h3 className="text-3xl font-bold text-green-800 mb-4">¡Proceso de Cambio Exitoso!</h3>
                <p className="text-green-700 text-lg max-w-4xl mx-auto leading-relaxed mb-6">
                  El equipo de Calzados "Nihjardi" ha completado exitosamente su proceso de transformación
                  organizacional. Los nuevos hábitos y prácticas se han integrado en la cultura empresarial, manteniendo
                  la esencia artesanal mientras se mejora la eficiencia operativa.
                </p>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
                  <div className="bg-white/80 p-6 rounded-lg shadow-sm">
                    <div className="font-bold text-green-700 text-lg">Tiempo Total</div>
                    <div className="text-3xl font-bold text-green-800">6 meses</div>
                    <div className="text-green-600 text-sm mt-1">Implementación gradual</div>
                  </div>
                  <div className="bg-white/80 p-6 rounded-lg shadow-sm">
                    <div className="font-bold text-green-700 text-lg">Nivel de Integración</div>
                    <div className="text-3xl font-bold text-green-800">95%</div>
                    <div className="text-green-600 text-sm mt-1">Altamente exitoso</div>
                  </div>
                  <div className="bg-white/80 p-6 rounded-lg shadow-sm">
                    <div className="font-bold text-green-700 text-lg">Satisfacción del Equipo</div>
                    <div className="text-3xl font-bold text-green-800">Alta</div>
                    <div className="text-green-600 text-sm mt-1">Compromiso consolidado</div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  )
}
