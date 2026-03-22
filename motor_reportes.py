from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, KeepTogether)

# ── PALETA ────────────────────────────────────────────────────────────────────
C_DARK   = colors.HexColor('#1a1a2e')
C_ACCENT = colors.HexColor('#e63946')
C_MID    = colors.HexColor('#457b9d')
C_MUTED  = colors.HexColor('#6c757d')
C_ROW    = colors.HexColor('#f8f9fa')
C_GREEN  = colors.HexColor('#d4edda')
C_GREEN_T= colors.HexColor('#155724')
C_WARN   = colors.HexColor('#fff3cd')
C_WARN_T = colors.HexColor('#856404')
C_ORANGE = colors.HexColor('#ffe5b4')
C_ORANGE_T=colors.HexColor('#7d4e00')
C_WHITE  = colors.white
C_BLUE   = colors.HexColor('#cce5ff')
C_BLUE_T = colors.HexColor('#004085')
C_RED_L  = colors.HexColor('#f8d7da')
C_RED_T  = colors.HexColor('#721c24')
GRID     = colors.HexColor('#dee2e6')
W = 7.0 * inch

# ── ESTILOS ───────────────────────────────────────────────────────────────────
s_small = ParagraphStyle('sm',  fontName='Helvetica',        fontSize=8,  textColor=C_MUTED, leading=12)
s_note  = ParagraphStyle('nt',  fontName='Helvetica-Oblique',fontSize=8,  textColor=C_MID,   leading=12)
s_warn  = ParagraphStyle('wn',  fontName='Helvetica-Oblique',fontSize=8,  textColor=C_WARN_T,leading=12)
s_title = ParagraphStyle('ti',  fontName='Helvetica-Bold',   fontSize=22, textColor=C_DARK,  spaceAfter=4, leading=26)
s_sec   = ParagraphStyle('sc',  fontName='Helvetica-Bold',   fontSize=10, textColor=C_ACCENT,spaceAfter=4)
s_step  = ParagraphStyle('st',  fontName='Helvetica-Bold',   fontSize=8,  textColor=C_MUTED, spaceAfter=3)

def sh(text):
    return [Spacer(1,8), HRFlowable(width='100%',thickness=1,color=C_ACCENT,spaceAfter=4),
            Paragraph(text.upper(), s_sec)]

def ts(hbg=C_DARK, alt=True):
    return TableStyle([
        ('BACKGROUND',(0,0),(-1,0),hbg),('TEXTCOLOR',(0,0),(-1,0),C_WHITE),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8),
        ('FONTNAME',(0,1),(-1,-1),'Helvetica'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[C_WHITE,C_ROW] if alt else [C_WHITE]),
        ('GRID',(0,0),(-1,-1),0.3,GRID),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
        ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
    ])

def kpi_card(label, val, sub, bg, border, val_color):
    return Table([
        [Paragraph(label, ParagraphStyle('kl',fontName='Helvetica',     fontSize=8,   textColor=C_MUTED,  alignment=TA_CENTER,leading=11))],
        [Paragraph(val,   ParagraphStyle('kv',fontName='Helvetica-Bold',fontSize=18,  textColor=val_color,alignment=TA_CENTER))],
        [Paragraph(sub,   ParagraphStyle('ks',fontName='Helvetica',     fontSize=7.5, textColor=C_MUTED,  alignment=TA_CENTER,leading=10))],
    ], colWidths=[W/4 - 6],
    style=TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),('BOX',(0,0),(-1,-1),1,border),
        ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))

def kpi_row_4(c1,c2,c3,c4):
    return Table([[c1,c2,c3,c4]], colWidths=[W/4]*4,
        style=TableStyle([
            ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
            ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ]))

def bloque(titulo, monto, detalle, bg, fg, ancho):
    return Table([
        [Paragraph(titulo,  ParagraphStyle('bt',fontName='Helvetica-Bold',fontSize=8, textColor=fg,alignment=TA_CENTER,leading=11))],
        [Paragraph(monto,   ParagraphStyle('bm',fontName='Helvetica-Bold',fontSize=16,textColor=fg,alignment=TA_CENTER))],
        [Paragraph(detalle, ParagraphStyle('bd',fontName='Helvetica',     fontSize=7, textColor=fg,alignment=TA_CENTER,leading=10))],
    ], colWidths=[ancho],
    style=TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),('BOX',(0,0),(-1,-1),0.75,fg),
        ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))

