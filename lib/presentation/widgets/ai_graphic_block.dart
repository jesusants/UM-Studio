import 'dart:convert';
import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../core/theme/app_theme.dart';
import 'interactive_engineering_chart.dart';
import 'ios_primitives.dart';

class AiGraphicSeries {
  const AiGraphicSeries({
    required this.name,
    required this.colorKey,
    required this.points,
  });

  final String name;
  final String colorKey;
  final List<Offset> points;
}

class AiGraphicVector {
  const AiGraphicVector({
    required this.name,
    required this.angleDeg,
    required this.magnitude,
    required this.colorKey,
  });

  final String name;
  final double angleDeg;
  final double magnitude;
  final String colorKey;
}

class AiGraphicBar {
  const AiGraphicBar({
    required this.label,
    required this.value,
    required this.colorKey,
  });

  final String label;
  final double value;
  final String colorKey;
}

/// Especificación estructurada de un elemento gráfico generado por la IA o por el usuario.
class AiGraphicSpec {
  const AiGraphicSpec({
    required this.tipo,
    required this.titulo,
    this.ejeX = 'x',
    this.ejeY = 'y',
    this.series = const [],
    this.vectores = const [],
    this.barras = const [],
    this.modoLab = '',
  });

  final String tipo; // funcion | vectores | barras | lab
  final String titulo;
  final String ejeX;
  final String ejeY;
  final List<AiGraphicSeries> series;
  final List<AiGraphicVector> vectores;
  final List<AiGraphicBar> barras;
  final String modoLab;

  static double? _toDouble(dynamic v) {
    if (v is num) return v.isFinite ? v.toDouble() : null;
    if (v is String) {
      final parsed = double.tryParse(v.trim());
      return (parsed != null && parsed.isFinite) ? parsed : null;
    }
    return null;
  }

