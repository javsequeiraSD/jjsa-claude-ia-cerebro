# CONTEXTO.md v8.0 — Proyecto Mando Central / Sivar Dogs
**CEO:** José Javier Sequeira | **Fecha última actualización:** 22/03/2026 | **Sprint:** 2

---

## 1. IDENTIDAD DEL PROYECTO

**Empresa:** Sivar Dogs S.A. de C.V.
**Punto de venta:** Parque San Martín, Santa Tecla, El Salvador
**Fundada:** 2018 | **Operación:** Lunes–Sábado
**Vendedora:** Vilma Luna (reportes diarios por WhatsApp)
**Equipo:** Daysi Rivas (operaciones auxiliar), Doris Rivas (producción)

**Objetivo del ecosistema:** Construir "Mando Central" — visibilidad y control CEO-level sobre todas las operaciones de Sivar Dogs, integrado con un futuro SaaS y holding personal.

---

## 2. ESTADO DEL ECOSISTEMA — SPRINT 1 COMPLETADO (13–22 mar 2026)

### 2.1 Documentos maestros vigentes

| # | Archivo | Versión | Rol |
|---|---------|---------|-----|
| 1 | Manual_Operaciones_Claude_IA.docx | v1.3 | FUENTE DE VERDAD — 8 capítulos |
| 2 | ReglasDelSistema_SivarDogs.docx | v5.1 | 29 reglas operativas canónicas |
| 3 | CONTEXTO.md | **v8.0** | Puente entre conversaciones |
| 4 | Explicaciones_SivarDogs.docx | v1.4 | Contexto + glosario + flujo + POS |
| 5 | Spec_ReporteCierre_SivarDogs.docx | v2.0 | Para Claude Code |
| 6 | ResumenEjecutivo_SivarDogs.docx | v3.0 | Estado del proyecto |
| 7 | motor_reportes.py | v5.1 | Motor de cálculo + reportes PDF |
| 8 | Historico_SivarDogs.xlsx | — | 464 días, 3 hojas |
| 9 | historico_v2.csv | — | 464 registros crudos para Python |
| 10 | Reporte_Historico_SivarDogs_v3.pdf | v3 | Reporte formal CEO/inversores |
| 11 | ReporteSprint1_AgenteGerencial.docx | v1 | Reporte ejecutivo Sprint 1 |