def op(sym, top=22):
    return Table([[Paragraph(sym,ParagraphStyle('op',fontName='Helvetica-Bold',fontSize=16,
                  textColor=C_MUTED,alignment=TA_CENTER))]],
        colWidths=[0.28*inch],
        style=TableStyle([('TOPPADDING',(0,0),(-1,-1),top),('BOTTOMPADDING',(0,0),(-1,-1),0),
                          ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))

def semaforo(brecha):
    v = abs(brecha)
    if brecha == 0:    return C_GREEN,  C_GREEN_T, '🟢 PERFECTO',  'PERFECTO'
    elif brecha > 0:
        if v <= 5:     return C_GREEN,  C_GREEN_T, '🟢 Verde',     'SOBRANTE'
        elif v <= 10:  return C_WARN,   C_WARN_T,  '🟡 Amarillo',  'SOBRANTE'
        elif v <= 15:  return C_ORANGE, C_ORANGE_T,'🟠 Naranja',   'SOBRANTE'
        else:          return C_RED_L,  C_RED_T,   '🔴 Rojo',      'SOBRANTE'
    else:
        if v <= 5:     return C_WARN,   C_WARN_T,  '🟡 Amarillo',  'FALTANTE'
        elif v <= 10:  return C_ORANGE, C_ORANGE_T,'🟠 Naranja',   'FALTANTE'
        else:          return C_RED_L,  C_RED_T,   '🔴 Rojo',      'FALTANTE'

# ══════════════════════════════════════════════════════════════════════════════
# MOTOR DE CÁLCULO — calcula todo desde los 10 inputs
# ══════════════════════════════════════════════════════════════════════════════
def calcular(cfg):
    t   = cfg['tickets']
    inv = cfg['inventario_vendido']

    # ── Unidades en tickets ──────────────────────────────────────
    t_hd_u  = (t.get('clasico',0) + t.get('chilidog',0) + t.get('chickedog',0)
               + t.get('combo_clasico',0) + t.get('combo_esp',0))
    t_sod_u = t.get('soda_ind',0) + t.get('combo_clasico',0) + t.get('combo_esp',0)
    t_lay_u = t.get('lays_ind',0) + t.get('combo_clasico',0) + t.get('combo_esp',0)

    # ── Valor de tickets (combos = precio único) ─────────────────
    t_val = (t.get('clasico',0)*1.50    + t.get('chilidog',0)*2.00
           + t.get('chickedog',0)*2.00  + t.get('combo_clasico',0)*2.75
           + t.get('combo_esp',0)*3.25  + t.get('soda_ind',0)*1.00
           + t.get('lays_ind',0)*0.50   + t.get('alitas',0)*4.00)

    # ── No ticketeados (inventario − ticket, mínimo 0) ───────────
    hd_nt  = max(0, inv.get('hd',0)    - t_hd_u)
    sod_nt = max(0, inv.get('sodas',0) - t_sod_u)
    lay_nt = max(0, inv.get('lays',0)  - t_lay_u)

    # ── Ajuste si ticket > inventario (inventario manda) ─────────
    hd_adj  = max(0, t_hd_u  - inv.get('hd',0))
    sod_adj = max(0, t_sod_u - inv.get('sodas',0))
    lay_adj = max(0, t_lay_u - inv.get('lays',0))
    ajuste  = hd_adj*1.50 + sod_adj*1.00 + lay_adj*0.50

    # ── No ticketeados valor (lays sin ticket = $0.25) ───────────
    nt_val = hd_nt*1.50 + sod_nt*1.00 + lay_nt*0.25

    # ── Concilio oficial ─────────────────────────────────────────
    concilio = round(t_val - ajuste + nt_val, 2)

    # ── Venta real ───────────────────────────────────────────────
    venta_real = round(
        cfg['corte_efectivo'] + cfg.get('pos',0) + cfg.get('pedidosya',0)
        + cfg.get('transferencia',0) + cfg['total_gastos'] - cfg['vuelto_inicial'], 2)

    # ── Brecha y semáforo ────────────────────────────────────────
    brecha = round(venta_real - concilio, 2)
    sem_bg, sem_fg, sem_label, tipo = semaforo(brecha)
    brecha_str = f"+${brecha:.2f}" if brecha >= 0 else f"-${abs(brecha):.2f}"

    # ── Pan vs Salchicha ─────────────────────────────────────────
    pan_vend = cfg.get('pan_vendido', inv.get('hd', 0))
    sal_vend = inv.get('hd', 0)
    diff_pan = abs(pan_vend - sal_vend)
    if diff_pan == 0:
        pan_sal_nota = f'Pan ({pan_vend}) = Salchicha ({sal_vend}): CUADRA PERFECTO ✓'
        pan_sal_status = '✅ Perfecto'
    elif diff_pan <= 2:
        pan_sal_nota = f'Pan ({pan_vend}) vs Salchicha ({sal_vend}): diferencia {diff_pan} — marginal, error de conteo mínimo.'
        pan_sal_status = '⚠️ Marginal'
    else:
        pan_sal_nota = f'Pan ({pan_vend}) vs Salchicha ({sal_vend}): diferencia {diff_pan} — HALLAZGO CRÍTICO.'
        pan_sal_status = '🔴 Crítico'

    # ── Tabla venta_final (sin doble conteo) ─────────────────────
    vf = []
    # Hotdogs individuales
    if t.get('clasico',0) > 0 or hd_nt > 0:
        u_clas = t.get('clasico',0) + (hd_nt if hd_nt > 0 else 0)
        origen = f"Ticket ({t.get('clasico',0)})" + (f" + No ticket ({hd_nt})" if hd_nt > 0 else "")
        vf.append(['Hotdog Clásico', origen, str(u_clas), '$1.50', f'${u_clas*1.50:.2f}'])
    if t.get('chilidog',0) > 0:
        vf.append(['Hotdog Chilidog','Ticket',str(t['chilidog']),'$2.00',f'${t["chilidog"]*2.00:.2f}'])
    if t.get('chickedog',0) > 0:
        vf.append(['Hotdog Chickedog','Ticket',str(t['chickedog']),'$2.00',f'${t["chickedog"]*2.00:.2f}'])
    if t.get('combo_clasico',0) > 0:
        vf.append(['Combo Clásico','Ticket (incl. soda+lays)',str(t['combo_clasico']),'$2.75',f'${t["combo_clasico"]*2.75:.2f}'])
    if t.get('combo_esp',0) > 0:
        vf.append(['Combo Especialidad','Ticket (incl. soda+lays)',str(t['combo_esp']),'$3.25',f'${t["combo_esp"]*3.25:.2f}'])
    # Sodas individuales
    sod_tick_ind = t.get('soda_ind',0)
    if sod_tick_ind > 0 or sod_nt > 0:
        u_sod = sod_tick_ind + sod_nt
        origen = f"Ticket ({sod_tick_ind})" + (f" + No ticket ({sod_nt})" if sod_nt > 0 else "")
        vf.append(['Soda individual', origen, str(u_sod), '$1.00', f'${u_sod*1.00:.2f}'])
    # Lays individuales
    if t.get('lays_ind',0) > 0:
        vf.append(['Lays individual','Ticket',str(t['lays_ind']),'$0.50',f'${t["lays_ind"]*0.50:.2f}'])
    if lay_nt > 0:
        vf.append(['Lays (estimadas)','Inventario − ticket',str(lay_nt),'$0.25',f'${lay_nt*0.25:.2f}'])
    # Alitas
    if t.get('alitas',0) > 0:
        vf.append(['Alitas','Ticket',str(t['alitas']),'$4.00',f'${t["alitas"]*4.00:.2f}'])

    # Verificar que vf suma = concilio
    vf_sum = sum(float(r[4].replace('$','')) for r in vf)

    # ── Tabla TVI ────────────────────────────────────────────────
    tvi = []
    tvi.append(['Pan Sanfran', str(pan_vend), str(t_hd_u), str(pan_vend-t_hd_u), '—'])
    tvi.append(['Salchicha Jumbo', str(sal_vend), str(t_hd_u), str(sal_vend-t_hd_u), '—'])
    tvi.append(['Pan vs Salchicha', str(pan_vend), str(sal_vend), str(pan_vend-sal_vend),
                '✓ Cuadra' if diff_pan==0 else f'Diff {diff_pan}'])
    tvi.append(['Hotdogs', str(sal_vend), str(t_hd_u), str(hd_nt if hd_nt>0 else -hd_adj),
                f'${hd_nt*1.50:.2f}' if hd_nt>0 else f'-${hd_adj*1.50:.2f}'])
    tvi.append(['Sodas', str(inv.get('sodas',0)), str(t_sod_u),
                str(sod_nt if sod_nt>0 else -sod_adj),
                f'${sod_nt*1.00:.2f}' if sod_nt>0 else f'-${sod_adj*1.00:.2f}'])
    tvi.append(['Lays', str(inv.get('lays',0)), str(t_lay_u),
                str(lay_nt if lay_nt>0 else -lay_adj),
                f'${lay_nt*0.25:.2f}' if lay_nt>0 else f'-${lay_adj*0.50:.2f}'])
    tvi.append(['TOTAL NO TICKETEADO', '', '', str(hd_nt+sod_nt+lay_nt), f'${nt_val:.2f}'])

    # ── Hallazgos automáticos — categorías estándar ──────────────
    # Categorías: Resuelto / Monitorear / Pendiente / Crítico
    hallazgos = []
    h_num = 1

    # Pan vs Salchicha
    if diff_pan == 0:
        hall_pan_cat = 'Resuelto'
    elif diff_pan <= 2:
        hall_pan_cat = 'Monitorear'
    else:
        hall_pan_cat = 'Crítico'
    hallazgos.append([str(h_num), f'Pan vs Salchicha: {diff_pan} diferencia',
                      pan_sal_nota.split(':')[1].strip() if ':' in pan_sal_nota else pan_sal_nota,
                      hall_pan_cat])
    h_num += 1

    if hd_nt > 0:
        hallazgos.append([str(h_num), f'{hd_nt} hotdogs no ticketeados (${hd_nt*1.50:.2f})',
                          'Asumidos clásicos $1.50. Método conservador.', 'Resuelto'])
        h_num += 1
    if hd_adj > 0:
        hallazgos.append([str(h_num), f'{hd_adj} tickets HD sin producto físico',
                          'Inventario manda. Tickets descontados del concilio.', 'Pendiente'])
        h_num += 1
    if sod_nt > 0:
        hallazgos.append([str(h_num), f'{sod_nt} sodas no ticketeadas (${sod_nt:.2f})',
                          'Confirmadas por inventario.', 'Resuelto'])
        h_num += 1
    if sod_adj > 0:
        hallazgos.append([str(h_num), f'{sod_adj} tickets soda sin respaldo físico',
                          'Inventario manda. Descontados del concilio.', 'Pendiente'])
        h_num += 1
    if lay_nt > 0:
        hallazgos.append([str(h_num), f'{lay_nt} lays estimadas ${lay_nt*0.25:.2f}',
                          'Sin ticket individual. Valuadas a $0.25 (precio combo).', 'Resuelto'])
        h_num += 1

    # Revisar datos faltantes
    revisar = cfg.get('revisar', [])
    for campo in revisar:
        hallazgos.append([str(h_num), f'[REVISAR] {campo}',
                          f'Dato no reportado por Vilma. Asumido 0. Confirmar en concilio posterior.', 'Pendiente'])
        h_num += 1

    var_caja = cfg['vuelto_final'] - cfg['vuelto_inicial']
    if var_caja >= 0:
        caja_cat = 'Resuelto'
    elif var_caja >= -15:
        caja_cat = 'Monitorear'
    else:
        caja_cat = 'Crítico'
    hallazgos.append([str(h_num), f'Caja: ${cfg["vuelto_inicial"]:.2f} → ${cfg["vuelto_final"]:.2f}',
                      f'Variación {var_caja:+.2f}', caja_cat])
    h_num += 1

    # Brecha
    if brecha == 0:
        brecha_cat = 'Resuelto'
    elif abs(brecha) <= 5:
        brecha_cat = 'Monitorear'
    elif abs(brecha) <= 10:
        brecha_cat = 'Pendiente'
    else:
        brecha_cat = 'Crítico'
    hallazgos.append([str(h_num), f'Brecha {brecha_str}',
                      f'Venta real ${venta_real:.2f} vs concilio ${concilio:.2f}', brecha_cat])

    return {
        # Calculados
        'concilio':      concilio,
        'venta_real':    venta_real,
        'brecha':        brecha,
        'brecha_str':    brecha_str,
        'tipo_brecha':   tipo,
        'sem_bg':        sem_bg,
        'sem_fg':        sem_fg,
        'sem_label':     sem_label,
        't_val':         round(t_val, 2),
        'nt_val':        round(nt_val, 2),
        'ajuste':        round(ajuste, 2),
        'hd_nt':         hd_nt,
        'sod_nt':        sod_nt,
        'lay_nt':        lay_nt,
        'hd_adj':        hd_adj,
        'sod_adj':       sod_adj,
        'lay_adj':       lay_adj,
        't_hd_u':        t_hd_u,
        't_sod_u':       t_sod_u,
        't_lay_u':       t_lay_u,
        'u_inventario':  inv.get('hd',0)+inv.get('sodas',0)+inv.get('lays',0)+t.get('alitas',0),
        'u_ticket':      t_hd_u + t_sod_u + t_lay_u + t.get('alitas',0),
        'pan_sal_nota':  pan_sal_nota,
        'pan_sal_status':pan_sal_status,
        'diff_pan':      diff_pan,
        'vf':            vf,
        'tvi':           tvi,
        'hallazgos':     hallazgos,
        'corte_ef':      cfg['corte_efectivo'],
    }

# ══════════════════════════════════════════════════════════════════════════════
# MOTOR DE PRESENTACIÓN — genera el PDF desde el resultado calculado
# ══════════════════════════════════════════════════════════════════════════════
def generar_reporte(cfg):
    c = calcular(cfg)
    d = cfg

    doc = SimpleDocTemplate(cfg['archivo'], pagesize=letter,
        rightMargin=0.75*inch, leftMargin=0.75*inch,
        topMargin=0.75*inch,   bottomMargin=0.75*inch)
    story = []

    # ── ENCABEZADO ────────────────────────────────────────────────
    ht = Table([[
        Paragraph('<b>SIVAR DOGS</b>',
            ParagraphStyle('hh',fontName='Helvetica-Bold',fontSize=22,textColor=C_WHITE)),
        Paragraph('Parque San Martín · Santa Tecla, El Salvador',
            ParagraphStyle('hs',fontName='Helvetica',fontSize=9,
            textColor=colors.HexColor('#a8dadc'),alignment=TA_RIGHT)),
    ]], colWidths=[W*0.5, W*0.5],
    style=TableStyle([('BACKGROUND',(0,0),(-1,-1),C_DARK),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),16),('BOTTOMPADDING',(0,0),(-1,-1),16),
        ('LEFTPADDING',(0,0),(-1,-1),18),('RIGHTPADDING',(0,0),(-1,-1),18)]))
    story.append(ht)
    story.append(Spacer(1,10))

    tt = Table([[
        Paragraph('Reporte de Cierre Diario', s_title),
        Paragraph(f"{d['dia_nombre']} · {d['fecha']}",
            ParagraphStyle('dt',fontName='Helvetica',fontSize=10,textColor=C_MID,alignment=TA_RIGHT)),
    ]], colWidths=[W*0.57, W*0.43],
    style=TableStyle([('VALIGN',(0,0),(-1,-1),'BOTTOM'),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    story.append(tt)
    story.append(Spacer(1,4))
    story.append(Paragraph(
        f"Vendedora: {d['vendedora']}  ·  Cierre: {d['hora_cierre']}  ·  Método: Concilio inventario vs caja  ·  v5.1 motor automático",
        s_small))
    story.append(Spacer(1,8))

    # ── KPIs ──────────────────────────────────────────────────────
    kpis_bloque = [
        *sh('Resumen Ejecutivo — KPIs Oficiales'),
        Spacer(1,6),
        kpi_row_4(
            kpi_card('Caja Real',           f"${c['venta_real']:.2f}",   'Fórmula corte+gastos−vuelto', C_ROW,  C_DARK,   C_DARK),
            kpi_card('Venta Oficial',        f"${c['concilio']:.2f}",     'Concilio inventario',         C_BLUE, C_BLUE_T, C_BLUE_T),
            kpi_card('Tickets Registrados',  f"${c['t_val']:.2f}",        f"{c['u_ticket']} ítems",      C_ROW,  C_MID,    C_MID),
            kpi_card('Brecha Diaria',         c['brecha_str'],             f"{c['sem_label']} · {c['tipo_brecha']}", c['sem_bg'], c['sem_fg'], c['sem_fg']),
        ),
        Spacer(1,10),
    ]

    # ── FLUJO PASO 1 ──────────────────────────────────────────────
    BW = (W - 3*0.28*inch) / 3
    inv = d['inventario_vendido']
    inv_det = (f"{inv.get('hd',0)} hotdogs\n"
               f"{inv.get('sodas',0)} sodas\n"
               f"{inv.get('lays',0)} lays")
    tick_det = (f"{c['t_hd_u']} hotdogs\n"
                f"{c['t_sod_u']} sodas\n"
                f"{c['t_lay_u']} lays")
    nt_lines = []
    if c['hd_nt']>0:  nt_lines.append(f"{c['hd_nt']} HD × $1.50 = ${c['hd_nt']*1.50:.2f}")
    if c['sod_nt']>0: nt_lines.append(f"{c['sod_nt']} S × $1.00 = ${c['sod_nt']:.2f}")
    if c['lay_nt']>0: nt_lines.append(f"{c['lay_nt']} L × $0.25 = ${c['lay_nt']*0.25:.2f}")
    if c['hd_adj']>0: nt_lines.append(f"−{c['hd_adj']} HD ticket extra")
    if not nt_lines:  nt_lines = ['Sin diferencias']
    nt_det = '\n'.join(nt_lines)

    flujo_1 = [
        Paragraph('Paso 1 — ¿Cuánto faltó registrar en tickets?', s_step),
        Table([[
            bloque('Inventario físico',      f"{c['u_inventario']} u / ${c['concilio']:.2f}",   inv_det,  colors.HexColor('#e8f4f8'), C_MID,    BW),
            op('−'),
            bloque('Tickets registrados',    f"{c['u_ticket']} u / ${c['t_val']:.2f}",           tick_det, C_ROW,                      C_MID,    BW),
            op('='),
            bloque('No ticketeados\n(clásicos $1.50)',f"{c['hd_nt']+c['sod_nt']+c['lay_nt']} u / ${c['nt_val']:.2f}", nt_det, colors.HexColor('#fff8e1'), C_WARN_T, BW),
        ]], colWidths=[BW,0.28*inch,BW,0.28*inch,BW],
        style=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),1),('RIGHTPADDING',(0,0),(-1,-1),1),
            ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])),
        Spacer(1,8),
    ]

    # ── FLUJO PASO 2 ──────────────────────────────────────────────
    BW2 = (W - 4*0.28*inch) / 4
    flujo_2 = [
        Paragraph('Paso 2 — ¿Cuánto vendimos realmente vs lo que entró a caja?', s_step),
        Table([[
            bloque('Tickets\nregistrados',    f"${c['t_val']:.2f}",     f"{c['u_ticket']} ítems",      C_ROW,                       C_MID,    BW2),
            op('+'),
            bloque('No ticketeados\nconciliados',f"+${c['nt_val']:.2f}",f"{c['hd_nt']+c['sod_nt']+c['lay_nt']} ítems estimados",colors.HexColor('#fff8e1'),C_WARN_T,BW2),
            op('='),
            bloque('VENTA OFICIAL\n(Concilio)',  f"${c['concilio']:.2f}",f"{c['u_inventario']} productos",C_BLUE,    C_BLUE_T, BW2),
            op('vs'),
            bloque('Caja Real\n(Fórmula)',       f"${c['venta_real']:.2f}",'Corte+Gastos−Vuelto',        C_ROW,     C_DARK,   BW2),
            op('='),
            bloque(f'RESULTADO\n{c["tipo_brecha"]}', c['brecha_str'], c['sem_label'],                   c['sem_bg'],c['sem_fg'],BW2),
        ]], colWidths=[BW2,0.28*inch,BW2,0.28*inch,BW2,0.28*inch,BW2,0.28*inch,BW2],
        style=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),1),('RIGHTPADDING',(0,0),(-1,-1),1),
            ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])),
        Spacer(1,5),
        Paragraph('Brecha $0.00 = día perfecto  ·  (+) sobrante = Otros ingresos no identificados  ·  (−) faltante = Diferencias de caja', s_warn),
        Spacer(1,6),
    ]

    story.append(KeepTogether(kpis_bloque + flujo_1))
    story.append(KeepTogether(flujo_2))

    # ── RESUMEN VENTA OFICIAL ─────────────────────────────────────
    vf_rows = [['Producto','Origen','Unidades','Precio','Total']]
    for row in c['vf']:
        vf_rows.append(row)
    vf_total_u = sum(int(r[2]) for r in c['vf'])
    vf_total_v = sum(float(r[4].replace('$','')) for r in c['vf'])
    vf_rows.append(['VENTA OFICIAL DEL DÍA','',str(vf_total_u),'',f'${vf_total_v:.2f}'])

    vf_t = Table(vf_rows, colWidths=[1.7*inch,2.1*inch,0.7*inch,0.8*inch,0.7*inch])
    vf_ts = ts()
    vf_ts.add('ALIGN',(2,0),(-1,-1),'CENTER')
    n = len(vf_rows)-1
    vf_ts.add('BACKGROUND',(0,n),(-1,n),C_DARK)
    vf_ts.add('TEXTCOLOR',(0,n),(-1,n),C_WHITE)
    vf_ts.add('FONTNAME',(0,n),(-1,n),'Helvetica-Bold')
    for i,row in enumerate(vf_rows[1:],1):
        if 'No ticket' in str(row[1]) or 'Inventario' in str(row[1]):
            vf_ts.add('TEXTCOLOR',(1,i),(1,i),C_WARN_T)
    vf_t.setStyle(vf_ts)

    # Resumen limpio
    rv_rows = [['Producto','Unidades','Total']]
    for row in c['vf']:
        rv_rows.append([row[0], row[2], row[4]])
    rv_rows.append(['TOTAL VENTA OFICIAL', str(vf_total_u), f'${vf_total_v:.2f}'])
    rv_t = Table(rv_rows, colWidths=[W*0.55, W*0.20, W*0.25])
    rv_ts = TableStyle([
        ('BACKGROUND',(0,0),(-1,0),C_MID),('TEXTCOLOR',(0,0),(-1,0),C_WHITE),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),9),
        ('FONTNAME',(0,1),(-1,-2),'Helvetica'),
        ('ROWBACKGROUNDS',(0,1),(-1,-2),[C_WHITE,C_ROW]),
        ('GRID',(0,0),(-1,-1),0.3,GRID),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),
        ('ALIGN',(1,0),(-1,-1),'CENTER'),
        ('BACKGROUND',(0,-1),(-1,-1),C_DARK),('TEXTCOLOR',(0,-1),(-1,-1),C_WHITE),
        ('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold'),('FONTSIZE',(0,-1),(-1,-1),10),
        ('TOPPADDING',(0,-1),(-1,-1),9),('BOTTOMPADDING',(0,-1),(-1,-1),9),
    ])
    rv_t.setStyle(rv_ts)

    story.append(KeepTogether([
        *sh('Venta Final del Día — Detalle por Producto'),
        Spacer(1,4),
        Paragraph('Tickets registrados + no ticketeados conciliados. Número oficial del día.', s_note),
        Spacer(1,5), vf_t, Spacer(1,4),
        Paragraph(f"Venta oficial: ${vf_total_v:.2f}  ·  Brecha {c['brecha_str']} → {'Otros Ingresos No Identificados' if c['brecha']>=0 else 'Diferencias de Caja'} (contable).", s_note),
        Spacer(1,6),
    ]))
    story.append(KeepTogether([
        *sh('Resumen de Venta Oficial'),
        Spacer(1,4), rv_t, Spacer(1,4),
    ]))

    # ── SECCIÓN 1: INVENTARIO ─────────────────────────────────────
    inv_rows = [['Producto','Inicio','Compras','Disponible','Cortesías','Pérdida','Sobra','Vendido']]
    for row in d['inventario']:
        inv_rows.append(row)
    inv_t = Table(inv_rows, colWidths=[1.5*inch,0.6*inch,0.7*inch,0.8*inch,0.7*inch,0.6*inch,0.6*inch,0.5*inch])
    inv_ts = ts()
    for i,row in enumerate(inv_rows[1:],1):
        if row[0]=='HOTDOGS TOTAL':
            inv_ts.add('BACKGROUND',(0,i),(-1,i),colors.HexColor('#e8f4f8'))
            inv_ts.add('FONTNAME',(0,i),(-1,i),'Helvetica-Bold')
        # Fix 3: Pan vs Sal rojo si diferencia crítica
        if row[0]=='Pan Sanfran' and c.get('diff_pan',0) > 2:
            inv_ts.add('BACKGROUND',(0,i),(-1,i),C_RED_L)
            inv_ts.add('TEXTCOLOR',(0,i),(-1,i),C_RED_T)
        # Fix 2: [REVISAR] — marcar en ámbar si el valor es 0 y está en lista revisar
        for campo in cfg.get('revisar',[]):
            if campo.lower() in row[0].lower():
                inv_ts.add('BACKGROUND',(0,i),(-1,i),C_WARN)
                inv_ts.add('TEXTCOLOR',(0,i),(0,i),C_WARN_T)
    inv_ts.add('ALIGN',(1,0),(-1,-1),'CENTER')
    inv_t.setStyle(inv_ts)

    # Pan vs Sal nota con color según severidad
    if c.get('diff_pan',0) == 0:
        pan_sal_style = s_note
    elif c.get('diff_pan',0) <= 2:
        pan_sal_style = s_warn
    else:
        pan_sal_style = ParagraphStyle('crit',fontName='Helvetica-Bold',fontSize=8,
                                        textColor=C_RED_T,leading=12)

    story.append(KeepTogether([*sh('1. Control de Inventario'), inv_t, Spacer(1,4),
        Paragraph(c['pan_sal_nota'], pan_sal_style)]))

    # ── SECCIÓN 2: TICKETS ────────────────────────────────────────
    tick_rows = [['Producto','Cantidad','Precio','Subtotal','Nota']]
    for row in d['tickets_tabla']:
        tick_rows.append(row)
    tick_t = Table(tick_rows, colWidths=[2.1*inch,0.7*inch,0.7*inch,0.8*inch,2.7*inch])
    tick_ts = ts(C_MID)
    for i,row in enumerate(tick_rows[1:],1):
        if row[0].startswith('TOTAL'):
            tick_ts.add('FONTNAME',(0,i),(-1,i),'Helvetica-Bold')
            tick_ts.add('BACKGROUND',(0,i),(-1,i),C_ROW)
        if 'Descartado' in str(row[4]):
            # Fix 4: fila completa en rojo, no solo texto
            tick_ts.add('BACKGROUND',(0,i),(-1,i),C_RED_L)
            tick_ts.add('TEXTCOLOR',(0,i),(-1,i),C_RED_T)
            tick_ts.add('FONTNAME',(0,i),(-1,i),'Helvetica-Bold')
        # Fix 2: [REVISAR] en tickets
        if '[REVISAR]' in str(row[4]):
            tick_ts.add('BACKGROUND',(0,i),(-1,i),C_WARN)
            tick_ts.add('TEXTCOLOR',(0,i),(-1,i),C_WARN_T)
    tick_ts.add('ALIGN',(1,0),(3,-1),'CENTER')
    tick_t.setStyle(tick_ts)
    story.append(KeepTogether([*sh('2. Tickets Registrados'), tick_t, Spacer(1,4),
        Paragraph(d.get('nota_tickets',''), s_note)]))

    # ── SECCIÓN 3: TVI ────────────────────────────────────────────
    tvi_rows = [['Producto','Inventario','Ticket','Diferencia','Dif. ($)']]
    for row in c['tvi']:
        tvi_rows.append(row)
    tvi_t = Table(tvi_rows, colWidths=[2.1*inch,1.0*inch,1.0*inch,1.1*inch,1.8*inch])
    tvi_ts = ts()
    for i,row in enumerate(tvi_rows[1:],1):
        if 'Pan vs' in str(row[0]):
            tvi_ts.add('BACKGROUND',(0,i),(-1,i),C_WARN)
            tvi_ts.add('FONTNAME',(0,i),(-1,i),'Helvetica-Bold')
        if row[0].startswith('TOTAL'):
            tvi_ts.add('BACKGROUND',(0,i),(-1,i),C_BLUE)
            tvi_ts.add('TEXTCOLOR',(0,i),(-1,i),C_BLUE_T)
            tvi_ts.add('FONTNAME',(0,i),(-1,i),'Helvetica-Bold')
    tvi_ts.add('ALIGN',(1,0),(-1,-1),'CENTER')
    tvi_t.setStyle(tvi_ts)
    story.append(KeepTogether([*sh('3. Ticket vs Inventario'), tvi_t, Spacer(1,4),
        Paragraph(d.get('nota_tvi','Inventario manda sobre tickets en todos los casos.'), s_note)]))

    # ── SECCIÓN 4: INGRESOS Y GASTOS ──────────────────────────────
    max_r = max(len(d['ingresos']), len(d['gastos']))
    ing_p = d['ingresos'] + [['','']]*( max_r-len(d['ingresos']))
    gst_p = d['gastos']   + [['','']]*( max_r-len(d['gastos']))
    ig_rows = [['INGRESOS','Monto','GASTOS','Monto']]
    for i in range(max_r):
        ig_rows.append([ing_p[i][0],ing_p[i][1],gst_p[i][0],gst_p[i][1]])
    ig_rows.append(['Subtotal ingresos', f"${c['corte_ef']+d.get('pos',0)+d.get('pedidosya',0)+d.get('transferencia',0):.2f}", 'Total gastos', f"${d['total_gastos']:.2f}"])
    ig_rows.append(['Vuelto inicial', f"−${d['vuelto_inicial']:.2f}", '', ''])
    ig_rows.append(['VENTA REAL', f"${c['venta_real']:.2f}", '', ''])
    ig_t = Table(ig_rows, colWidths=[2.1*inch,1.1*inch,2.1*inch,1.7*inch])
    ig_ts = ts()
    ig_ts.add('BACKGROUND',(0,0),(1,0),C_MID)
    ig_ts.add('BACKGROUND',(2,0),(3,0),C_ACCENT)
    n_ig = len(ig_rows)
    ig_ts.add('FONTNAME',(0,n_ig-3),(-1,n_ig-3),'Helvetica-Bold')
    ig_ts.add('BACKGROUND',(0,n_ig-1),(1,n_ig-1),C_DARK)
    ig_ts.add('TEXTCOLOR',(0,n_ig-1),(1,n_ig-1),C_WHITE)
    ig_ts.add('FONTNAME',(0,n_ig-1),(1,n_ig-1),'Helvetica-Bold')
    ig_ts.add('ALIGN',(1,0),(1,-1),'RIGHT')
    ig_ts.add('ALIGN',(3,0),(3,-1),'RIGHT')
    ig_t.setStyle(ig_ts)

    var = d['vuelto_final'] - d['vuelto_inicial']

    # Fix 5: tendencia de caja con historial si existe
    historial = cfg.get('historial_vueltos', [])  # lista de (dia, monto)
    tendencia_str = ' → '.join([f"{dia} ${monto:.2f}" for dia,monto in historial])
    if tendencia_str:
        tendencia_str += f' → Hoy ${d["vuelto_final"]:.2f}'
    else:
        tendencia_str = cfg.get('nota_caja', '')

    caja_rows = [['Concepto','Monto','Observación'],
        ['Caja base ideal','$45.00','Fondo estándar del negocio'],
        ['Vuelto inicial', f"${d['vuelto_inicial']:.2f}", d.get('obs_vuelto_ini','')],
        ['Vuelto final',   f"${d['vuelto_final']:.2f}",  d.get('obs_vuelto_fin','')],
        ['Variación',      f"{var:+.2f}",                d.get('obs_variacion','')],
    ]
    caja_t = Table(caja_rows, colWidths=[2.0*inch,1.0*inch,4.0*inch])
    caja_ts = ts(C_MID)
    var_bg = C_GREEN if var>=0 else C_RED_L
    var_fg = C_GREEN_T if var>=0 else C_RED_T
    caja_ts.add('BACKGROUND',(0,4),(-1,4),var_bg)
    caja_ts.add('TEXTCOLOR',(1,4),(1,4),var_fg)
    caja_ts.add('FONTNAME',(0,4),(-1,4),'Helvetica-Bold')
    caja_ts.add('ALIGN',(1,0),(1,-1),'CENTER')
    caja_t.setStyle(caja_ts)
    formula = (f"Fórmula: Corte ${d['corte_efectivo']:.2f} + POS ${d.get('pos',0):.2f} + "
               f"PedidosYa ${d.get('pedidosya',0):.2f} + Gastos ${d['total_gastos']:.2f} "
               f"− Vuelto ${d['vuelto_inicial']:.2f} = ${c['venta_real']:.2f} ✓")
    story.append(KeepTogether([
        *sh('4. Ingresos y Gastos del Día'), ig_t,
        Spacer(1,4), Paragraph(formula, s_small),
        Spacer(1,8),
        Paragraph('Estado de Caja', ParagraphStyle('sc2',fontName='Helvetica-Bold',fontSize=9,textColor=C_DARK,spaceAfter=3)),
        caja_t, Spacer(1,4),
        Paragraph(tendencia_str, s_note),
    ]))

    # ── SECCIÓN 5: ANÁLISIS FINAL ─────────────────────────────────
    sem_tbl = Table([
        ['Tipo','Rango','Estado','Significado'],
        ['Sobrante (+)','$0 — $5',  '🟢 Verde',   'Normal — diferencia de precio o conteo mínimo'],
        ['Sobrante (+)','$5 — $10', '🟡 Amarillo','Monitorear — posible autopréstamo del vendedor'],
        ['Sobrante (+)','$10 — $15','🟠 Naranja',  'Alerta — investigar causa recurrente'],
        ['Sobrante (+)','>$15',      '🔴 Rojo',    'Acción inmediata'],
        ['Faltante (−)','$0 — $5',  '🟡 Amarillo','Revisar conteo — faltante siempre más grave'],
        ['Faltante (−)','$5 — $10', '🟠 Naranja',  'Investigar causa específica'],
        ['Faltante (−)','>$10',      '🔴 Rojo',    'Acción inmediata'],
    ], colWidths=[1.1*inch,1.0*inch,1.1*inch,3.8*inch])
    s_ts = ts(C_DARK)
    s_ts.add('BACKGROUND',(0,1),(-1,1),C_GREEN)
    s_ts.add('BACKGROUND',(0,2),(-1,2),C_WARN)
    s_ts.add('BACKGROUND',(0,3),(-1,3),C_ORANGE)
    s_ts.add('BACKGROUND',(0,4),(-1,4),C_RED_L)
    s_ts.add('BACKGROUND',(0,5),(-1,5),C_WARN)
    s_ts.add('BACKGROUND',(0,6),(-1,6),C_ORANGE)
    s_ts.add('BACKGROUND',(0,7),(-1,7),C_RED_L)
    s_ts.add('ALIGN',(1,0),(2,-1),'CENTER')
    sem_tbl.setStyle(s_ts)

    hall_rows = [['#','Hallazgo','Conclusión','Estado']]
    for row in c['hallazgos']:
        hall_rows.append(row)
    hall_t = Table(hall_rows, colWidths=[0.3*inch,2.2*inch,2.9*inch,1.6*inch])
    hall_ts = ts(C_MID)
    for i,row in enumerate(hall_rows[1:],1):
        est = str(row[3])
        if est == 'Resuelto':
            hall_ts.add('BACKGROUND',(0,i),(-1,i),C_GREEN)
            hall_ts.add('TEXTCOLOR',(3,i),(3,i),C_GREEN_T)
        elif est == 'Monitorear':
            hall_ts.add('BACKGROUND',(0,i),(-1,i),C_WARN)
            hall_ts.add('TEXTCOLOR',(3,i),(3,i),C_WARN_T)
        elif est == 'Pendiente':
            hall_ts.add('BACKGROUND',(0,i),(-1,i),C_ORANGE)
            hall_ts.add('TEXTCOLOR',(3,i),(3,i),C_ORANGE_T)
        elif est == 'Crítico':
            hall_ts.add('BACKGROUND',(0,i),(-1,i),C_RED_L)
            hall_ts.add('TEXTCOLOR',(3,i),(3,i),C_RED_T)
        hall_ts.add('FONTNAME',(3,i),(3,i),'Helvetica-Bold')
    hall_t.setStyle(hall_ts)

    story.append(KeepTogether([
        *sh('5. Análisis Final'),
        Paragraph(f'Resultado del día: Brecha {c["brecha_str"]} — {c["sem_label"]}',
            ParagraphStyle('res',fontName='Helvetica-Bold',fontSize=9,textColor=c['sem_fg'],spaceAfter=4)),
        sem_tbl, Spacer(1,8),
        Paragraph('Hallazgos y seguimiento', ParagraphStyle('hh',fontName='Helvetica-Bold',fontSize=9,textColor=C_DARK,spaceAfter=3)),
        hall_t, Spacer(1,4),
        Paragraph(d.get('accion_final',''), s_warn),
    ]))

    # ── FOOTER ────────────────────────────────────────────────────
    story.append(Spacer(1,12))
    story.append(HRFlowable(width='100%',thickness=0.5,color=C_MUTED))
    story.append(Spacer(1,4))
    story.append(Table([[
        Paragraph('Sivar Dogs · Control Operativo · v5.1 motor automático', s_small),
        Paragraph(f"Documento confidencial · Uso interno · {d['fecha']}",
            ParagraphStyle('fr',fontName='Helvetica',fontSize=8,textColor=C_MUTED,alignment=TA_RIGHT)),
    ]], colWidths=[W*0.5,W*0.5],
    style=TableStyle([('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)])))

    doc.build(story)
    print(f"✓ {cfg['archivo'].split('/')[-1]}  |  Concilio ${c['concilio']:.2f}  |  Venta ${c['venta_real']:.2f}  |  Brecha {c['brecha_str']} {c['sem_label']}")


# ══════════════════════════════════════════════════════════════════════════════
# DATOS — 10 INPUTS CRUDOS POR DÍA
# ══════════════════════════════════════════════════════════════════════════════

SABADO = dict(
    archivo='/home/claude/Reporte_Sabado_SivarDogs.pdf',
    dia_nombre='Sábado', fecha='15 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='8:45 p.m.',
    # 10 inputs crudos
    tickets=dict(clasico=160,chilidog=0,combo_clasico=28,soda_ind=45,lays_ind=3,alitas=1),
    inventario_vendido=dict(hd=222, sodas=84, lays=31),
    pan_vendido=226,
    corte_efectivo=246.38, pos=6.50, pedidosya=0, transferencia=0,
    total_gastos=211.27, vuelto_inicial=24.15, vuelto_final=43.35,
    # Contexto para secciones de presentación
    inventario=[
        ['Pan Sanfran','20','288','308','3','0','79','226'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','65','208','273','4','0','47','222'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','222'],
        ['Sodas','26','72','98','3','0','11','84'],
        ['Lays','3','36','39','0','0','8','31'],
        ['Alitas','2','0','2','0','0','1','1'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','160','$1.50','$240.00',''],
        ['Combo Clásico','28','$2.75','$77.00','28 HD+28 S+28 L'],
        ['Bebidas latas individual','45','$1.00','$45.00',''],
        ['Lays individual','3','$0.50','$1.50',''],
        ['Alitas','1','$4.00','$4.00',''],
        ['TOTAL TICKET','237','','$367.50','188 HD + 73 S + 31 L'],
    ],
    nota_tickets='Sábado excepcional — 222 hotdogs vendidos.',
    obs_vuelto_ini='Inicio del día', obs_vuelto_fin='Queda para el lunes',
    obs_variacion='Caja repuesta +$19.20',
    nota_caja='Tendencia: Sáb $43.35 → siguiente día.',
    ingresos=[['Corte efectivo total','$246.38'],['POS','$6.50'],['PedidosYa','$0.00'],['Transferencia','$0.00']],
    gastos=[['Insumos varios','$211.27']],
    accion_final='Día excepcional. Confirmar con Vilma la diferencia Pan(226) vs Sal(222).',
)

LUNES = dict(
    archivo='/home/claude/Reporte_Lunes_SivarDogs.pdf',
    dia_nombre='Lunes', fecha='16 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='9:15 p.m.',
    tickets=dict(clasico=71,chilidog=15,combo_clasico=3,soda_ind=26,lays_ind=1),
    inventario_vendido=dict(hd=114, sodas=36, lays=4),
    pan_vendido=113,
    corte_efectivo=151.49, pos=0, pedidosya=0, transferencia=0,
    total_gastos=112.10, vuelto_inicial=43.35, vuelto_final=16.40,
    inventario=[
        ['Pan Sanfran','81','144','225','3','0','109','113'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','47','64','111','3','0','0','108'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','114'],
        ['Sodas','11','24','35','0','0','14','21'],
        ['Lays','8','12','20','0','0','11','9'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','71','$1.50','$106.50',''],
        ['Hotdog Chilidog individual','15','$2.00','$30.00',''],
        ['Combo Clásico','3','$2.75','$8.25','3 HD+3 S+3 L'],
        ['Bebidas latas individual','26','$1.00','$26.00',''],
        ['Lays individual','1','$0.50','$0.50',''],
        ['TOTAL TICKET','116','','$171.25','89 HD+29 S+4 L'],
    ],
    nota_tickets='Lunes — segundo día más fuerte de la semana.',
    obs_vuelto_ini='Heredado del sábado', obs_vuelto_fin='Queda para el martes',
    obs_variacion='Caja cayó — pagos del día',
    nota_caja='Sáb $43.35 → Lun $16.40. Caja cayó por pagos.',
    ingresos=[['Corte efectivo total','$151.49'],['POS','$0.00'],['PedidosYa','$0.00']],
    gastos=[['Selectos','$4.06'],['Despensa','$4.04'],['Milagro','$6.65'],['Super','$2.35'],['Pagos','$75.00'],['Vilma','$20.00']],
    accion_final='Día sano. Reponer fondo de caja prioritario.',
)

MARTES = dict(
    archivo='/home/claude/Reporte_Martes_SivarDogs.pdf',
    dia_nombre='Martes', fecha='17 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='8:20 p.m.',
    tickets=dict(clasico=33,chilidog=3,combo_clasico=1,soda_ind=9,lays_ind=1),
    inventario_vendido=dict(hd=44, sodas=11, lays=1),
    pan_vendido=44,
    corte_efectivo=87.85, pos=0, pedidosya=0, transferencia=0,
    total_gastos=10.00, vuelto_inicial=16.40, vuelto_final=12.85,
    inventario=[
        ['Pan Sanfran','35','0','35','2','0','35','44'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','0','120','120','2','0','86','32'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','44'],
        ['Sodas','14','0','14','0','0','3','11'],
        ['Lays','11','0','11','0','0','10','1'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','33','$1.50','$49.50',''],
        ['Hotdog Chilidog individual','3','$2.00','$6.00',''],
        ['Combo Clásico','1','$2.75','$2.75','1 HD+1 S+1 L'],
        ['Bebidas latas individual','9','$1.00','$9.00',''],
        ['Lays individual','1','$0.50','$0.50','— 1 lays sin respaldo físico, ajuste aplicado'],
        ['TOTAL TICKET','47','','$67.75','37 HD+10 S+1 L'],
    ],
    nota_tickets='1 lays individual ticketeada sin respaldo físico — inventario = 1 (usada en combo). Ajuste de $0.50 aplicado.',
    nota_tvi='Lays inventario = 1. Ticket pide 2 (1 combo + 1 individual). Ajuste: −1 lays × $0.50.',
    obs_vuelto_ini='Heredado del lunes', obs_vuelto_fin='Queda para el miércoles',
    obs_variacion='Caja sigue bajando',
    nota_caja='Sáb $43.35 → Lun $16.40 → Mar $12.85. Reponer urgente.',
    ingresos=[['Corte efectivo total','$87.85'],['POS','$0.00'],['PedidosYa','$0.00']],
    gastos=[['Vilma','$10.00']],
    accion_final='Día sano. Reponer fondo antes del jueves.',
)

MIERCOLES = dict(
    archivo='/home/claude/Reporte_Miercoles_v2_SivarDogs.pdf',
    dia_nombre='Miércoles', fecha='18 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='9:10 p.m.',
    tickets=dict(clasico=30,chilidog=12,combo_clasico=1,soda_ind=8,lays_ind=0),
    inventario_vendido=dict(hd=48, sodas=12, lays=1),
    pan_vendido=49,
    corte_efectivo=73.20, pos=0, pedidosya=0, transferencia=0,
    total_gastos=35.30, vuelto_inicial=12.85, vuelto_final=33.20,
    inventario=[
        ['Pan Sanfran','35','144','179','4','0','126','49'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','86','160','246','4','0','194','48'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','48'],
        ['Sodas','3','24','27','1','0','14','12'],
        ['Lays','10','0','10','0','0','9','1'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','30','$1.50','$45.00',''],
        ['Hotdog Chilidog individual','12','$2.00','$24.00',''],
        ['Combo Clásico','1','$2.75','$2.75','1 HD+1 S+1 L'],
        ['Combo Especialidad','0','$3.25','$0.00','Descartado — sin lays física disponible'],
        ['Bebidas latas individual','8','$1.00','$8.00',''],
        ['TOTAL TICKET','51','','$79.75','43 HD+9 S+1 L'],
    ],
    nota_tickets='Combo Especialidad descartado: lays inventario = 1 ya usada en Combo Clásico.',
    obs_vuelto_ini='Heredado del martes — caja venía baja',
    obs_vuelto_fin='Queda para el jueves',
    obs_variacion='Primera subida de la semana +$20.35',
    nota_caja='Sáb $43.35 → Lun $16.40 → Mar $12.85 → Mié $33.20. Recuperándose.',
    ingresos=[['Corte efectivo total','$73.20'],['POS','$0.00'],['PedidosYa','$0.00']],
    gastos=[['Salchicha','$10.00'],['Gaseosas','$15.30'],['Vilma','$10.00']],
    accion_final='Confirmar con Vilma combo especialidad y chilidogs no ticketeados.',
)

JUEVES = dict(
    archivo='/home/claude/Reporte_Jueves_SivarDogs.pdf',
    dia_nombre='Jueves', fecha='19 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='7:25 p.m.',
    tickets=dict(clasico=39,chilidog=6,combo_clasico=1,soda_ind=7,lays_ind=0),
    inventario_vendido=dict(hd=44, sodas=8, lays=1),
    pan_vendido=44,
    corte_efectivo=63.96, pos=0, pedidosya=0, transferencia=0,
    total_gastos=44.99, vuelto_inicial=33.20, vuelto_final=18.95,
    inventario=[
        ['Pan Sanfran','80','0','80','2','0','24','44'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','148','0','148','2','0','96','44'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','44'],
        ['Sodas','30','24','54','0','0','30','8'],
        ['Lays','8','0','8','0','0','7','1'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','39','$1.50','$58.50',''],
        ['Hotdog Chilidog individual','6','$2.00','$12.00',''],
        ['Combo Clásico','1','$2.75','$2.75','1 HD+1 S+1 L'],
        ['Bebidas latas individual','7','$1.00','$7.00',''],
        ['TOTAL TICKET','53','','$80.25','46 HD+8 S+1 L'],
    ],
    nota_tickets='Inventario: 44 HD. Ticket: 46 HD. 2 tickets sin producto físico — ajuste aplicado.',
    obs_vuelto_ini='Heredado del miércoles',
    obs_vuelto_fin='Queda para el viernes',
    obs_variacion='Caja bajó — acceso $20',
    nota_caja='Mié $33.20 → Jue $18.95. Caja fluctuando.',
    ingresos=[['Corte efectivo total','$63.96'],['POS','$0.00'],['PedidosYa','$0.00']],
    gastos=[['Sodas','$14.99'],['Acceso','$20.00'],['Vilma','$10.00']],
    accion_final='Confirmar con Vilma: ¿hubo devolución o ticket anulado? Los 2 tickets extra explican el faltante.',
)

VIERNES = dict(
    archivo='/home/claude/Reporte_Viernes_SivarDogs.pdf',
    dia_nombre='Viernes', fecha='20 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='8:50 p.m.',
    tickets=dict(clasico=52,chilidog=2,combo_clasico=0,soda_ind=22,lays_ind=0),
    inventario_vendido=dict(hd=53, sodas=19, lays=0),
    pan_vendido=53,
    corte_efectivo=55.30, pos=0, pedidosya=0, transferencia=0,
    total_gastos=62.15, vuelto_inicial=18.95, vuelto_final=5.30,
    inventario=[
        ['Pan Sanfran','24','0','24','3','0','24','53'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','92','0','92','3','0','92','53'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','53'],
        ['Sodas','30','0','30','0','0','11','19'],
        ['Lays','8','0','8','0','0','8','0'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','52','$1.50','$78.00',''],
        ['Hotdog Chilidog individual','2','$2.00','$4.00',''],
        ['Bebidas latas individual','22','$1.00','$22.00','— 3 sodas extra sin respaldo, ajuste aplicado'],
        ['TOTAL TICKET','76','','$104.00','54 HD+22 S'],
    ],
    nota_tickets='54 HD ticket vs 53 inventario (1 ajuste). 22 sodas ticket vs 19 inventario (3 ajuste).',
    obs_vuelto_ini='Heredado del jueves',
    obs_vuelto_fin='Queda para el sábado — CRÍTICO',
    obs_variacion='Caja cayó a $5.30 — urgente reponer',
    nota_caja='Jue $18.95 → Vie $5.30. URGENTE reponer fondo antes del sábado.',
    ingresos=[['Corte efectivo total','$55.30'],['POS','$0.00'],['PedidosYa','$0.00']],
    gastos=[['Acceso','$40.00'],['Vilma','$10.00'],['Gas','$12.15']],
    accion_final='URGENTE: reponer caja antes del sábado. Confirmar tickets extra (1 HD + 3 sodas) con Vilma.',
)

SABADO2 = dict(
    archivo='/home/claude/Reporte_Sabado2_SivarDogs.pdf',
    dia_nombre='Sábado', fecha='21 de marzo de 2026',
    vendedora='Vilma Luna', hora_cierre='7:30 p.m.',
    tickets=dict(clasico=72,chilidog=10,combo_clasico=2,combo_esp=1,soda_ind=16,lays_ind=1),
    inventario_vendido=dict(hd=93, sodas=23, lays=6),
    pan_vendido=93,
    corte_efectivo=100.45, pos=8.75, pedidosya=6.00, transferencia=0,
    total_gastos=61.90, vuelto_inicial=5.30, vuelto_final=40.45,
    inventario=[
        ['Pan Sanfran','24','156','180','2','0','85','93'],
        ['Pan Única','0','0','0','0','0','0','0'],
        ['Salchicha Jumbo','92','99','191','2','0','96','93'],
        ['Salchicha Mini Jumbo','120','0','120','0','0','120','0'],
        ['HOTDOGS TOTAL','—','—','—','—','—','—','93'],
        ['Sodas','11','24','35','0','0','12','23'],
        ['Lays','8','0','8','0','0','2','6'],
    ],
    tickets_tabla=[
        ['Hotdog Clásico individual','72','$1.50','$108.00',''],
        ['Hotdog Chilidog individual','10','$2.00','$20.00',''],
        ['Combo Clásico','2','$2.75','$5.50','2 HD+2 S+2 L'],
        ['Combo Especialidad','1','$3.25','$3.25','1 HD+1 S+1 L — lays disponibles ✓'],
        ['Bebidas latas individual','16','$1.00','$16.00',''],
        ['Lays individual','1','$0.50','$0.50',''],
        ['TOTAL TICKET','102','','$153.25','85 HD+19 S+4 L'],
    ],
    nota_tickets='Combos válidos: 3 combos requieren 3 lays, inventario tiene 6. Todos válidos ✓',
    obs_vuelto_ini='Heredado del viernes — caja venía crítica ($5.30)',
    obs_vuelto_fin='Queda para el lunes',
    obs_variacion='Caja se recuperó +$35.15',
    nota_caja='Vie $5.30 → Sáb $40.45. El sábado rescató el fondo.',
    ingresos=[['Corte efectivo total','$100.45'],['POS','$8.75'],['PedidosYa','$6.00'],['Transferencia','$0.00']],
    gastos=[['Compras (pan/soda/sal)','$35.00'],['Pan Lido','$5.60'],['Desechables','$4.45'],['Pizza','$5.55'],['Javier','$1.30'],['Vilma','$10.00']],
    accion_final='Día sano. Sobrante de $2.05 verde. Confirmar con Vilma 8 HD no ticketeados.',
)

# ── GENERAR LOS 7 REPORTES ────────────────────────────────────────────────────
print("Generando 7 reportes con motor de cálculo automático...\n")
for cfg in [SABADO, LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO2]:
    generar_reporte(cfg)
print("\n✅ Todos los reportes generados.")

# ══════════════════════════════════════════════════════════════════════════════
# RESUMEN SEMANAL 15–21 MARZO 2026
# ══════════════════════════════════════════════════════════════════════════════
def generar_resumen_semanal():

    # Calcular todos los días con el motor
    TODOS = [SABADO, LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO2]
    resultados = [calcular(d) for d in TODOS]
    labels = ['Sáb 15','Lun 16','Mar 17','Mié 18','Jue 19','Vie 20','Sáb 21']

    total_vr = sum(r['venta_real']  for r in resultados)
    total_co = sum(r['concilio']    for r in resultados)
    brecha_sem = round(total_vr - total_co, 2)
    sem_bg, sem_fg, sem_label, tipo = semaforo(brecha_sem)
    brecha_str = f"+${brecha_sem:.2f}" if brecha_sem >= 0 else f"-${abs(brecha_sem):.2f}"

    doc = SimpleDocTemplate('/home/claude/Resumen_Semana_SivarDogs.pdf',
        pagesize=letter,
        rightMargin=0.75*inch, leftMargin=0.75*inch,
        topMargin=0.75*inch,   bottomMargin=0.75*inch)
    story = []

    # ── ENCABEZADO ────────────────────────────────────────────────
    ht = Table([[
        Paragraph('<b>SIVAR DOGS</b>', ParagraphStyle('hh',fontName='Helvetica-Bold',fontSize=22,textColor=C_WHITE)),
        Paragraph('Parque San Martín · Santa Tecla, El Salvador',
            ParagraphStyle('hs',fontName='Helvetica',fontSize=9,textColor=colors.HexColor('#a8dadc'),alignment=TA_RIGHT)),
    ]], colWidths=[W*0.5, W*0.5],
    style=TableStyle([('BACKGROUND',(0,0),(-1,-1),C_DARK),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),16),('BOTTOMPADDING',(0,0),(-1,-1),16),
        ('LEFTPADDING',(0,0),(-1,-1),18),('RIGHTPADDING',(0,0),(-1,-1),18)]))
    story.append(ht)
    story.append(Spacer(1,10))

    tt = Table([[
        Paragraph('Resumen Semanal de Operaciones',
            ParagraphStyle('ti',fontName='Helvetica-Bold',fontSize=20,textColor=C_DARK,leading=24)),
        Paragraph('15 — 21 de marzo de 2026',
            ParagraphStyle('dt',fontName='Helvetica',fontSize=10,textColor=C_MID,alignment=TA_RIGHT)),
    ]], colWidths=[W*0.60, W*0.40],
    style=TableStyle([('VALIGN',(0,0),(-1,-1),'BOTTOM'),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    story.append(tt)
    story.append(Spacer(1,4))
    story.append(Paragraph('Vendedora: Vilma Luna  ·  6 días operados  ·  Motor v5.1 cálculo automático', s_small))
    story.append(Spacer(1,10))

    # ── KPIs SEMANALES ────────────────────────────────────────────
    total_hd = sum(d['inventario_vendido']['hd'] for d in TODOS)
    story += sh('Resumen Ejecutivo — KPIs de la Semana')
    story.append(Spacer(1,6))
    story.append(kpi_row_4(
        kpi_card('Hotdogs vendidos',   str(total_hd),      '6 días operados',       C_ROW,   C_DARK,   C_DARK),
        kpi_card('Venta Real total',   f'${total_vr:.2f}', 'Caja acumulada',         C_BLUE,  C_BLUE_T, C_BLUE_T),
        kpi_card('Concilio total',     f'${total_co:.2f}', 'Venta oficial semana',   C_GREEN, C_GREEN_T,C_GREEN_T),
        kpi_card('Brecha semanal',      brecha_str,         f'{sem_label} · {tipo}',  sem_bg,  sem_fg,   sem_fg),
    ))
    story.append(Spacer(1,8))
    story.append(kpi_row_4(
        kpi_card('HD promedio/día',    f'{total_hd/6:.0f}',        'vs histórico 61 HD/día',  C_ROW,  C_DARK,   C_DARK),
        kpi_card('Venta prom/día',     f'${total_vr/6:.2f}',       'vs histórico $116.77/día',C_BLUE, C_BLUE_T, C_BLUE_T),
        kpi_card('Días en verde',      '3 / 6',                    'Lun+Mar+Sáb21 ≤ $5',      C_GREEN,C_GREEN_T,C_GREEN_T),
        kpi_card('Mejor día',          'Sáb 15',                   f'222 HD · $440 caja',      C_ROW,  C_MID,    C_MID),
    ))
    story.append(Spacer(1,10))

    # ── TABLA DÍA A DÍA ──────────────────────────────────────────
    notas_dia = [
        '34 HD no ticket. Mix precios explica sobrante.',
        '25 HD no ticket. Día sano. Caja bajó por pagos.',
        '7 HD no ticket. 1 lays ajustada. Día sano.',
        '5 HD no ticket. Combo esp descartado sin lays.',
        '2 tickets sin producto. Confirmar con Vilma.',
        '1 HD + 3 sodas ticket extra. Faltante mínimo.',
        '8 HD no ticket. POS $8.75 + PedidosYa $6. ✓',
    ]
    sem_dia = [
        (C_ORANGE, C_ORANGE_T), (C_GREEN, C_GREEN_T), (C_GREEN, C_GREEN_T),
        (C_WARN, C_WARN_T),     (C_WARN, C_WARN_T),   (C_WARN, C_WARN_T),
        (C_GREEN, C_GREEN_T),
    ]

    cw_d = [1.15*inch,0.65*inch,0.9*inch,0.9*inch,0.75*inch,0.85*inch,1.8*inch]

    hdr = Table([[
        Paragraph('Día',              ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_LEFT)),
        Paragraph('HD',               ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph('Venta Real',       ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph('Concilio',         ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph('Brecha',           ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph('Semáforo',         ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph('Hallazgo principal',ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_LEFT)),
    ]], colWidths=cw_d,
    style=TableStyle([('BACKGROUND',(0,0),(-1,-1),C_DARK),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
        ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]))

    filas = []
    for i, (r, d, lbl, nota, (rbg, rfg)) in enumerate(zip(resultados, TODOS, labels, notas_dia, sem_dia)):
        filas.append(Table([[
            Paragraph(lbl,             ParagraphStyle('r',fontName='Helvetica-Bold' if i in [0,6] else 'Helvetica',fontSize=8,textColor=C_DARK)),
            Paragraph(str(d['inventario_vendido']['hd']), ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=9,textColor=C_DARK,alignment=TA_CENTER)),
            Paragraph(f"${r['venta_real']:.2f}",  ParagraphStyle('r',fontName='Helvetica',fontSize=8,textColor=C_DARK,alignment=TA_CENTER)),
            Paragraph(f"${r['concilio']:.2f}",    ParagraphStyle('r',fontName='Helvetica',fontSize=8,textColor=C_BLUE_T,alignment=TA_CENTER)),
            Paragraph(r['brecha_str'],             ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=rfg,alignment=TA_CENTER)),
            Paragraph(r['sem_label'],              ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=rfg,alignment=TA_CENTER)),
            Paragraph(nota,                        ParagraphStyle('r',fontName='Helvetica',fontSize=7.5,textColor=C_MUTED)),
        ]], colWidths=cw_d,
        style=TableStyle([
            ('BACKGROUND',(0,0),(-1,-1), rbg),
            ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
            ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
            ('GRID',(0,0),(-1,-1),0.3,GRID),
        ])))

    total_fila = Table([[
        Paragraph('TOTAL SEMANA', ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE)),
        Paragraph(str(total_hd),  ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=9,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph(f'${total_vr:.2f}', ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph(f'${total_co:.2f}', ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=C_WHITE,alignment=TA_CENTER)),
        Paragraph(brecha_str,     ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=C_WARN,alignment=TA_CENTER)),
        Paragraph(sem_label,      ParagraphStyle('r',fontName='Helvetica-Bold',fontSize=8,textColor=C_WARN,alignment=TA_CENTER)),
        Paragraph('Sobrante acumulado → Otros ingresos no identificados', ParagraphStyle('r',fontName='Helvetica',fontSize=7.5,textColor=C_MUTED)),
    ]], colWidths=cw_d,
    style=TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),C_DARK),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('GRID',(0,0),(-1,-1),0.3,GRID),
    ]))

    story.append(KeepTogether([
        *sh('Detalle diario de la semana'),
        Spacer(1,5),
        Paragraph('Calculado por motor v5.1. Concilios y brechas verificados automáticamente.', s_note),
        Spacer(1,5),
        hdr, *filas, total_fila,
    ]))
    story.append(Spacer(1,10))

    # ── TENDENCIA DE CAJA ─────────────────────────────────────────
    caja_rows = [['Día','Vuelto inicial','Vuelto final','Variación','Observación']]
    for d, lbl in zip(TODOS, labels):
        var = d['vuelto_final'] - d['vuelto_inicial']
        caja_rows.append([lbl, f"${d['vuelto_inicial']:.2f}", f"${d['vuelto_final']:.2f}",
                          f"{var:+.2f}", d.get('obs_variacion','')])
    ct = Table(caja_rows, colWidths=[0.9*inch,0.9*inch,0.9*inch,0.75*inch,3.55*inch])
    cts = ts()
    cts.add('ALIGN',(1,0),(3,-1),'CENTER')
    for i, d in enumerate(TODOS, 1):
        var = d['vuelto_final'] - d['vuelto_inicial']
        if var >= 0:
            cts.add('BACKGROUND',(0,i),(-1,i), C_GREEN)
            cts.add('TEXTCOLOR',(3,i),(3,i), C_GREEN_T)
        else:
            cts.add('BACKGROUND',(0,i),(-1,i), C_WARN)
            cts.add('TEXTCOLOR',(3,i),(3,i), C_WARN_T)
    ct.setStyle(cts)

    story.append(KeepTogether([
        *sh('Tendencia de Caja Base'),
        Spacer(1,4),
        Paragraph('Verde = caja subió. Amarillo = caja bajó.', s_note),
        Spacer(1,5), ct, Spacer(1,4),
        Paragraph('La caja tuvo una montaña rusa durante la semana. El sábado 21 la rescató dejando $40.45.', s_note),
    ]))

    # ── ANÁLISIS DE BRECHAS ────────────────────────────────────────
    sobrantes = sum(r['brecha'] for r in resultados if r['brecha'] > 0)
    faltantes = sum(r['brecha'] for r in resultados if r['brecha'] < 0)
    dias_sob = sum(1 for r in resultados if r['brecha'] > 0)
    dias_fal = sum(1 for r in resultados if r['brecha'] < 0)

    bd = [
        ['Tipo','Días','Monto total','Impacto contable'],
        ['Sobrantes (+)', f'{dias_sob} días', f'+${sobrantes:.2f}', 'Otros ingresos no identificados'],
        ['Faltantes (−)', f'{dias_fal} días', f'-${abs(faltantes):.2f}', 'Diferencias de caja'],
        ['BRECHA NETA',   '6 días operados',  brecha_str,              f'{tipo} acumulado semanal'],
    ]
    bt = Table(bd, colWidths=[1.5*inch,1.8*inch,1.2*inch,3.5*inch])
    bts = ts(C_MID)
    bts.add('ALIGN',(2,0),(2,-1),'CENTER')
    bts.add('BACKGROUND',(0,1),(-1,1), C_GREEN)
    bts.add('TEXTCOLOR',(2,1),(2,1), C_GREEN_T)
    bts.add('BACKGROUND',(0,2),(-1,2), C_WARN)
    bts.add('TEXTCOLOR',(2,2),(2,2), C_WARN_T)
    n = len(bd)-1
    bts.add('BACKGROUND',(0,n),(-1,n), C_DARK)
    bts.add('TEXTCOLOR',(0,n),(-1,n), C_WHITE)
    bts.add('FONTNAME',(0,n),(-1,n),'Helvetica-Bold')
    bt.setStyle(bts)

    story.append(KeepTogether([
        *sh('Análisis de Brechas Semanal'),
        Spacer(1,5), bt, Spacer(1,6),
        Paragraph(f'El sobrante de {brecha_str} en una semana de ${total_vr:.2f} representa el {brecha_sem/total_vr*100:.1f}% de la venta real. Calculado con motor v5.1 — sin errores manuales.', s_note),
    ]))

    # ── HALLAZGOS SEMANALES ───────────────────────────────────────
    hd = [
        ['#','Hallazgo','Detalle','Acción'],
        ['1','Pan=Sal perfecto: Jue+Vie+Sáb21','3 días consecutivos sin discrepancia.','✅ Sin acción'],
        ['2','Ticket>Inventario: Jue y Vie','2 HD Jue, 1HD+3S Vie. Motor aplicó ajuste.','⚠️ Confirmar Vilma'],
        ['3','Caja crítica viernes ($5.30)','Accesos semanales ($40+$20) vaciaron fondo.','🔴 Revisar política gastos'],
        ['4','Motor v5.1 implementado','Cálculos automáticos — sin errores manuales.','✅ Permanente'],
        ['5','Sobrante acumulado +$22.64','1.9% de venta. Dentro de rango operativo.','🟠 Monitorear patrón'],
    ]
    ht2 = Table(hd, colWidths=[0.3*inch,2.0*inch,2.9*inch,1.8*inch])
    hts2 = ts(C_MID)
    for i,row in enumerate(hd[1:],1):
        est = str(row[3])
        if '✅' in est:   hts2.add('BACKGROUND',(0,i),(-1,i), C_GREEN)
        elif '🔴' in est: hts2.add('BACKGROUND',(0,i),(-1,i), C_RED_L)
        elif '⚠️' in est or '🟠' in est: hts2.add('BACKGROUND',(0,i),(-1,i), C_WARN)
    ht2.setStyle(hts2)

    story.append(KeepTogether([
        *sh('Hallazgos y Acciones de la Semana'),
        Spacer(1,5), ht2, Spacer(1,6),
        Paragraph('Acción prioritaria: revisar política de gastos de acceso ($40+$20 esta semana = $60) — mayor factor de caída de caja.', s_warn),
    ]))

    # ── RESUMEN VENTA OFICIAL SEMANA ──────────────────────────────
    prod_semana = {}
    orden = ['Hotdog Clásico','Hotdog Chilidog','Hotdog Chickedog','Combo Clásico',
             'Combo Especialidad','Soda individual','Lays individual','Lays (estimadas)','Alitas']
    for r in resultados:
        for row in r['vf']:
            nombre = row[0]
            u = int(row[2]); v = float(row[4].replace('$',''))
            if nombre not in prod_semana:
                prod_semana[nombre] = {'u':0,'total':0.0}
            prod_semana[nombre]['u']     += u
            prod_semana[nombre]['total'] += v
    prods_ord = sorted(prod_semana.keys(), key=lambda x: orden.index(x) if x in orden else 99)

    rs_rows = [['Producto','Unidades','Total semana']]
    tu_sem = 0; tv_sem = 0.0
    for prod in prods_ord:
        v = prod_semana[prod]
        rs_rows.append([prod, str(v['u']), f"${v['total']:.2f}"])
        tu_sem += v['u']; tv_sem += v['total']
    rs_rows.append(['TOTAL VENTA OFICIAL SEMANA', str(tu_sem), f'${tv_sem:.2f}'])

    rs_t = Table(rs_rows, colWidths=[W*0.55, W*0.20, W*0.25])
    rs_ts = TableStyle([
        ('BACKGROUND',(0,0),(-1,0),C_DARK),('TEXTCOLOR',(0,0),(-1,0),C_WHITE),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),9),
        ('FONTNAME',(0,1),(-1,-2),'Helvetica'),
        ('ROWBACKGROUNDS',(0,1),(-1,-2),[C_WHITE,C_ROW]),
        ('GRID',(0,0),(-1,-1),0.3,GRID),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),
        ('ALIGN',(1,0),(-1,-1),'CENTER'),
        ('BACKGROUND',(0,-1),(-1,-1),C_DARK),('TEXTCOLOR',(0,-1),(-1,-1),C_WHITE),
        ('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold'),('FONTSIZE',(0,-1),(-1,-1),10),
        ('TOPPADDING',(0,-1),(-1,-1),9),('BOTTOMPADDING',(0,-1),(-1,-1),9),
    ])
    rs_t.setStyle(rs_ts)

    # ── MATRIZ PRODUCTO × DÍA ─────────────────────────────────────
    mx_hdr1 = [''] + labels + ['TOTAL']
    mx_hdr2 = ['Producto'] + ['u  ·  $'] * len(labels) + ['u  ·  $']
    mx_rows = [mx_hdr1, mx_hdr2]

    for prod in prods_ord:
        row = [prod]
        for r in resultados:
            dia_u = 0; dia_v = 0.0
            for vfr in r['vf']:
                if vfr[0] == prod:
                    dia_u += int(vfr[2])
                    dia_v += float(vfr[4].replace('$',''))
            row.append(f"{dia_u}\n${dia_v:.2f}" if dia_u > 0 else '—')
        v = prod_semana[prod]
        row.append(f"{v['u']}\n${v['total']:.2f}")
        mx_rows.append(row)

    tot_u_dia = []; tot_v_dia = []
    for i,r in enumerate(resultados):
        tu = sum(int(vfr[2]) for vfr in r['vf'])
        tv = sum(float(vfr[4].replace('$','')) for vfr in r['vf'])
        tot_u_dia.append(tu); tot_v_dia.append(tv)
    tot_row = ['TOTAL']
    for u,v in zip(tot_u_dia, tot_v_dia):
        tot_row.append(f"{u}\n${v:.2f}")
    tot_row.append(f"{tu_sem}\n${tv_sem:.2f}")
    mx_rows.append(tot_row)

    prod_w2 = 1.45*inch
    day_w2  = (W - prod_w2) / (len(labels)+1)
    mx_cws  = [prod_w2] + [day_w2]*(len(labels)+1)

    mx_t = Table(mx_rows, colWidths=mx_cws)
    mx_ts = TableStyle([
        ('BACKGROUND',(0,0),(-1,0),C_DARK),('TEXTCOLOR',(0,0),(-1,0),C_WHITE),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
        ('BACKGROUND',(0,1),(-1,1),C_MID),('TEXTCOLOR',(0,1),(-1,1),C_WHITE),
        ('FONTNAME',(0,1),(-1,1),'Helvetica-Bold'),
        ('FONTSIZE',(0,0),(-1,-1),7),('FONTNAME',(0,2),(-1,-2),'Helvetica'),
        ('ROWBACKGROUNDS',(0,2),(-1,-2),[C_WHITE,C_ROW]),
        ('GRID',(0,0),(-1,-1),0.3,GRID),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
        ('ALIGN',(1,0),(-1,-1),'CENTER'),
        ('BACKGROUND',(len(labels)+1,2),(len(labels)+1,-2),C_BLUE),
        ('TEXTCOLOR',(len(labels)+1,2),(len(labels)+1,-2),C_BLUE_T),
        ('FONTNAME',(len(labels)+1,2),(len(labels)+1,-2),'Helvetica-Bold'),
        ('BACKGROUND',(0,-1),(-1,-1),C_DARK),('TEXTCOLOR',(0,-1),(-1,-1),C_WHITE),
        ('FONTNAME',(0,-1),(-1,-1),'Helvetica-Bold'),
        ('TOPPADDING',(0,-1),(-1,-1),6),('BOTTOMPADDING',(0,-1),(-1,-1),6),
    ])
    # Sábados destacados
    for i in range(2, len(mx_rows)-1):
        mx_ts.add('BACKGROUND',(1,i),(1,i),colors.HexColor('#EBF8FF'))
        mx_ts.add('BACKGROUND',(7,i),(7,i),colors.HexColor('#EBF8FF'))
    mx_t.setStyle(mx_ts)

    story.append(KeepTogether([
        *sh('Resumen de Venta Oficial — Semana Completa'),
        Spacer(1,5), rs_t,
        Spacer(1,4),
        Paragraph(f'Total semana: {tu_sem:,} productos vendidos · ${tv_sem:,.2f} venta oficial acumulada.', s_note),
        Spacer(1,10),
    ]))
    story.append(KeepTogether([
        *sh('Tendencia Diaria por Producto — Unidades y $'),
        Spacer(1,4),
        Paragraph('Unidades y $ por producto cada día. "—" = cero ventas. Sábados en azul. Total semana en azul.', s_note),
        Spacer(1,5), mx_t, Spacer(1,6),
    ]))

    # ── FOOTER ────────────────────────────────────────────────────
    story.append(Spacer(1,12))
    story.append(HRFlowable(width='100%',thickness=0.5,color=C_MUTED))
    story.append(Spacer(1,4))
    story.append(Table([[
        Paragraph('Sivar Dogs · Resumen Semanal · 15–21 Marzo 2026 · Motor v5.1', s_small),
        Paragraph('Documento confidencial · Uso interno · 21/03/2026',
            ParagraphStyle('fr',fontName='Helvetica',fontSize=8,textColor=C_MUTED,alignment=TA_RIGHT)),
    ]], colWidths=[W*0.55,W*0.45],
    style=TableStyle([('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)])))

    doc.build(story)
    print(f"✓ Resumen_Semana_SivarDogs.pdf  |  Semana ${total_vr:.2f} venta / ${total_co:.2f} concilio / {brecha_str} {sem_label}")


generar_resumen_semanal()