  static AiGraphicSpec? tryParse(String rawBlock) {
    var cleaned = rawBlock.trim();
    if (cleaned.isEmpty) return null;
    if (cleaned.startsWith('```')) {
      cleaned = cleaned
          .replaceFirst(RegExp(r'^```[a-zA-Z0-9_-]*\s*'), '')
          .replaceFirst(RegExp(r'```\s*$'), '')
          .trim();
    }
    // Eliminar comas colgantes antes de `]` o `}` para tolerar JSON imperfecto
    cleaned = cleaned.replaceAllMapped(
      RegExp(r',\s*([\]}])'),
      (m) => m.group(1)!,
    );

    dynamic decoded;
    try {
      decoded = jsonDecode(cleaned);
    } catch (_) {
      return null;
    }
    if (decoded is! Map) return null;
    final map = decoded.map((k, v) => MapEntry(k.toString(), v));

    final rawTipo = (map['tipo'] ?? map['type'] ?? 'funcion')
        .toString()
        .toLowerCase()
        .trim();
    final titulo =
        (map['titulo'] ?? map['title'] ?? 'Elemento Gráfico').toString().trim();
    final ejeX = (map['ejex'] ?? map['eje_x'] ?? 'x').toString().trim();
    final ejeY = (map['ejey'] ?? map['eje_y'] ?? 'y').toString().trim();
    final modoLab =
        (map['modo_lab'] ?? map['mode'] ?? '').toString().trim();

    final series = <AiGraphicSeries>[];
    final rawSeries = map['series'];
    if (rawSeries is Iterable) {
      for (final item in rawSeries) {
        if (item is! Map) continue;
        final pts = <Offset>[];
        final rawPts = item['puntos'] ?? item['points'];
        if (rawPts is Iterable) {
          for (final pt in rawPts) {
            if (pt is List && pt.length >= 2) {
              final x = _toDouble(pt[0]);
              final y = _toDouble(pt[1]);
              if (x != null && y != null) pts.add(Offset(x, y));
            } else if (pt is Map) {
              final x = _toDouble(pt['x']);
              final y = _toDouble(pt['y']);
              if (x != null && y != null) pts.add(Offset(x, y));
            }
          }
        }
        if (pts.isNotEmpty) {
          series.add(
            AiGraphicSeries(
              name: (item['nombre'] ?? item['name'] ?? 'Curva').toString(),
              colorKey: (item['color'] ?? 'green').toString(),
              points: pts,
            ),
          );
        }
      }
    }

    final vectores = <AiGraphicVector>[];
    final rawVectores = map['vectores'] ?? map['vectors'] ?? map['fasores'];
    if (rawVectores is Iterable) {
      for (final item in rawVectores) {
        if (item is! Map) continue;
        final mag = _toDouble(item['magnitud'] ?? item['magnitude'] ?? 1.0) ?? 1.0;
        final ang = _toDouble(item['angulo_deg'] ?? item['angulo'] ?? item['angle'] ?? 0.0) ?? 0.0;
        vectores.add(
          AiGraphicVector(
            name: (item['nombre'] ?? item['name'] ?? 'V').toString(),
            angleDeg: ang,
            magnitude: mag.abs().clamp(0.05, 1000.0),
            colorKey: (item['color'] ?? 'green').toString(),
          ),
        );
      }
    }

    final barras = <AiGraphicBar>[];
    final rawBarras = map['barras'] ?? map['bars'] ?? map['datos'];
    if (rawBarras is Iterable) {
      for (final item in rawBarras) {
        if (item is! Map) continue;
        final val = _toDouble(item['valor'] ?? item['value']);
        if (val == null) continue;
        barras.add(
          AiGraphicBar(
            label: (item['label'] ?? item['nombre'] ?? '').toString(),
            value: val,
            colorKey: (item['color'] ?? 'indigo').toString(),
          ),
        );
      }
    }

    final resolvedTipo = rawTipo.contains('vec') ||
            rawTipo.contains('dcl') ||
            rawTipo.contains('fasor')
        ? (vectores.isNotEmpty ? 'vectores' : 'funcion')
        : rawTipo.contains('bar') || rawTipo.contains('comp')
            ? (barras.isNotEmpty ? 'barras' : 'funcion')
            : rawTipo.contains('lab') || modoLab.isNotEmpty
                ? 'lab'
                : (series.isNotEmpty
                    ? 'funcion'
                    : (vectores.isNotEmpty
                        ? 'vectores'
                        : (barras.isNotEmpty ? 'barras' : 'lab')));

    return AiGraphicSpec(
      tipo: resolvedTipo,
      titulo: titulo.isEmpty ? 'Visualización de Ingeniería' : titulo,
      ejeX: ejeX,
      ejeY: ejeY,
      series: series,
      vectores: vectores,
      barras: barras,
      modoLab: modoLab,
    );
  }
}

Color resolveGraphicAccentColor(String key, AppPalette p) {
  final lower = key.toLowerCase().trim();
  if (lower.contains('indigo') || lower.contains('purple') || lower.contains('blue')) {
    return p.indigo;
  }
  if (lower.contains('orange') || lower.contains('amber') || lower.contains('red')) {
    return p.orange;
  }
  if (lower.contains('cyan') || lower.contains('teal')) {
    return const Color(0xFF64D2FF);
  }
  return p.green;
}

/// Renderizador nativo e interactivo de elementos gráficos dentro de mensajes IA y usuario.
class AiGraphicBlockWidget extends StatefulWidget {
  const AiGraphicBlockWidget({
    super.key,
    required this.spec,
    this.asignaturaNombre = 'Ingeniería',
    this.temaTitulo = 'Análisis Gráfico',
  });

  final AiGraphicSpec spec;
  final String asignaturaNombre;
  final String temaTitulo;

  @override
  State<AiGraphicBlockWidget> createState() => _AiGraphicBlockWidgetState();
}

class _AiGraphicBlockWidgetState extends State<AiGraphicBlockWidget> {
  double? _hoverNormalizedX;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final spec = widget.spec;

