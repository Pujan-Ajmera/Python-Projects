import 'package:flutter/material.dart';
import 'dart:html' as html;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  void downloadAndRunBat() {
    html.AnchorElement anchor = html.AnchorElement(href: 'assets/open_cmd.bat')
      ..setAttribute('download', 'open_cmd.bat')
      ..click();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("Download & Run .bat")),
        body: Center(
          child: ElevatedButton(
            onPressed: downloadAndRunBat,
            child: Text("Download .bat"),
          ),
        ),
      ),
    );
  }
}
