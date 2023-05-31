# CHECK24-GenDev-Holiday-Challenge

## Mein Ansatz

### Projekt Struktur + Grundsätzliche Idee

Um die CHECK24 GenDev Holiday Challenge zu meistern, habe ich mich in diesem Projekt für das Django Framework mit einem HTML-Frontend (inklusive JavaScript und CSS) und einem python-Backend mit sqlite-Datenbank Integration entschieden.

Das Frontend ist in den Ordnern /holiday_project/templates/ und /holiday_project/assets/ gespeichert.

Für das Backend inklusive Datenbankzugriff wird hauptsächlich die Datei /holiday_project/members/views.py verwendet.

Die Grundidee zur performanten Abfrage der Daten ist die Transformation der csv-Files in einzelne Tables der Datenbank db.splite3. Diese liegen schon nach dem Preis sortiert in der Datenbank und werden dann nach gewissen Kriterien(days, countadults, etc.) gefiltert. Weitere Informationen werden dann in einem separaten Table gespeichert und mithilfe einer universellen id gemaped.

### Datenbank Struktur

Die Datenbank besteht aus den Tables hotel, first/second und den verschiedenen offerXXX(je nach Flughafen):

![Datenbank Schema](/holiday_project/assets/db_schema.png)

### Veränderung von offers.csv

Die Einträge in offers.csv wurden nicht einfach in die Datenbank 1 zu 1 übertragen, sondern folgender Maßen verändert:

- inbounddepartureairport, outboundarrivalairport wurden gelöscht, da sie immer den Wert 'PMI' haben
- mealtype, roomtype wurden zu integer-Werten gemapped, um die Größe einzelner Einträge zu verringern und somit die Abfragegeschwindigkeit zu erhöhen

Zudem wurden die Attribute startdate und days berechnet, um auch hier die Abfragepeformanz zu erhöhen.
Das beschriebene Verfahren wurde in /holiday_project/rewriteFinal.py umgesetzt.

## Anleitung zur Programmausführung

### Benötigte Installationen

Zur erfolgreichen Ausführung dieser Lösung wird Django (mind. Version 4.1.1) benötigt.
Hierfür muss zuerst Python installiert sein. Dies kann folgendermaßen überprüft werden:


Windows:

> py --version

MAC/Unix:

> Python --version


Sollte Python nicht installiert sein kann dies unter https://www.python.org/downloads/ gedownloaded werden.

Als nächstes muss überprüft werden, ob pip installiert ist. Dies kann mit folgendem Befehl herausgefunden werden:


Windows:

> py -m pip --version

MAC/Unix:

> Python -m pip --version


Sollte pip nicht installiert sein kann dies mit der Hilfe von https://pip.pypa.io/en/stable/installation/ getan werden.

Nun kann folgender Befehl ausgeführt werden, um Django zu installieren.


Windows:

> py -m pip install Django

MAC/Unix:

> Python -m pip install Django


### Starten des Programms

Ist nun alles korrekt installiert kann man per Kommandozeile ins Verzeichnis ./holiday_project/ gehen und dann folgendes Kommando ausführen:


Windows:

> py manage.py runserver

MAC/Unix:

> Python manage.py runserver


Daraufhin kann unter http://127.0.0.1:8000/ auf das laufende Programm zugreifen. 

## Videoaufzeichnung des ausgeführten Programmes

https://youtu.be/8TySInxfeQg

## Anmerkungen

### Mini-Datenbank

Die eigentliche Datenbank war leider zu groß, um sie einfach über GitHub zu pushen, daher habe ich eine kleine Test-Datenbank erstellt. Auf dieser Datenbank können folgende Abfragen ausgeführt werden:

- Flughäfen: MUC,FRA,BER + Tage: 7 + Erwachsene: 2 + Kinder: 1
- Flughafen: FRA + Tage: 10 + Erwachsene: 1 + Kinder: 0
- Flughafen: MUC + Tage: 4 + Erwachsene: 1 + Kinder: 0
- Flughafen: MUC + Tage: 14 + Erwachsene: 2 + Kinder: 0

### Weitere Optimierungen

Durch das Sortieren der Aller Einträge nach dem Preis wird indirekt auch nach der Anzahl der Personen(mehr Personen = höherer Preis) und der Tage(mehr Tage = höherer Preis) sortiert. Somit ist die Performance einer Abfrage stark davon abhängig. Bei großen Tables wie zum Beispiel offerDUS oder offerFRA wäre es also sinnvoll noch bezüglich dieser Werte aufzuspliten.
Zudem sind noch folgende weitere Suchkriterien möglich:

- Hotelsterne
- Meerblick
- Verpflegung
- Zimmer

Diese könnten bei allen offerXXX Tables hinzugefügt werden und dann beim filtern optional berücksichtigt werden.