    if (spec.tipo == 'lab') {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 6),
        child: InteractiveEngineeringChart(
          asignaturaNombre: widget.asignaturaNombre,
          temaTitulo: spec.titulo.isNotEmpty ? spec.titulo : widget.temaTitulo,
          explicitHint: spec.modoLab,
          compact: true,
        ),
      );
    }

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 6),
      padding: const EdgeInsets.all(11),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF0A0C12) : const Color(0xFFF6F8FB),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(
          color: isDark ? const Color(0xFF1F2430) : const Color(0xFFDCDFE6),
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(
            children: [
              Icon(
                spec.tipo == 'vectores'
                    ? Icons.north_east_rounded
                    : (spec.tipo == 'barras'
                        ? Icons.bar_chart_rounded
                        : Icons.show_chart_rounded),
                size: 14,
                color: p.indigo,
              ),
              const SizedBox(width: 6),
              Expanded(
                child: Text(
                  spec.titulo,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 11.5,
                    fontWeight: FontWeight.w700,
                    color: p.textPrimary,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          if (spec.tipo == 'funcion' && spec.series.isNotEmpty)
            _buildFunctionChart(p, isDark, spec)
          else if (spec.tipo == 'vectores' && spec.vectores.isNotEmpty)
            _buildVectorDiagram(p, isDark, spec)
          else if (spec.tipo == 'barras' && spec.barras.isNotEmpty)
            _buildBarChart(p, isDark, spec),
        ],
      ),
    );
  }

  Widget _buildFunctionChart(
    AppPalette p,
    bool isDark,
    AiGraphicSpec spec,
  ) {
    var minX = double.infinity;
    var maxX = double.negativeInfinity;
    var minY = double.infinity;
    var maxY = double.negativeInfinity;

    for (final s in spec.series) {
      for (final pt in s.points) {
        if (pt.dx < minX) minX = pt.dx;
        if (pt.dx > maxX) maxX = pt.dx;
        if (pt.dy < minY) minY = pt.dy;
        if (pt.dy > maxY) maxY = pt.dy;
      }
    }

    if ((maxX - minX).abs() < 1e-6) {
      minX -= 1;
      maxX += 1;
    }
    if ((maxY - minY).abs() < 1e-6) {
      minY -= 1;
      maxY += 1;
    } else {
      final pad = (maxY - minY) * 0.12;
      minY -= pad;
      maxY += pad;
    }

    String? hoverText;
    if (_hoverNormalizedX != null) {
      final targetX = minX + _hoverNormalizedX! * (maxX - minX);
      final firstPts = spec.series.first.points;
      Offset nearest = firstPts.first;
      var bestDist = (nearest.dx - targetX).abs();
      for (final pt in firstPts) {
        final d = (pt.dx - targetX).abs();
        if (d < bestDist) {
          bestDist = d;
          nearest = pt;
        }
      }
      hoverText =
          '(${nearest.dx.toStringAsFixed(2)}, ${nearest.dy.toStringAsFixed(2)})';
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(
          height: 155,
          width: double.infinity,
          child: LayoutBuilder(
            builder: (context, constraints) {
              return MouseRegion(
                onHover: (e) => setState(() {
                  _hoverNormalizedX =
                      (e.localPosition.dx / constraints.maxWidth).clamp(0.0, 1.0);
                }),
                onExit: (_) => setState(() => _hoverNormalizedX = null),
                child: GestureDetector(
                  onHorizontalDragUpdate: (d) => setState(() {
                    _hoverNormalizedX =
                        (d.localPosition.dx / constraints.maxWidth).clamp(0.0, 1.0);
                  }),
                  onTapDown: (d) => setState(() {
                    _hoverNormalizedX =
                        (d.localPosition.dx / constraints.maxWidth).clamp(0.0, 1.0);
                  }),
                  child: RepaintBoundary(
                    child: CustomPaint(
                      painter: _FunctionGraphPainter(
                        spec: spec,
                        minX: minX,
                        maxX: maxX,
                        minY: minY,
                        maxY: maxY,
                        hoverNormX: _hoverNormalizedX,
                        palette: p,
                        isDark: isDark,
                      ),
                    ),
                  ),
                ),
              );
            },
          ),
        ),
        const SizedBox(height: 6),
        Wrap(
          spacing: 8,
          runSpacing: 4,
          crossAxisAlignment: WrapCrossAlignment.center,
          children: [
            for (final s in spec.series)
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Container(
                    width: 8,
                    height: 8,
                    decoration: BoxDecoration(
                      color: resolveGraphicAccentColor(s.colorKey, p),
                      shape: BoxShape.circle,
                    ),
                  ),
                  const SizedBox(width: 4),
                  Text(
                    s.name,
                    style: mono(fontSize: 9.5, color: p.textSecondary),
                  ),
                ],
              ),
            Text(
              'Ejes: ${spec.ejeX} vs ${spec.ejeY}',
              style: mono(fontSize: 9, color: p.textTertiary),
            ),
            if (hoverText != null)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 1.5),
                decoration: BoxDecoration(
                  color: p.indigo.o(0.16),
                  borderRadius: BorderRadius.circular(5),
                ),
                child: Text(
                  hoverText,
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    color: p.indigo,
                  ),
                ),
              ),
          ],
        ),
      ],
    );
  }

  Widget _buildVectorDiagram(
    AppPalette p,
    bool isDark,
    AiGraphicSpec spec,
  ) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(
          height: 170,
          width: double.infinity,
          child: RepaintBoundary(
            child: CustomPaint(
              painter: _VectorDiagramPainter(
                vectores: spec.vectores,
                palette: p,
                isDark: isDark,
              ),
            ),
          ),
        ),
        const SizedBox(height: 6),
        Wrap(
          spacing: 8,
          runSpacing: 4,
          children: [
            for (final v in spec.vectores)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                decoration: BoxDecoration(
                  color: resolveGraphicAccentColor(v.colorKey, p).o(0.14),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  '${v.name} (${v.angleDeg.toStringAsFixed(0)}° • ${v.magnitude.toStringAsFixed(1)}u)',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w600,
                    color: resolveGraphicAccentColor(v.colorKey, p),
                  ),
                ),
              ),
          ],
        ),
      ],
    );
  }

  Widget _buildBarChart(
    AppPalette p,
    bool isDark,
    AiGraphicSpec spec,
  ) {
    final maxVal = spec.barras
        .map((b) => b.value.abs())
        .fold<double>(1.0, (a, b) => a > b ? a : b);

    return Column(
      children: [
        for (final bar in spec.barras) ...[
          Padding(
            padding: const EdgeInsets.only(bottom: 6),
            child: Row(
              children: [
                SizedBox(
                  width: 78,
                  child: Text(
                    bar.label,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: mono(fontSize: 10, color: p.textSecondary),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: LayoutBuilder(
                    builder: (context, constraints) {
                      final ratio = (bar.value.abs() / maxVal).clamp(0.06, 1.0);
                      final color = resolveGraphicAccentColor(bar.colorKey, p);
                      return Container(
                        height: 14,
                        alignment: Alignment.centerLeft,
                        decoration: BoxDecoration(
                          color: isDark
                              ? const Color(0xFF141822)
                              : const Color(0xFFE9ECF2),
                          borderRadius: BorderRadius.circular(7),
                        ),
                        child: Container(
                          width: constraints.maxWidth * ratio,
                          height: 14,
                          decoration: BoxDecoration(
                            color: color,
                            borderRadius: BorderRadius.circular(7),
                          ),
                        ),
                      );
                    },
                  ),
                ),
                const SizedBox(width: 8),
                Text(
                  bar.value.toStringAsFixed(
                    bar.value == bar.value.roundToDouble() ? 0 : 1,
                  ),
                  style: mono(
                    fontSize: 10.5,
                    fontWeight: FontWeight.w700,
                    color: p.textPrimary,
                  ),
                ),
              ],
            ),
          ),
        ],
      ],
    );
  }
}

