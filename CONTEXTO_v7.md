# CONTEXTO.md v7.0
**Proyecto:** Mando Central — Sivar Dogs  
**CEO:** Javier Sequeira  
**Última actualización:** 21 de marzo de 2026 (motor v5.1 — 5 fixes visuales)  
**Sesión:** Chat 2 — Cortes Diarios Sivar Dogs

---

## 1. DATOS DEL NEGOCIO

**Nombre:** Sivar Dogs  
**Ubicación:** Parque San Martín, Santa Tecla, El Salvador  
**Fundado:** 2018  
**Operación:** Lunes a Sábado  
**Equipo:** Vilma Luna (vendedora on-site), Daysi Rivas (auxiliar), Doris Rivas (producción)  
**Contexto financiero:** Días típicos 30-40 hotdogs (bajo punto de equilibrio). Hay préstamos, salarios y alquileres fijos. Situación financiera requiere saneamiento.

---

## 2. REGLAS OPERATIVAS DEL NEGOCIO (v5.0 — vigentes)

### Empaques
- Pan Sanfran = 12u/bolsa | Pan Única = 10u/bolsa
- Salchicha Jumbo = 16u/paquete | Salchicha Mini Jumbo = 24u/paquete

### Receta
- Todos los hotdogs → Pan Sanfran + Salchicha Jumbo
- **EXCEPCIÓN:** Hotdog Básico → Pan Única + Salchicha Mini Jumbo
- Combo = 1 hotdog + 1 soda + 1 lays

### Precios oficiales
| Producto | Precio |
|---|---|
| Hotdog Clásico individual | $1.50 |
| Hotdog Chilidog / Chickedog | $2.00 |
| Combo Clásico | $2.75 (precio único) |
| Combo Especialidad | $3.25 (precio único) |
| Soda individual | $1.00 |
| Lays con ticket individual | $0.50 |
| **Lays sin ticket / en combo** | **$0.25 — NUEVA REGLA 21/03/2026** |
| Flanes | $0.65 |
| Alitas | $4.00 |

### Reglas críticas
- **R04 Pan = Salchicha:** Deben coincidir siempre. Diff ≤ 2 = marginal. Diff > 2 = hallazgo crítico.
- **R05 Jerarquía de verdad:** 1° Caja real → 2° Inventario → 3° Ticket (referencia, no verdad)
- **R06 Combos:** Precio único en venta_final. NUNCA desglosar soda + lays como filas adicionales.
- **R07 Lays:** Sin ticket = $0.25 siempre. Con ticket individual = $0.50.
- **R08 No ticketeados:** Asumir clásicos $1.50 (método conservador).
- **R09 Inicio del día:** Inventario inicio = sobra física del día anterior. Vuelto inicial = vuelto final anterior.
- **R10 Dato faltante:** Asumir 0 + tag [REVISAR].
- **R11 Sobrante:** También es alerta. Registrar como "Devolución".

---

## 3. MOTOR DE REPORTES v5.1 (implementado 21/03/2026)

### Arquitectura
```
calcular(cfg)        → recibe 10 inputs, calcula todo automáticamente
generar_reporte(cfg) → llama a calcular() y produce el PDF
```

### Los 10 inputs crudos (único input humano)
1. `tickets` — dict: clasico, chilidog, chickedog, combo_clasico, combo_esp, soda_ind, lays_ind, alitas
2. `inventario_vendido` — dict: hd, sodas, lays
3. `pan_vendido` — int
4. `corte_efectivo` — float
5. `pos` — float
6. `pedidosya` — float
7. `transferencia` — float
8. `total_gastos` — float
9. `vuelto_inicial` — float
10. `vuelto_final` — float

### Lo que calcula automáticamente
- `concilio_total` = total_ticket − ajuste + no_ticketeados
- `venta_real` = corte + pos + peya + transf + gastos − vuelto_inicial
- `brecha` = venta_real − concilio
- `semáforo`, `venta_final` (sin doble conteo), `tvi`, `hallazgos`

### Fórmulas
- **Venta Real** = Corte Efectivo + POS + PedidosYa + Transferencias + Gastos − Vuelto Inicial
- **Corte Efectivo** = Efectivo Enviado + Vuelto Final
- **Concilio** = Tickets ($) + No Ticketeados ($)
- **Brecha** = Venta Real − Concilio

