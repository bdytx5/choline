import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
import 'package:firebase_database/firebase_database.dart';

Future<void> main() async {
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(CholineApp());
}

class CholineApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Choline',
      theme: ThemeData(
        primarySwatch: Colors.red,
      ),
      home: ModelListPage(),
    );
  }
}

class ModelListPage extends StatefulWidget {
  @override
  _ModelListPageState createState() => _ModelListPageState();
}

class _ModelListPageState extends State<ModelListPage> {
  final databaseReference = FirebaseDatabase.instance.reference();
  List<Model> models = [];

  @override
  void initState() {
    super.initState();
    _loadModels();
  }

  void _loadModels() {
    databaseReference.child('models').once().then((DatabaseEvent event) {
      var temp = <Model>[];
      final snapshot = event.snapshot;

      if (snapshot.exists) {
        Map<dynamic, dynamic> modelsMap =
            snapshot.value as Map<dynamic, dynamic>;
        modelsMap.forEach((key, value) {
          var model = Model.fromMap(key, value as Map<dynamic, dynamic>);
          temp.add(model);
        });
      }

      setState(() {
        models = temp;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Choline Models'),
      ),
      body: models.isEmpty
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: models.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(models[index].name),
                  subtitle: Text(models[index].hardwareRequirements),
                );
              },
            ),
    );
  }
}

class Model {
  String id;
  String name;
  String hardwareRequirements;

  Model(this.id, this.name, this.hardwareRequirements);

  factory Model.fromMap(String id, Map<dynamic, dynamic> data) {
    return Model(
      id,
      data['name'],
      data['hardwareRequirements'],
    );
  }
}
