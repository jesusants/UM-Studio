import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:um_studio/presentation/widgets/mouse_scrollable_horizontal_bar.dart';

void main() {
  testWidgets('MouseScrollableHorizontalBar converts vertical mouse wheel into horizontal scroll',
      (WidgetTester tester) async {
    final controller = ScrollController();

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: Center(
            child: SizedBox(
              width: 200,
              height: 40,
              child: MouseScrollableHorizontalBar(
                controller: controller,
                height: 40,
                child: ListView.builder(
                  controller: controller,
                  scrollDirection: Axis.horizontal,
                  itemCount: 20,
                  itemBuilder: (_, index) => Container(
                    width: 80,
                    height: 40,
                    alignment: Alignment.center,
                    child: Text('Item $index'),
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );

    await tester.pumpAndSettle();

    expect(controller.offset, 0.0);

    // PointerScrollEvent with vertical delta (simulating mouse wheel rotation)
    final pointerEvent = PointerScrollEvent(
      position: tester.getCenter(find.byType(MouseScrollableHorizontalBar)),
      scrollDelta: const Offset(0, 80),
    );
    tester.binding.handlePointerEvent(pointerEvent);
    await tester.pumpAndSettle();

    expect(controller.offset, greaterThan(0.0));
  });

  testWidgets('MouseScrollableHorizontalBar works seamlessly with builder pattern',
      (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: Center(
            child: SizedBox(
              width: 200,
              height: 40,
              child: MouseScrollableHorizontalBar(
                height: 40,
                builder: (context, controller) => ListView.builder(
                  controller: controller,
                  scrollDirection: Axis.horizontal,
                  itemCount: 15,
                  itemBuilder: (_, index) => Container(
                    width: 70,
                    height: 40,
                    alignment: Alignment.center,
                    child: Text('Chip $index'),
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );

    await tester.pumpAndSettle();

    // Verify right arrow exists because content overflows
    expect(find.byIcon(Icons.chevron_right_rounded), findsOneWidget);

    // Tap right arrow
    await tester.tap(find.byIcon(Icons.chevron_right_rounded));
    await tester.pumpAndSettle();

    // Verify left arrow is now enabled
    expect(find.byIcon(Icons.chevron_left_rounded), findsOneWidget);
  });
}
