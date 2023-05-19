# Benutzerdokumentation - XLS-Konverter

Der XLS-Konverter ist ein Python-Skript, das entwickelt wurde, um XLS-Dateien in das XLSX-Format zu konvertieren. Es verwendet die `pandas`-Bibliothek, um die Konvertierung durchzuführen.

## Systemanforderungen

- Python (Version 3.6 oder höher) muss auf Ihrem System installiert sein.
- Die erforderlichen Bibliotheken (pandas, xlrd) müssen installiert sein. Sie können diese Bibliotheken mit dem Befehl `pip install pandas xlrd` installieren.

## Verwendung

1. Öffnen Sie die Befehlszeile oder das Terminal auf Ihrem System.

2. Navigieren Sie zum Verzeichnis, in dem sich das XLS-Konverter-Skript befindet.

3. Geben Sie den folgenden Befehl ein, um das Skript auszuführen:

python xls_converter.py -i <inputfile> -o <outputfile>

Ersetzen Sie `<inputfile>` durch den Pfad zur XLS-Datei, die Sie konvertieren möchten, und `<outputfile>` durch den Pfad, unter dem die konvertierte XLSX-Datei gespeichert werden soll.

4. Drücken Sie die Eingabetaste, um den Befehl auszuführen. Das Skript führt die Konvertierung durch und zeigt den Fortschritt an.

5. Sobald die Konvertierung abgeschlossen ist, finden Sie die konvertierte XLSX-Datei am angegebenen Ausgabepfad.

## Beispiel

Angenommen, Sie möchten die Datei `input.xls` in das XLSX-Format konvertieren und die konvertierte Datei als `output.xlsx` speichern. Navigieren Sie im Befehlszeilenfenster zum Verzeichnis, in dem sich das Skript befindet, und geben Sie den folgenden Befehl ein:


Das Skript führt die Konvertierung durch, und Sie können den Fortschritt in der Befehlszeile verfolgen. Sobald die Konvertierung abgeschlossen ist, finden Sie die Datei `output.xlsx` im angegebenen Ausgabepfad.

## Fehlerbehandlung

- Wenn während der Konvertierung ein Fehler auftritt, wird eine entsprechende Fehlermeldung angezeigt. Überprüfen Sie die Meldung, um das Problem zu identifizieren und entsprechend zu handeln.
- Stellen Sie sicher, dass die angegebenen Dateipfade gültig sind und dass Sie die erforderlichen Schreibberechtigungen für den Ausgabepfad haben.
