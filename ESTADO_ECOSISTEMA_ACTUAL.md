# ESTADO ECOSISTEMA ACTUAL — Inversiones JJSA / Sivar Dogs
> Archivo vivo mantenido por Claude Code | Actualizado: 2026-03-27
> Complementa CONTEXTO_v8_1.md con el estado real post-sprint
> Claude Code actualiza este archivo al cerrar cada sprint

---

## ⚠️ CORRECCIONES CRÍTICAS vs CONTEXTO_v8_1.md

El CONTEXTO_v8_1.md tiene errores que deben corregirse en la próxima sesión de Claude.ai:

| Campo | CONTEXTO_v8_1.md dice | Realidad actual |
|-------|----------------------|-----------------|
| Numeración agentes | A2=Financiero, A3=POS | **A2=POS Integral, A3=Financiero** |
| Tecnología Sala de Mando | Firebase Firestore | **Vercel (archivos estáticos) — NO Firebase** |
| DTEs procesados | 1,541 / $44,815.94 | **2,170 DTEs / $64,205.65** |
| Agente 1 % | 48% | **57% (post-S011)** |
| Agente 2 POS % | 64% | **90% (post-S010, prueba real validada)** |
| Reportes | 8 pendientes docx | **7 reportes HTML en producción en Vercel + 1 brief HTML** |
| Sprint en curso | Sprint 2 (nomenclatura Claude.ai) | **S012 (nomenclatura Claude Code)** |
| CEREBRO IA | Carpeta OneDrive fragmentada | **Repo git C:\Users\HP\CLAUDE.IA\ + GitHub javsequeiraSD/jjsa-claude-ia-cerebro** |

---

## Equivalencia de nomenclatura de sprints

Claude.ai y Claude Code usan nomenclaturas distintas para los mismos períodos:

| Claude.ai | Claude Code | Período | Estado |
|-----------|-------------|---------|--------|
| Sprint 1 | S001–S010 | 13–22 mar 2026 | ✅ Completado |
| Sprint 2 | S011 | 27 mar 2026 | ✅ Completado |
| Sprint 2 (cont.) | S012 | Abierto | 🟡 En curso |

---

## Estado de los 8 Agentes (post-S011 — 2026-03-27)

| # | Agente | Herramienta | % | Estado |
|---|--------|-------------|---|--------|
| 1 | Gerencial (Sala de Mando) | Claude Code | **57%** | En construcción — S012 abierto |
| 2 | POS Integral | Claude Code | **90%** | **EN PRODUCCIÓN** — prueba real validada |
| 3 | Financiero-Contable-Fiscal | Claude Code Python | **35%** | Funcional local — deploy Railway pendiente |
| 4 | Project Manager | Antigravity | **33%** | Base lista |
| 5 | Marketing | — | 0% | Por crear |
| 6 | Pedidos Aquí | — | 0% | Por crear |
| 7 | Inventario | — | 0% | Por crear |
| 8 | Tienda en Línea | — | 0% | Por crear |

**`pct_activos` (Agentes 1-4) = 56%** ← métrica primaria CEO
**`ecosistema_pct` (los 8) = 58%** ← referencia estratégica

---

## URLs en Producción

| Sistema | URL | PIN | Estado |
|---------|-----|-----|--------|
| Sala de Mando (A1) | https://sivar-dogs-sala-de-mando.vercel.app/ | 150818 | ✅ Activo |
| POS Integral (A2) | https://sivar-control.vercel.app/ | 0001 Vilma / 0000·0004 Admin | ✅ Activo |
| Financiero (A3) | http://localhost:5000 | — | 🟡 Solo local |
| GitHub Sala de Mando | https://github.com/javsequeiraSD/sivar-dogs-sala-de-mando | — | ✅ Activo |
| GitHub CEREBRO IA | https://github.com/javsequeiraSD/jjsa-claude-ia-cerebro | — | ✅ Activo |

---

## CEREBRO IA — Estado al 2026-03-27

### Ubicación del repo git (fuera de OneDrive para evitar conflicto Drive/.git)
```
C:\Users\HP\CLAUDE.IA\         ← repo git LOCAL (fuera de OneDrive)
GitHub: javsequeiraSD/jjsa-claude-ia-cerebro
```

