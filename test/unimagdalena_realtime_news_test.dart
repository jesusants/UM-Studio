import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/models/noticia_model.dart';
import 'package:um_studio/data/services/unimagdalena_realtime_news_service.dart';
import 'package:um_studio/presentation/screens/desktop/widgets/desktop_news_feed.dart';
import 'package:um_studio/presentation/screens/home/tabs/resumen_tab.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  GoogleFonts.config.allowRuntimeFetching = false;

  group('NoticiaModel tests', () {
    test('JSON serialization & deserialization', () {
      final now = DateTime.now();
      final model = NoticiaModel(
        id: 'test_1',
        title: 'Nueva turbina eólica en Unimagdalena',
        summary: 'Ensayos en el campus con aerogenerador de eje vertical.',
        url: 'https://www.unimagdalena.edu.co/noticia/1',
        imageUrl: 'https://cdn.unimagdalena.edu.co/img.png',
        dateText: 'Hoy',
        category: 'FACULTAD',
        publishedAt: now,
        isNew: true,
      );

      final json = model.toJson();
      expect(json['id'], 'test_1');
      expect(json['title'], 'Nueva turbina eólica en Unimagdalena');

      final reconstructed = NoticiaModel.fromJson(json);
      expect(reconstructed.id, model.id);
      expect(reconstructed.title, model.title);
      expect(reconstructed.isNew, true);
      expect(reconstructed.isRecent, true);
    });

    test('isRecent detects recent dates', () {
      final old = NoticiaModel(
        id: 'old_1',
        title: 'Noticia del mes pasado',
        summary: '',
        url: '',
        imageUrl: '',
        dateText: '15 de Septiembre',
        publishedAt: DateTime.now().subtract(const Duration(days: 30)),
        isNew: false,
      );
      expect(old.isRecent, false);

      final fresh = old.copyWith(
        dateText: 'Hoy',
        publishedAt: DateTime.now().subtract(const Duration(hours: 3)),
      );
      expect(fresh.isRecent, true);
    });
  });

  group('Unimagdalena HTML Parser tests', () {
    test('Parses article cards with title, link, image, and summary', () {
      const htmlSnippet = '''
        <!DOCTYPE html>
        <html>
          <body>
            <div class="noticias-container">
              <article class="card">
                <img src="/images/noticias/solar.jpg" />
                <div class="card-body">
                  <h3 class="card-title">
                    <a href="/PresentacionPublicacion/DetalleNoticia/1234">Inauguración del Parque Solar Fotovoltaico</a>
                  </h3>
                  <span class="fecha">Hoy a las 10:00 AM</span>
                  <p class="card-text">La Universidad del Magdalena avanza hacia la carbono-neutralidad.</p>
                </div>
              </article>
              <div class="item-noticia">
                <a href="https://www.unimagdalena.edu.co/Noticia/5678" class="titulo">Seminario Internacional de Hidrógeno Verde</a>
                <time class="date">Ayer</time>
                <div class="resumen">Investigadores de Ingeniería Energética presentaron avances.</div>
              </div>
            </div>
          </body>
        </html>
      ''';

      final list = UnimagdalenaRealtimeNewsService.parseNoticiasHtml(htmlSnippet);
      expect(list.length, 2);

      final first = list.first;
      expect(first.title, 'Inauguración del Parque Solar Fotovoltaico');
      expect(first.url, 'https://www.unimagdalena.edu.co/PresentacionPublicacion/DetalleNoticia/1234');
      expect(first.imageUrl, 'https://www.unimagdalena.edu.co/images/noticias/solar.jpg');
      expect(first.dateText, 'Hoy a las 10:00 AM');
      expect(first.category, 'FACULTAD');

      final second = list[1];
      expect(second.title, 'Seminario Internacional de Hidrógeno Verde');
      expect(second.url, 'https://www.unimagdalena.edu.co/Noticia/5678');
      expect(second.category, 'FACULTAD');
    });

    test('Falls back gracefully to seed news when offline or empty', () async {
      SharedPreferences.setMockInitialValues({});
      final service = UnimagdalenaRealtimeNewsService.instance;
      await service.init();

      expect(service.news.isNotEmpty, true);
      expect(service.news.any((n) => n.title.contains('CENIIECT')), true);
    });
  });

  group('News Widgets Rendering tests', () {
    testWidgets('DesktopNewsFeed renders cleanly without errors', (tester) async {
      tester.view.physicalSize = const Size(1440, 900);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);

      SharedPreferences.setMockInitialValues({});

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: const Scaffold(
            body: SizedBox(
              width: 400,
              height: 800,
              child: DesktopNewsFeed(),
            ),
          ),
        ),
      );

      await tester.pumpAndSettle();

      expect(find.text('NOTICIAS & EVENTOS'), findsOneWidget);
      expect(find.text('Todas'), findsOneWidget);
      expect(find.text('Facultad'), findsOneWidget);
      expect(find.byType(DesktopNewsFeed), findsOneWidget);
    });

    testWidgets('ResumenTab renders news carousel and refresh indicator', (tester) async {
      tester.view.physicalSize = const Size(430, 932);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);

      SharedPreferences.setMockInitialValues({});

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: Scaffold(
            body: ResumenTab(
              onOpenClaseViva: (_) {},
            ),
          ),
        ),
      );

      await tester.pumpAndSettle();

      expect(find.byType(RefreshIndicator), findsOneWidget);
      expect(find.text('NOTICIAS UNIMAGDALENA'), findsOneWidget);
    });
  });
}