class _FunctionGraphPainter extends CustomPainter {
  const _FunctionGraphPainter({
    required this.spec,
    required this.minX,
    required this.maxX,
    required this.minY,
    required this.maxY,
    required this.hoverNormX,
    required this.palette,
    required this.isDark,
  });

  final AiGraphicSpec spec;
  final double minX;
  final double maxX;
  final double minY;
  final double maxY;
  final double? hoverNormX;
  final AppPalette palette;
  final bool isDark;

  @override
  void paint(Canvas canvas, Size size) {
    final rect = Offset.zero & size;
    final gridPaint = Paint()
      ..color = (isDark ? Colors.white : Colors.black).withAlpha(18)
      ..strokeWidth = 0.8;

    for (var i = 1; i < 5; i++) {
      final gx = size.width * (i / 5);
      final gy = size.height * (i / 5);
      canvas.drawLine(Offset(gx, 0), Offset(gx, size.height), gridPaint);
      canvas.drawLine(Offset(0, gy), Offset(size.width, gy), gridPaint);
    }

    double mapX(double x) =>
        ((x - minX) / (maxX - minX)).clamp(0.0, 1.0) * size.width;
    double mapY(double y) =>
        size.height - ((y - minY) / (maxY - minY)).clamp(0.0, 1.0) * size.height;

    final axisPaint = Paint()
      ..color = (isDark ? Colors.white : Colors.black).withAlpha(55)
      ..strokeWidth = 1.1;

    if (minY <= 0 && maxY >= 0) {
      final y0 = mapY(0);
      canvas.drawLine(Offset(0, y0), Offset(size.width, y0), axisPaint);
    }
    if (minX <= 0 && maxX >= 0) {
      final x0 = mapX(0);
      canvas.drawLine(Offset(x0, 0), Offset(x0, size.height), axisPaint);
    }

    for (final s in spec.series) {
      if (s.points.isEmpty) continue;
      final color = resolveGraphicAccentColor(s.colorKey, palette);
      final stroke = Paint()
        ..color = color
        ..strokeWidth = 2.2
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round;

      final path = Path();
      final p0 = Offset(mapX(s.points.first.dx), mapY(s.points.first.dy));
      path.moveTo(p0.dx, p0.dy);
      for (var i = 1; i < s.points.length; i++) {
        final prev = Offset(mapX(s.points[i - 1].dx), mapY(s.points[i - 1].dy));
        final curr = Offset(mapX(s.points[i].dx), mapY(s.points[i].dy));
        final mid = Offset((prev.dx + curr.dx) / 2, (prev.dy + curr.dy) / 2);
        path.quadraticBezierTo(prev.dx, prev.dy, mid.dx, mid.dy);
        if (i == s.points.length - 1) {
          path.lineTo(curr.dx, curr.dy);
        }
      }
      canvas.drawPath(path, stroke);
    }

    if (hoverNormX != null) {
      final hx = hoverNormX! * size.width;
      final cursorPaint = Paint()
        ..color = palette.indigo.withAlpha(140)
        ..strokeWidth = 1.0;
      canvas.drawLine(Offset(hx, 0), Offset(hx, size.height), cursorPaint);
    }

    canvas.drawRRect(
      RRect.fromRectAndRadius(rect, const Radius.circular(8)),
      Paint()
        ..color = (isDark ? Colors.white : Colors.black).withAlpha(24)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1,
    );
  }

