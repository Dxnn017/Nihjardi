"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import EncuestaCalzadosNihjardi from "../encuesta-calzados-nihjardi"
import ResultadosEncuesta from "../resultados-encuesta"
import CurvaKublerRoss from "../curva-kubler-ross"

export default function Page() {
  const [mostrarResultados, setMostrarResultados] = useState(false)
  const [mostrarCurvaKublerRoss, setMostrarCurvaKublerRoss] = useState(false)

  return (
    <div>
      {!mostrarResultados && !mostrarCurvaKublerRoss ? (
        <div>
          <EncuestaCalzadosNihjardi />
          <div className="fixed bottom-4 right-4">
            <Button
              onClick={() => setMostrarResultados(true)}
              className="bg-gradient-to-r from-purple-500 to-indigo-500 hover:from-purple-600 hover:to-indigo-600 shadow-lg"
            >
              Ver Resultados del Diagnóstico
            </Button>
            <Button
              onClick={() => setMostrarCurvaKublerRoss(true)}
              className="ml-2 bg-gradient-to-r from-green-500 to-blue-500 hover:from-green-600 hover:to-blue-600 shadow-lg"
            >
              Ver Curva Kubler-Ross
            </Button>
          </div>
        </div>
      ) : mostrarResultados ? (
        <div>
          <ResultadosEncuesta />
          <div className="fixed bottom-4 right-4">
            <Button onClick={() => setMostrarResultados(false)} variant="outline" className="bg-white shadow-lg">
              Volver a la Encuesta
            </Button>
          </div>
        </div>
      ) : (
        <div>
          <CurvaKublerRoss />
          <div className="fixed bottom-4 right-4">
            <Button onClick={() => setMostrarCurvaKublerRoss(false)} variant="outline" className="bg-white shadow-lg">
              Volver
            </Button>
          </div>
        </div>
      )}
    </div>
  )
}