### Semáforo
| Tipo | Rango | Estado |
|---|---|---|
| Sobrante | $0-$5 | 🟢 Verde |
| Sobrante | $5-$10 | 🟡 Amarillo |
| Sobrante | $10-$15 | 🟠 Naranja |
| Sobrante | >$15 | 🔴 Rojo |
| Faltante | $0-$5 | 🟡 Amarillo |
| Faltante | $5-$10 | 🟠 Naranja |
| Faltante | >$10 | 🔴 Rojo |

### Errores corregidos en v5.1
- **Doble conteo combos:** Se listaban soda+lays del combo como filas extra → $42.50 inflación eliminada
- **Concilios manuales:** 5 días tenían errores de $0.25 a $1.25 → ahora motor calcula
- **Lays sin ticket:** Se asignaba $0.50 → corregido a $0.25

### Regla estándar
**TODO cálculo financiero ejecutado por el motor, NUNCA por el humano en el chat.**

---

## 4. KPIs OFICIALES DEL DÍA

1. **Caja Real ($)** — fórmula venta real
2. **Venta Oficial ($)** — concilio inventario
3. **Tickets Registrados ($)** — ventas ticketeadas
4. **Brecha Diaria ($)** — con signo: + sobrante, − faltante

**Concilio contable:**
- Brecha (+) sobrante → "Otros ingresos no identificados"
- Brecha (−) faltante → "Diferencias de caja"

---

## 5. CIERRES AUDITADOS — SEMANA OFICIAL LUNES 16 – SÁBADO 21/03/2026

> **Nota:** La semana oficial es Lunes–Sábado. El Sábado 15 queda como histórico de la semana anterior.

### Sábado 15 — Histórico semana anterior
| HD | Venta Real | Concilio | Brecha | Semáforo |
|---|---|---|---|---|
| 222 | $440.00 | $429.50 | +$10.50 | 🟠 Naranja |

### Semana oficial Lun 16 – Sáb 21

| Día | HD | Venta Real | Concilio | Brecha | Semáforo |
|---|---|---|---|---|---|
| Lun 16 | 114 | $220.24 | $215.75 | +$4.49 | 🟢 Verde |
| Mar 17 | 44 | $81.45 | $78.75 | +$2.70 | 🟢 Verde |
| Mié 18 | 48 | $95.65 | $90.25 | +$5.40 | 🟡 Amarillo |
| Jue 19 | 44 | $75.75 | $77.25 | −$1.50 | 🟢 Verde |
| Vie 20 | 53 | $98.50 | $99.50 | −$1.00 | 🟢 Verde |
| Sáb 21 | 93 | $171.80 | $169.75 | +$2.05 | 🟢 Verde |
| **TOTAL** | **396** | **$743.39** | **$731.25** | **+$12.14** | 🟠 Naranja |

**KPIs semanales:**
- HD promedio/día: 66 (vs histórico 61 HD/día ✅ por encima)
- Mejor día: Lunes 16 (114 HD · $220.24)
- Días en verde: 5/6
- Brecha neta: +$12.14 sobrante 🟠 Naranja

**Tendencia caja Lun-Sáb:** $43.35 → $16.40 → $12.85 → $33.20 → $18.95 → $5.30 → **$40.45**

**Confirmaciones pendientes con Vilma:**
- Combo especialidad miércoles 18 — ¿se cobró?
- 2 tickets extra jueves 19 — ¿devolución o error?
- 1 HD + 3 sodas ticket extra viernes 20 — ¿causa?

---

## 6. HISTÓRICO WHATSAPP

- **Rango:** 16/12/2024 – 18/03/2026 | **464 registros**
- Total HD ticketeados: 28,321 | Total productos: 37,024 | Ingreso: $54,186
- Promedio: 61 HD/día | $116.77/día
- Mejor mes: Dic 2024 (82.9 HD/día) | Récord: 188 HD el 14/03/2026
- Mejor día semana: Lunes (78.9 HD avg)
- Mix: Clásico 69.4% | Chilidog 9.6% (creció 4.5x) | Combo Clásico 5.9%

---

## 7. ARQUITECTURA TÉCNICA