**Ruta local:** `C:\Users\HP\OneDrive\LAPTOP\SIVAR DOGS\GERENCIA\AGENTE GERENCIAL\`

---

## 3. LOS TRES CHATS DEL PROYECTO

### CHAT 1 — Excel Finanzas / Módulo B1 Agente Gerencial
**Estado:** 🔴 PENDIENTE — NO iniciado
**Archivos a adjuntar:** CONTEXTO.md + Finanzas_2026.xlsm + SivarDogs_Control_Operativo.xlsx

**Agenda completa (8 temas identificados):**
1. Diseño del Módulo B1 de Finanzas dentro del Agente Gerencial
2. Estructura de Finanzas_2026.xlsm — hojas, campos, fórmulas existentes
3. Cómo los cierres diarios del motor alimentan el P&L mensual
4. Integración del concilio diario con el módulo financiero
5. Tratamiento contable de brechas: sobrantes = "Otros Ingresos no identificados", faltantes = "Diferencias de Caja"
6. Punto de equilibrio del negocio — cálculo y seguimiento mensual
7. Salarios, préstamos y alquileres fijos — estructura en el Excel
8. Proyecciones basadas en el histórico de 15 meses

**Contexto financiero crítico:** Situación actual requiere saneamiento. Hay préstamos, salarios y alquileres fijos activos. Los días típicos (30–40 HD) están por debajo del punto de equilibrio. El sábado 15/03/2026 fue excepcional con 222 HD y $440 en ventas.

---

### CHAT 2 — Cortes Diarios Sivar Dogs ✅ SPRINT 1 COMPLETADO
**Estado:** 🟢 ACTIVO — Motor v5.1 funcionando
**Archivos a adjuntar:** CONTEXTO.md + motor_reportes.py

**Semana oficial Lun 16 – Sáb 21 marzo 2026:**

| Día | HD | Venta Real | Concilio | Brecha | Semáforo |
|-----|----|-----------|---------|----|---------|
| Lun 16 | 114 | $220.24 | $215.75 | +$4.49 | 🟢 |
| Mar 17 | 44 | $81.45 | $78.75 | +$2.70 | 🟢 |
| Mié 18 | 48 | $95.65 | $90.25 | +$5.40 | 🟡 |
| Jue 19 | 44 | $75.75 | $77.25 | −$1.50 | 🟢 |
| Vie 20 | 53 | $98.50 | $99.50 | −$1.00 | 🟢 |
| Sáb 21 | 93 | $171.80 | $169.75 | +$2.05 | 🟢 |
| **TOTAL** | **396** | **$743.39** | **$731.25** | **+$12.14** | 🟠 |

**Hallazgos pendientes con Vilma:**
- Mié 18: Combo Especialidad descartado por falta de lays — ¿se cobró parcialmente?
- Jue 19: 2 tickets HD sin respaldo físico — ¿devolución o error?
- Vie 20: 1 HD + 3 sodas ticket sin inventario — ¿confirmar causa?

**Pendientes técnicos Sprint 2:**
- Automatizar flujo WhatsApp → motor → PDF sin intervención manual
- Módulo CIERRE en Google Sheets con reglas motor v5.1

---

### CHAT 3 — Histórico de Venta ✅ COMPLETADO
**Estado:** 🟢 DATOS ESTRUCTURADOS — Análisis profundo pendiente
**Archivos a adjuntar:** CONTEXTO.md + Historico_SivarDogs.xlsx + historico_v2.csv

#### Qué se hizo:
- Chat de WhatsApp exportado y parseado en Python
- 464 registros extraídos y normalizados (16/12/2024 al 18/03/2026)
- Generados: `historico_v2.csv`, `Historico_SivarDogs.xlsx` (3 hojas), `Reporte_Historico_SivarDogs_v3.pdf` (6 páginas)
- El PDF pasó por v1 → v2 (corrección overflow) → v3 (rediseño responsive con proporciones relativas)

#### KPIs históricos oficiales:

| KPI | Valor |
|-----|-------|
| Período | 16/12/2024 – 18/03/2026 |
| Días operados | 464 |
| Hotdogs ticketeados | 28,321 |
| Total productos vendidos | 37,024 |
| Ingreso ticketeado total | $54,186 |
| Ingreso solo hotdogs | $46,980 (87%) |
| Promedio HD/día | 61.0 |
| Ingreso promedio/día | $116.77 |
| Mejor mes (promedio) | Dic 2024 — 82.9 HD/día, $153.36/día |
| Peor mes (promedio) | Feb 2025 — 45.7 HD/día, $89.14/día |
| Récord absoluto | 188 HD el 14/03/2026 (Sábado) |
| Mejor día de semana | **Lunes** — 78.9 HD avg (supera al sábado: 77.1) |

#### Mix de productos histórico:

| Producto | Unidades | % | Ingreso |
|----------|---------|---|---------|
| Clásico | 22,731 | 69.4% | $34,097 |
| Soda individual | 4,278 | 13.1% | $4,278 |
| Chilidog | 3,161 | 9.6% | $6,322 |
| Combo Clásico | 1,923 | 5.9% | $5,288 |
| Chickedog | 297 | 0.9% | $594 |
| Combo Especialidad | 209 | 0.6% | $679 |
| Lays individual | 109 | 0.3% | $55 |
| Alitas | 52 | 0.2% | $208 |

**HD en combos:** 2,132 | **Sodas totales (incl. combos):** 6,410

#### Hallazgos clave del histórico:
- **Chilidog:** creció 4.5x en un año (162u Q4-2024 → 737u Q4-2025). Ya es el 10% del mix.
- **Lunes vs Sábado:** el lunes supera al sábado en promedio — patrón poco convencional para un restaurante en parque. Posiblemente actividades regulares del Parque.
- **Efecto diciembre:** Dic 2024 y Dic 2025 son los mejores meses. Dic 2025 ($4,142) superó a Dic 2024 ($3,374) en 22.8% — crecimiento anual comprobado.
- **Alerta mayo–octubre 2025:** gastos se acercan peligrosamente a ventas ticketeadas. En octubre 2025 prácticamente se cruzan. Señal que el Módulo B1 de Finanzas debe detectar automáticamente.
- **Concentración:** 70.9% de los días en rango 40–80+ HD, generando el 79.5% del volumen.

#### Análisis pendientes para Chat 3 (no ejecutados aún):
1. Punto de equilibrio histórico — ¿cuántos HD/día para cubrir costos fijos?
2. Estacionalidad con significancia estadística
3. Proyección de crecimiento del Chilidog y su impacto en ticket promedio
4. Comparativo año 1 (Dic24–Nov25) vs año 2 (Dic25–Mar26)
5. Análisis de días excepcionales — ¿qué tienen en común los días >100 HD?
6. Meta diaria realista por día de semana (percentil 75 histórico)
7. Impacto de combos en el ticket promedio
8. Análisis de sodas y lays — correlación con volumen de hotdogs
9. Dashboard interactivo de tendencias para el Agente Gerencial

---

## 4. REGLAS CRÍTICAS DEL MOTOR (motor_reportes.py v5.1)

**Input:** 10 campos crudos de WhatsApp
**Output:** PDF diario verificado automáticamente

### Fórmula Venta Real (validada Sáb 15/03/2026 = $440.00):
```
Venta Real = Corte Efectivo + POS + PedidosYa + Transferencias + Gastos − Vuelto Inicial
Corte Efectivo = Efectivo Enviado + Vuelto Final
```

### Fórmula Concilio:
```
Concilio = Tickets ($) + No Ticketeados ($) = Venta Oficial
Brecha = Venta Real − Concilio
```

### Jerarquía de verdad:
1. Caja real (verdad financiera)
2. Inventario (verificador de cantidad)
3. Ticket (verificador de composición — referencia, no verdad)

### Semáforo de brecha:
- Sobrante: 🟢 $0–$5 | 🟡 $5–$10 | 🟠 $10–$15 | 🔴 >$15
- Faltante: 🟡 $0–$5 | 🟠 $5–$10 | 🔴 >$10 (siempre más grave que sobrante)

### Regla Pan = Salchicha:
- Pan Sanfran vendido = Salchicha Jumbo vendida SIEMPRE
- Diff ≤ 2 = marginal | Diff > 2 = hallazgo crítico inmediato
- Excepción: Básico usa Pan Única + Sal Mini Jumbo

### Precios oficiales:
| Producto | Precio | Nota |
|----------|--------|------|
| Clásico | $1.50 | Motor del negocio |
| Chilidog / Chickedog | $2.00 | |
| Combo Clásico | $2.75 | Precio único — NUNCA desglosar |
| Combo Especialidad | $3.25 | NUNCA con Básico |
| Soda individual | $1.00 | |
| Lays individual | $0.50 | Solo con ticket explícito |
| **Lays sin ticket** | **$0.25** | **NUEVA REGLA 21/03/2026** |
| Flanes | $0.65 | |
| Alitas | $4.00 | |

### Empaques:
- Pan Sanfran = 12u/bolsa | Pan Única = 10u/bolsa
- Salchicha Jumbo = 16u/paquete | Salchicha Mini Jumbo = 24u/paquete

---

## 5. ARQUITECTURA DEL ECOSISTEMA

### Agentes activos:
| Agente | Herramienta | Estado |
|--------|-------------|--------|
| Agente 1 Gerencial | Claude Code | En construcción |
| Agente 2 Financiero-Contable-Fiscal | Antigravity | MVP local — pendiente Railway |
| Agente 3 POS | Antigravity/Vercel | En producción (sivar-control.vercel.app) |
| Agentes 4–7 | — | Pendiente creación |

### Sala de Mando:
- URL: sivar-dogs-sala-de-mando.vercel.app
- Backend: Firebase Firestore (proyecto: sivar-dogs-gerencia)
- **REGLA:** Firebase es SOLO para modelo SaaS / CEO data. Google Sheets se mantiene para POS.

### Sprint 2 objetivos:
1. Crear carpeta CLAUDE_AI en OneDrive como puente Claude.ai ↔ Claude Code
2. Deploy Agente 2 a Railway
3. Firebase Auth en Sala de Mando (reemplazar PIN expuesto)
4. Módulo B1 Finanzas en Agente Gerencial
5. Automatizar flujo WhatsApp → motor → PDF

---

## 6. PROTOCOLO DE USO DE CLAUDE

### Al iniciar cualquier conversación de trabajo:
1. Adjuntar este CONTEXTO.md
2. Adjuntar el archivo principal del tema (motor.py, Excel, CSV)
3. Indicar objetivo de la sesión
4. Al cerrar: pedir actualización de memoria y CONTEXTO.md
5. Descargar TODOS los archivos generados antes de cerrar

### Regla estándar:
> TODO cálculo financiero ejecutado por el motor, NUNCA el humano en el chat.
> Input = 10 campos crudos de WhatsApp. Output = PDF verificado automáticamente.

### Protocolo de actualización de documentos (en orden):
1. Memoria → 2. motor_reportes.py → 3. ReglasDelSistema → 4. Manual → 5. Spec → 6. ResumenEjecutivo → 7. Explicaciones → 8. CONTEXTO.md

### Distribución de chats:
- **Claude.ai:** Estrategia, diseño, análisis, documentos, CONTEXTO.md
- **Claude Code:** Construcción, implementación, modificación de archivos
- **Antigravity:** Agentes definidos — lee CONTEXTO.md + tasks.md

---

## 7. CONTEXTO FINANCIERO DEL NEGOCIO

- **Situación:** Requiere saneamiento activo
- **Compromisos fijos:** préstamos, salarios, alquileres
- **Días típicos:** 30–40 HD (bajo punto de equilibrio estimado)
- **Días buenos:** 60–80 HD
- **Días excepcionales:** >100 HD (recurrentes en lunes y sábados)
- **Fuente para PE:** histórico WhatsApp + Finanzas_2026.xlsm
- **Proyección conservadora anual** (base 12 meses Abr25–Mar26):
  - 21,240 HD/año | $40,644 ingresos | $116.77/día promedio
- **Escenario optimista (+15%):** 24,426 HD/año | $46,741 ingresos

---

*CONTEXTO.md v8.0 — 22 marzo 2026 — Sivar Dogs · Proyecto Mando Central*
*Próxima versión: v9.0 al cierre del Sprint 2*
