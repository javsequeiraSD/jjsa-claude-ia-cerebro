# ESTADO ECOSISTEMA ACTUAL — Inversiones JJSA / Sivar Dogs
> Archivo vivo mantenido por Claude Code | Actualizado: 2026-03-22
> Complementa CONTEXTO_v8_1.md con el estado real post-sprint
> Claude Code actualiza este archivo al cerrar cada sprint

---

## Estado de los 8 Agentes (post-S010 — 2026-03-20)

| # | Agente | Herramienta | % | Estado |
|---|--------|-------------|---|--------|
| 1 | Gerencial (Sala de Mando) | Claude Code | **61%** | En construcción — S011 abierto |
| 2 | POS Integral | Claude Code | **90%** | **EN PRODUCCIÓN** — prueba real validada |
| 3 | Financiero-Contable-Fiscal | Claude Code Python | **41%** | Funcional local — deploy Railway pendiente |
| 4 | Project Manager | Antigravity | **33%** | Base lista (Fase 1 completa) |
| 5 | Marketing | Antigravity | 0% | Por crear |
| 6 | Pedidos Aquí | Antigravity | 0% | Por crear |
| 7 | Inventario | Antigravity | 0% | Por crear |
| 8 | Tienda en Línea | Antigravity | 0% | Por crear |

**`pct_activos` (Agentes 1-4) = 56%** ← métrica primaria CEO
**`ecosistema_pct` (los 8) = 53%** ← referencia estratégica

---

## ⚠️ Correcciones Críticas vs CONTEXTO_v8_1.md

| Campo | CONTEXTO_v8_1.md dice | Realidad actual |
|-------|----------------------|-----------------|
| Numeración agentes | A2=Financiero, A3=POS | **A2=POS Integral, A3=Financiero** |
| Tecnología Sala de Mando | Firebase Firestore | **Vercel (archivos estáticos) — NO Firebase** |
| DTEs procesados | 1,541 / $44,815.94 | **2,170 DTEs / $64,205.65** |
| Agente 1 % | 48% | **61% (post-S010)** |
| Agente 2 POS % | 64% | **90% (post-S010, prueba real validada)** |
| Reportes | 8 pendientes | **7 reportes HTML en producción en Vercel** |

---

## URLs en Producción

| Sistema | URL | PIN | Estado |
|---------|-----|-----|--------|
| Sala de Mando (A1) | https://sivar-dogs-sala-de-mando.vercel.app/ | 150818 | ✅ Activo |
| POS Integral (A2) | https://sivar-control.vercel.app/ | 0001 Vilma / 0000 Admin | ✅ Activo |
| Financiero (A3) | http://localhost:5000 | — | 🟡 Solo local |

---

## Logros S010 (2026-03-20) — que Claude.ai NO conoce

- Nav sticky entre los 7 reportes (active link detection)
- `esc()` en todos los reportes (mitigación XSS)
- `pct_activos` como KPI primario separado de `ecosistema_pct`
- `renderPulso()` — sección Pulso del Ecosistema por rol en cada reporte
- Sort auditorías y sprints newest first
- PA status badges con `completado_en: "SXXX"`
- `hora_sesion` en sprint cards
- `narrativa_prensa` dinámica desde `negocio{}` en bitacora_data.js
- Prueba real Agente 2 validada: VentaReal $440 · Brecha +$11.25 SOBRANTE
- A004 registrada: Infraestructura Gerencial, score 5.2/10 (10 PAs pendientes)

---

## Arquitectura Sala de Mando (A1) — Real

```
sala-de-mando/
├── data/bitacora_data.js      ← FUENTE ÚNICA DE VERDAD
│   └── window.BITACORA_DATA = { meta, agentes[], sprints[], auditorias[] }
├── css/reportes.css
├── reporte-ceo.html
├── reporte-inversionista.html
├── reporte-dev.html           ← dark mode
├── reporte-prensa.html
├── reporte-pm.html
├── reporte-auditoria.html
└── reporte-bitacora.html
```

Ciclo de actualización:
```
Sprint cierra → sprint_nuevo.json → sync_bitacora.py → bitacora_data.js → git push → Vercel auto-deploy
```

---

## Auditorías Activas

| ID | Sprint | Score | Tema | PAs pendientes |
|----|--------|-------|------|----------------|
| A001 | S006 | 7.8/10 | Sistema de Reportería | PA-02, PA-06..PA-10 |
| A002 | S007 | 8.3/10 | Full Vision Developer | PA-11, PA-12 |
| A003 | S010 | 8.8/10 | Agente 2 POS Integral | PA-A3-01, PA-A3-02 |
| A004 | S010 | 5.2/10 | Infraestructura Gerencial | PA-A04-01..10 |

**A004 bugs críticos (S011 los resuelve):**
- CR-01: bitacora_data.js sin backup = SPOF
- CR-02: esc()/renderPulso() duplicados en 7 archivos
- CR-03: null safety faltante en reporte-pm.html
- CR-04: Google Fonts bloquea render
- CR-05: date parsing con null en reporte-dev
- CR-06: XSS residual en algunos innerHTML

---

## Sprint Actual: S011

**Objetivo:** Consolidación técnica A004 + share por sprint

| PA | Prioridad | Descripción |
|----|-----------|-------------|
| PA-A04-01 | Alta | Backup auto bitacora_data.js |
| PA-A04-02 | Alta | lib/shared.js — unificar esc(), renderPulso(), fmtFecha() |
| PA-A04-03 | Alta | Validación JSON en sync_bitacora.py |
| PA-A04-08 | Alta | Share por sprint: ?sprint=SXXX + link copiable |
| PA-A04-04..07,09,10 | Media/Baja | Ver bitacora_data.js |

---

## Agente 3 — Financiero (Estado Detallado)

- **DTEs únicos procesados:** 2,170 (certificados)
- **Monto total compras:** $64,205.65
- **Con PDF:** ~84% (resto: links vencidos, irrecuperables)
- **Descarga automática:** Task Scheduler 7AM diario
- **Deduplicación:** por `codigoGeneracion` UUID — NUNCA por nombre de archivo
- **Arranque local:** `iniciar_dashboard.bat` → http://localhost:5000
- **Deploy pendiente:** Railway o Render — NO Vercel (app Flask con estado)

---

## Roadmap S011 → S013

- **S011:** Consolidación técnica A004 (CR-01/02/03) + share por sprint
- **S012:** PDF export + WhatsApp share (Web Share API)
- **S013:** PIN de acceso por audiencia (viewer privado por rol)

---

*Próxima actualización: al cerrar S011*
*Mantenido por: Claude Code CLI*
*Ver también: CONTEXTO_v8_1.md (contexto operativo) · bitacora_data.js (fuente de verdad sprints)*