  @override
  bool shouldRepaint(covariant _FunctionGraphPainter oldDelegate) {
    return oldDelegate.spec != spec ||
        oldDelegate.hoverNormX != hoverNormX ||
        oldDelegate.isDark != isDark;
  }
}

class _VectorDiagramPainter extends CustomPainter {
  const _VectorDiagramPainter({
    required this.vectores,
    required this.palette,
    required this.isDark,
  });

  final List<AiGraphicVector> vectores;
  final AppPalette palette;
  final bool isDark;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final maxR = math.min(size.width, size.height) * 0.40;

    final axisPaint = Paint()
      ..color = (isDark ? Colors.white : Colors.black).withAlpha(42)
      ..strokeWidth = 1.0;

    canvas.drawCircle(
      center,
      maxR * 0.85,
      Paint()
        ..color = (isDark ? Colors.white : Colors.black).withAlpha(18)
        ..style = PaintingStyle.stroke,
    );
    canvas.drawLine(
      Offset(center.dx - maxR * 1.15, center.dy),
      Offset(center.dx + maxR * 1.15, center.dy),
      axisPaint,
    );
    canvas.drawLine(
      Offset(center.dx, center.dy - maxR * 1.1),
      Offset(center.dx, center.dy + maxR * 1.1),
      axisPaint,
    );

