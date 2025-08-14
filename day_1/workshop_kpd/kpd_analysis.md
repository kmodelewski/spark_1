# TRAFFIC ANALYSIS KPD

## I. Ingest Data

1. Look at first file, what do you notice? 

- we need to skip three rows, third row is a header what to do with this? 
- data vs schema
- how to ingest files? Any ideas? save to volume, as external location
- change excel to csv (excel is difficult for processing)

zawsze dodawajmy zone info

```python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_now = datetime.now(ZoneInfo("UTC"))
warsaw_now = datetime.now(ZoneInfo("Europe/Warsaw"))

print(f"UTC time: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Warsaw time: {warsaw_now.strftime('%Y-%m-%d %H:%M:%S')}")
```

2. fdsf
274706 sum of rows in all files

3. Multiline z i bez (plik ListaUtrudnien_20190513_20190519.csv)

[spark_docs_csv](https://spark.apache.org/docs/latest/sql-data-sources-csv.html)

```sql
CREATE TABLE IF NOT EXISTS transportation_dept.bronze.kpd
AS
SELECT *, input_file_name() AS file, current_timestamp() AS ingest_to_bronze, _metadata
FROM read_files(
  'dbfs:/Volumes/transportation_dept/bronze/s3/kpd/csv/',
  format => 'csv',
  header => true,
  quote => '"',
  inferSchema => true,
  delimiter => ',',
  multiLine => true,
  mode => 'PERMISSIVE'
);
```

```python
df = spark.read.option("header", True)\
               .option("quote", '"')\
               .option("inferSchema", True)\
               .option("delimiter", ",")\
               .option("multiLine", True)\
               .option("mode", "PERMISSIVE")\
               .csv("dbfs:/Volumes/transportation_dept/bronze/s3/kpd/csv/")

df = df.withColumn("file", input_file_name())\
       .withColumn("ingest_to_bronze", current_timestamp())

```

plik
```text
Generalna Dyrekcja DrĂłg Krajowych i Autostrad,KrĂłtkotrwaĹ‚e roboty drogowe,Prace utrzymaniowe,2019-11-15 12:00,,2021-07-31 12:00,S6,,319.9,1.7,brak lub nieznany,tak,18.47203642134748,54.473914772749865,"Budowa drogi S6 GdaĹ„sk- SĹ‚upsk ""Trasa Kaszubska"" zad. nr. 3.
Na odcinku Budowy zwÄ™ĹĽewnie pasĂłw ruchu jezdni drogi S6 do 2,75m lewy i 3,0m prawy, ograniczenie prÄ™dkoĹ›ci do 70 km/h",,2025-08-11 23:19:34
```

4. Ręczne usniecie wierszy
```sql
DELETE FROM transportation_dept.bronze.kpd WHERE typ in ('2025-08-11 23:19:34',' zwężenie do jednego prawego pasa ruchu na docinku 120m."',
'500-148',' 43-400 Cieszyn')

DELETE FROM transportation_dept.bronze.kpd WHERE typ is null;
```

