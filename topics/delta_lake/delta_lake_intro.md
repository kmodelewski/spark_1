# Wprowadzenie

Delta Lake to framework open source, który umożliwia osiągnięcia ACID (m.in. transakcyjności danych) na
na chmurowych platformach danych (ADSL2 dla Azure, S3 dla AWS, GCS dla Google Cloud).
Rozproszone systemy plików potrzebują dodatkowej warstwy w przypadku np. błędów zapisu danych.
Gdy część danych się zapisze, a część nie. 

W Delta Lake tabele nazywane są tabelami Delta i zawierają "write-ahead log". Obiekty tabel
przechowywane są w plikach Parquet. Log ten zawiera min/max dla każdego pliku, co pozwala
na szybkość odczytu danych. Takie podejście zapewniło dodatkowe funkcjonalności, m.in.:
 - Time travel
 - Operacje typu Insert, Update, Delete
 - Strumieniowe przetwarzanie danych poprzez szybkie dopisanie danych do tabeli, a później 
   połączenie ich z danymi już istniejącymi
 - Cache - dane są niezmienialne w sensie transakcji, więc można ja przechowywać w pamięci
 - Schema evolution - możliwość czytania "starych" plików parquet bez konieczności ich przetworzenia.
 - Optymalizacja wielkości plików
 - Logowanie wszystkich zmian na tabeli - co zapewnia log transakcyjny.

Hive metastore - zmiany do plików trzymane są w realacyjnej bazie danych np. MySQL
co powoduje problemy wydajnościowe dla dużej skali danych.