### Historia del CEREBRO IA (sesiones no registradas en bitácora)

**Sesión 22-mar-2026 (registrada parcialmente):**
- Se creó el repo GitHub `jjsa-claude-ia-cerebro`
- Se estableció el flujo: CLAUDE.IA → GitHub ← Claude.ai (raw URLs)
- Se detectó que los documentos en el repo original estaban incompletos
- Se copió CEREBRO COMPLETO IA → CLAUDE.IA (fuera de OneDrive para evitar conflicto)
- Último commit de esa sesión: `da5cd09` "estructura limpia — PDFs y docx solo en Reportes/"

**Sesión 26-mar-2026 (PERDIDA — terminal cerrado sin guardar):**
- Se analizaron 3 carpetas: CEREBRO IA (OneDrive), CEREBRO COMPLETO IA, 🧠 AGENTE GERENCIAL.IA
- Se encontró mal etiquetado en Manual de Operaciones: v1_3 desactualizado, v1_4 es punto 9 no punto 8
- Se identificó que los documentos tienen info válida en distintas versiones con posible duplicidad
- Sesión terminó sin ejecutar consolidación → trabajo perdido

**Sesión 27-mar-2026 (esta sesión, sprint S012):**
- Se confirmó repo CLAUDE.IA como repositorio único y fuente de verdad del CEREBRO IA
- Se hizo `.gitignore` para `~$*` (archivos temp Office)
- Se commitearon 36 archivos históricos → todos los documentos ahora en git
- Commit: `954c08b` "sync: archivo completo CEREBRO IA — todos los documentos históricos"
- Se extrajeron y leyeron todos los `.docx` con python-docx
- Se actualizó este ESTADO con el contexto completo de ambos mundos (Claude.ai + Claude Code)

### Documentos en CLAUDE.IA (inventario completo al 2026-03-27)

**Documentos VIGENTES (versión final):**
| Archivo | Versión | Propósito |
|---------|---------|-----------|
| CONTEXTO_v8_1.md | v8.1 | Puente Claude.ai ↔ trabajo (tiene errores — ver tabla correcciones) |
| ESTADO_ECOSISTEMA_ACTUAL.md | — | Este archivo — mantenido por Claude Code |
| IdentidadAgenteGerencial.md | v1.0 | Identidad, auditoría interna y roadmap estratégico del agente |
| Manual_Operaciones_Claude_IA.docx | v1.2 (texto) | Bitácora — Capítulos 1-8 |
| Manual_Operaciones_Claude_IA_v1_4_addendum.docx | v1.4 | Capítulo 9 — Sistema de Reportería 8 roles |
| ReglasDelSistema_SivarDogs_v5_1.docx | v5.1 | 29 reglas operativas canónicas |
| Explicaciones_SivarDogs_v1_4.docx | v1.4 | Contexto, glosario, flujo |
| Spec_ReporteCierre_SivarDogs_v2.docx | v2.0 | Spec técnica para Claude Code |
| ResumenEjecutivo_SivarDogs_v3.docx | v3.0 | Estado del proyecto |
| Reporte_Auditoria_SivarDogs_v1_0.docx | v1.0 | Auditoría 4 áreas — Sprint 1 |
| ReporteSprint1_AgenteGerencial_SivarDogs.docx | v1 | Reporte ejecutivo Sprint 1 |
| motor_reportes.py | v5.1 | Motor de cálculo + PDFs diarios (39KB) |
| historico_v2.csv | — | 464 registros históricos limpios |
| Historico_SivarDogs.xlsx | — | 464 días, 3 hojas |
| SivarDogs_Control_Operativo.xlsx | — | Control operativo |
| SivarDogs_Control_Operativo MICROSOFT.xlsx | — | Versión Microsoft del control operativo |