    final maxMag = vectores
        .map((v) => v.magnitude)
        .fold<double>(0.001, (a, b) => a > b ? a : b);

    for (final v in vectores) {
      final rad = v.angleDeg * math.pi / 180.0;
      final len = (v.magnitude / maxMag).clamp(0.25, 1.0) * maxR;
      final end = Offset(
        center.dx + math.cos(rad) * len,
        center.dy - math.sin(rad) * len,
      );
      final color = resolveGraphicAccentColor(v.colorKey, palette);
      final paint = Paint()
        ..color = color
        ..strokeWidth = 2.6
        ..strokeCap = StrokeCap.round;

      canvas.drawLine(center, end, paint);

      // Punta de flecha
      const headLen = 9.0;
      final tipAngle = math.atan2(end.dy - center.dy, end.dx - center.dx);
      final p1 = Offset(
        end.dx - headLen * math.cos(tipAngle - 0.42),
        end.dy - headLen * math.sin(tipAngle - 0.42),
      );
      final p2 = Offset(
        end.dx - headLen * math.cos(tipAngle + 0.42),
        end.dy - headLen * math.sin(tipAngle + 0.42),
      );
      canvas.drawLine(end, p1, paint);
      canvas.drawLine(end, p2, paint);

      // Etiqueta
      final labelOffset = Offset(
        end.dx + math.cos(rad) * 12,
        end.dy - math.sin(rad) * 12,
      );
      final tp = TextPainter(
        text: TextSpan(
          text: v.name,
          style: TextStyle(
            fontSize: 10.5,
            fontWeight: FontWeight.w700,
            color: color,
          ),
        ),
        textDirection: TextDirection.ltr,
      )..layout();
      tp.paint(
        canvas,
        Offset(
          (labelOffset.dx - tp.width / 2).clamp(2.0, size.width - tp.width - 2),
          (labelOffset.dy - tp.height / 2)
              .clamp(2.0, size.height - tp.height - 2),
        ),
      );
    }

    // Nodo de masa/origen
    canvas.drawCircle(
      center,
      5,
      Paint()..color = isDark ? Colors.white : Colors.black,
    );
  }

  @override
  bool shouldRepaint(covariant _VectorDiagramPainter oldDelegate) {
    return oldDelegate.vectores != vectores || oldDelegate.isDark != isDark;
  }
}