### Stack
- **Motor reportes:** Python + ReportLab → PDFs diarios
- **Agente POS:** Código local → GitHub → Vercel (sivar-control.vercel.app)
- **Base de datos POS:** Google Sheets (SE MANTIENE — no migrar)
- **Firebase:** SOLO para modelo SaaS futuro
- **Sala de Mando:** sivar-dogs-sala-de-mando.vercel.app (Firebase Firestore)

### Agentes del ecosistema
| Agente | Estado | Plataforma |
|---|---|---|
| Agente 1 Gerencial | En construcción | Claude Code |
| Agente 2 Financiero-Contable | MVP local activo | Antigravity |
| Agente 3 POS | En producción | Vercel |
| Agentes 4-7 | Pendiente | — |

---

## 8. DOCUMENTOS MAESTROS — ESTADO AL 21/03/2026

| Documento | Versión | Estado |
|---|---|---|
| CONTEXTO.md | v7.0 | ✅ Este archivo |
| motor_reportes.py | v5.1 | ✅ Activo — descargado |
| Manual_Operaciones_Claude_IA.docx | v1.1 | ✅ 7 capítulos |
| ReglasDelSistema_SivarDogs.docx | v5.0 | ✅ R01-R11 + M01-M06 |
| Spec_ReporteCierre_SivarDogs.docx | v2.0 | ✅ Para Claude Code |
| ResumenEjecutivo_SivarDogs.docx | v3.0 | ✅ Actualizado |
| Historico_SivarDogs.xlsx | — | ✅ 464 días |
| historico_v2.csv | — | ✅ Datos crudos |
| Reporte_Historico_SivarDogs_v3.pdf | v3 | ✅ Para inversores/bancos |
| SivarDogs_Control_Operativo.xlsx | — | ⚠️ Pendiente actualizar |
| Explicaciones_SivarDogs.docx | v1.3 | ⚠️ Pendiente actualizar |

### Ruta local
```
C:\Users\HP\OneDrive\LAPTOP\SIVAR DOGS\GERENCIA\[carpeta ecosistema]\
```
*(Confirmar ruta exacta — fue reorganizada)*

---

## 9. ROADMAP — TRES CHATS ACTIVOS

### Chat 2 — Cortes Diarios (este chat) ✅ En curso
**Pendientes menores:**
- Confirmaciones con Vilma (ver sección 5)

### Chat 1 — Excel Finanzas / Módulo B1 Agente Gerencial ⏳
**Adjuntar:** CONTEXTO.md + Finanzas_2026.xlsm + SivarDogs_Control_Operativo.xlsx  
**Temas:** Módulo B1 finanzas, P&L mensual, punto de equilibrio, integración concilio diario, estructura contable de brechas

### Chat 3 — Análisis Profundo Histórico ⏳
**Adjuntar:** CONTEXTO.md + Historico_SivarDogs.xlsx + historico_v2.csv  
**Temas:** Punto de equilibrio histórico, estacionalidad, proyecciones, meta diaria por día, dashboard tendencias

---

## 10. PROTOCOLO DE INICIO — CLAUDE CODE

Al iniciar sesión en Claude Code:
1. Leer este CONTEXTO.md completo
2. Leer AVANCE.md si existe
3. Confirmar ruta de archivos
4. Ejecutar sync_avance.py para actualizar estado de agentes
5. No calcular nada manualmente — usar motor_reportes.py

## 11. PROTOCOLO DE CIERRE — CUALQUIER CHAT

Al cerrar cualquier sesión importante:
1. Actualizar notas de memoria de Claude
2. Generar CONTEXTO.md actualizado
3. Actualizar documentos maestros afectados
4. Descargar todos los archivos generados
5. Versionar documentos Word con número incremental

---

## 12. FIREBASE / PROYECTO TÉCNICO

- **Proyecto Firebase:** sivar-dogs-gerencia
- **Script sync:** sync_avance.py (agrega estados de agentes a AVANCE.md)
- **Sprint 1 activo (Mar 13-27):** Migrar avance_data.js a Firebase, Deploy Agente 2 a Railway, Firebase Auth, KPI real en dashboard

---

*CONTEXTO.md v7.0 — generado automáticamente al cierre de sesión Chat 2 — 21/03/2026*