**Documentos HISTÓRICOS (en git, a archivar en próxima sesión Claude.ai):**
- Manual_Operaciones_Claude_IA_v1_3.docx → DESACTUALIZADO (puntos 1-7 del manual, superado por la versión sin número)
- Explicaciones_SivarDogs.docx, v1_1, v1_2, v1_3 → versiones antiguas
- ReglasDelSistema_SivarDogs.docx, v2, v3, v4, v4_1, v5 → versiones antiguas (la vigente es v5_1)
- ResumenEjecutivo_SivarDogs.docx, v2 → versiones antiguas
- Spec_ReporteCierre_SivarDogs.docx → versión antigua
- CONTEXTO_v7.md, CONTEXTO_v8.md → versiones antiguas
- Todos los PDFs de reportes diarios y semanales → en Reportes/

---

## Lo que Claude.ai NO conoce (logros post-CONTEXTO_v8_1)

### S010 — 2026-03-20 (Sprint 1 cierre Claude Code)
- 7 reportes HTML desplegados en Vercel: CEO, Inversionista, Dev, Prensa, PM, Auditoría, Bitácora
- Fuente de verdad: `bitacora_data.js` → `window.BITACORA_DATA` (no Firebase, no Word)
- Protocolo sprint_nuevo.json: Claude genera JSON → sync_bitacora.py integra → Vercel publica
- `pct_activos` (Agentes 1-4) como métrica primaria CEO separada de `ecosistema_pct`
- `renderPulso()` — sección Pulso del Ecosistema por rol en cada reporte HTML
- Sort sprints/auditorías newest first en todos los reportes
- Prueba real Agente 2 POS validada: VentaReal $440 · Brecha +$11.25 SOBRANTE · Sáb 15 mar
- A004 registrada: Infraestructura Gerencial score 5.2/10 (10 PAs de mejora)
- Nav sticky entre los 7 reportes con active link detection

### S011 — 2026-03-27 (Consolidación técnica A004)
- **PA-A04-01 ✓** — Backup automático bitacora_data.js con timestamp en deploy.bat
- **PA-A04-02 ✓** — `lib/shared.js` creado: SD.esc(), SD.fmtFecha(), SD.renderPulso(), SD.initNav(), SD.getSprintParam(), SD.copySprintLink() — elimina duplicación en 7 archivos
- **PA-A04-03 ✓** — sync_bitacora.py: validación JSON + escritura atómica (.tmp → rename)
- **PA-A04-08 ✓** — `?sprint=SXXX` query param en los 7 reportes + botón 🔗 Compartir sprint + toast confirmación
- **CR-03 fix** — reporte-pm: optional chaining null safety
- **CR-05 fix** — reporte-dev: null guards en date parsing
- **CR-06 fix** — reporte-dev: SD.esc() en pending items — cierra XSS residual
- **Deuda Técnica visible** — reporte-dev muestra auditorias[].plan_accion donde completado=false en tiempo real
- **CSS dark consolidado** — clases .dev-* en reportes.css, elimina 150 líneas inline
- Score A004 estimado post-S011: ~7.5/10 (desde 5.2/10)

---

## Reconciliación: Sistema Claude.ai vs Sistema Claude Code

Claude.ai diseñó un sistema documental (Word/PDF). Claude Code construyó el mismo sistema en HTML/Vercel. Son complementarios:

| Concepto Claude.ai | Implementación Claude Code | Estado |
|-------------------|---------------------------|--------|
| Bitácora (Manual_Operaciones.docx) | `bitacora_data.js` + `reporte-bitacora.html` | ✅ Activo en Vercel |
| Reporte CEO | `reporte-ceo.html` | ✅ Activo en Vercel |
| Reporte Inversionista Privado/Familiar | `reporte-inversionista.html` | ✅ Activo (unificado) |
| Reporte Prensa | `reporte-prensa.html` | ✅ Activo en Vercel |
| Reporte Developers | `reporte-dev.html` (dark mode) | ✅ Activo en Vercel |
| Reporte Project Manager | `reporte-pm.html` | ✅ Activo en Vercel |
| Reporte Auditoría | `reporte-auditoria.html` | ✅ Activo en Vercel |
| Reporte Histórico | Pendiente en HTML | 🔴 Falta integrar |
| 8 reportes por rol | 7 HTML desplegados (Histórico pendiente) | 🟡 Casi completo |

**Conclusión:** El sistema HTML de Claude Code YA implementó lo que Claude.ai diseñó documentalmente. El CONTEXTO_v8_1.md debe actualizarse para reflejar que los reportes existen como HTML en Vercel, no como archivos pendientes de crear.