/// Plantillas listas para que el usuario o estudiante inserte elementos gráficos en el chat IA.
Future<String?> showAiGraphicComposerDialog(
  BuildContext context, {
  required String temaTitulo,
}) async {
  final p = context.palette;
  final titleCtrl = TextEditingController(text: 'Gráfica sobre $temaTitulo');
  String selectedPreset = 'funcion';

  final result = await showDialog<String>(
    context: context,
    builder: (ctx) => StatefulBuilder(
      builder: (ctx, setDlgState) {
        final presets = <({String id, String label, String desc, IconData icon})>[
          (
            id: 'funcion',
            label: 'Curva / Función Matemática',
            desc: 'Pide a la IA una gráfica cartesiana x-y con ejes y puntos del tema.',
            icon: Icons.show_chart_rounded,
          ),
          (
            id: 'vectores',
            label: 'Diagrama de Vectores / Fuerzas / Fasores',
            desc: 'Genera un diagrama vectorial o DCL con ángulos y magnitudes.',
            icon: Icons.north_east_rounded,
          ),
          (
            id: 'barras',
            label: 'Comparación Energética / Barras',
            desc: 'Compara magnitudes, pérdidas o eficiencias paso a paso.',
            icon: Icons.bar_chart_rounded,
          ),
          (
            id: 'lab',
            label: 'Insertar Simulador Interactivo Aquí',
            desc: 'Incrusta directamente el laboratorio interactivo en el chat.',
            icon: Icons.insights_rounded,
          ),
        ];

        return AlertDialog(
          backgroundColor: p.card,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
            side: BorderSide(color: p.cardBorder),
          ),
          title: Row(
            children: [
              Icon(Icons.auto_graph_rounded, color: p.indigo, size: 20),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  'Añadir Elemento Gráfico',
                  style: TextStyle(
                    fontSize: 15.5,
                    fontWeight: FontWeight.w700,
                    color: p.textPrimary,
                  ),
                ),
              ),
            ],
          ),
          content: SizedBox(
            width: 360,
            child: SingleChildScrollView(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                TextField(
                  controller: titleCtrl,
                  style: TextStyle(fontSize: 13, color: p.textPrimary),
                  decoration: InputDecoration(
                    labelText: 'Título o enfoque del gráfico',
                    labelStyle: TextStyle(fontSize: 12, color: p.textSecondary),
                    isDense: true,
                    filled: true,
                    fillColor: p.elevated,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                      borderSide: BorderSide(color: p.cardBorder),
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                for (final item in presets) ...[
                  TapScale(
                    onTap: () => setDlgState(() => selectedPreset = item.id),
                    child: Container(
                      margin: const EdgeInsets.only(bottom: 7),
                      padding: const EdgeInsets.symmetric(
                        horizontal: 11,
                        vertical: 9,
                      ),
                      decoration: BoxDecoration(
                        color: selectedPreset == item.id
                            ? p.indigo.o(0.14)
                            : p.elevated,
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(
                          color: selectedPreset == item.id
                              ? p.indigo
                              : p.cardBorder,
                        ),
                      ),
                      child: Row(
                        children: [
                          Icon(
                            item.icon,
                            size: 16,
                            color: selectedPreset == item.id
                                ? p.indigo
                                : p.textSecondary,
                          ),
                          const SizedBox(width: 9),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  item.label,
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w700,
                                    color: p.textPrimary,
                                  ),
                                ),
                                Text(
                                  item.desc,
                                  style: TextStyle(
                                    fontSize: 10.5,
                                    color: p.textSecondary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ),
        actions: [
            TextButton(
              onPressed: () => Navigator.of(ctx).pop(),
              child: Text(
                'Cancelar',
                style: TextStyle(color: p.textSecondary),
              ),
            ),
            FilledButton(
              style: FilledButton.styleFrom(backgroundColor: p.indigo),
              onPressed: () {
                final title = titleCtrl.text.trim().isNotEmpty
                    ? titleCtrl.text.trim()
                    : temaTitulo;
                if (selectedPreset == 'lab') {
                  final safeTitle = jsonEncode(title);
                  Navigator.of(ctx).pop(
                    'Explícame y muestra el laboratorio interactivo:\n```um-grafica\n{"tipo":"lab","titulo":$safeTitle,"modo_lab":""}\n```',
                  );
                } else {
                  Navigator.of(ctx).pop(
                    'Genera un elemento gráfico tipo "$selectedPreset" (bloque ```um-grafica) titulado "$title" aplicado al tema "$temaTitulo" y explícalo paso a paso.',
                  );
                }
              },
              child: const Text('Insertar en chat'),
            ),
          ],
        );
      },
    ),
  );
  titleCtrl.dispose();
  return result;
}