---

## Arquitectura Sala de Mando (A1) — Real

```
sala-de-mando/
├── data/
│   ├── bitacora_data.js      ← FUENTE ÚNICA DE VERDAD
│   └── backups/              ← backup automático con timestamp (PA-A04-01)
├── lib/
│   └── shared.js             ← SD.esc, fmtFecha, renderPulso, initNav, getSprintParam, copySprintLink
├── css/reportes.css          ← estilos compartidos + .dev-* dark theme
├── reporte-ceo.html
├── reporte-inversionista.html
├── reporte-dev.html          ← dark mode + Deuda Técnica Activa en tiempo real
├── reporte-prensa.html
├── reporte-pm.html
├── reporte-auditoria.html
└── reporte-bitacora.html
```

Ciclo de actualización:
```
Sprint cierra → sprint_nuevo.json → sync_bitacora.py (valida JSON + escritura atómica)
→ deploy.bat (backup timestamp) → bitacora_data.js → git push → Vercel auto-deploy
```

---

## Auditorías Activas

| ID | Sprint | Score | Tema | PAs pendientes |
|----|--------|-------|------|----------------|
| A001 | S006 | 7.8/10 | Sistema de Reportería | PA-02, PA-06..PA-10 |
| A002 | S007 | 8.3/10 | Full Vision Developer | PA-11, PA-12 |
| A003 | S010 | 8.8/10 | Agente 2 POS Integral | PA-A3-01 (OPERATING_HOURS), PA-A3-02 (logout) |
| A004 | S010→S011 | ~7.5/10 | Infraestructura Gerencial | PA-A04-04/05/06/07/09/10 (media/baja) |

---

## Sprint S012 — Objetivos (en curso)

| Prioridad | Tema | Área |
|-----------|------|------|
| 🔴 Alta | Registrar sesiones 22-mar y 26-mar en bitácora | Agente 1 |
| 🔴 Alta | Claude.ai: rehacer documentos maestros unificados (sin duplicados) | CEREBRO IA |
| 🟡 Media | PDF export reporte CEO + WhatsApp share (Web Share API) | Agente 1 |
| 🟡 Media | Go-live Agente 2 POS: OPERATING_HOURS.enabled=true + App.logout() | Agente 2 |
| 🟡 Media | Deploy Agente 3 Financiero a Railway/Render | Agente 3 |
| 🟡 Media | Módulo 1B Finanzas (feed desde Agente 2 Google Sheets) | Agente 1 |
| ⚪ Baja | Archivar versiones históricas en CLAUDE.IA (archivo_historico/) | CEREBRO IA |

---

## Roadmap S012 → S014

- **S012:** CEREBRO IA consolidado + sesiones no registradas en bitácora + PDF/WhatsApp share
- **S013:** PIN de acceso por audiencia (viewer privado por rol)
- **S014:** Módulo 1B Finanzas estratégicas — feed desde Agente 2

---

## Agenda para próxima sesión Claude.ai

**Lo que Claude.ai debe hacer (en orden):**
1. Leer este ESTADO_ECOSISTEMA_ACTUAL.md completo
2. Leer CONTEXTO_v8_1.md + IdentidadAgenteGerencial.md + Manual (caps 1-9)
3. Corregir los errores del CONTEXTO_v8_1 (tabla de correcciones arriba)
4. Reorganizar CLAUDE.IA: mover versiones históricas a `archivo_historico/`, renombrar maestros con formato `NombreDocumento_vX.X_YYYYMMDD`
5. Unificar Manual de Operaciones: consolidar caps 1-8 + cap 9 (addendum) en un solo documento maestro
6. Actualizar todos los documentos maestros con estado real del ecosistema (sprint S011 completado, 7 HTML en Vercel)
7. Crear CONTEXTO_v9.0 con toda la información correcta y actualizada

---

*Mantenido por: Claude Code CLI*
*Actualizado: 2026-03-27 — Sprint S012*
*Ver también: CONTEXTO_v8_1.md (contexto operativo) · bitacora_data.js (fuente de verdad sprints)*
*GitHub CEREBRO IA: https://github.com/javsequeiraSD/jjsa-claude-ia-cerebro*
