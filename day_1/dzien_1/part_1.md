# Definicja i zastosowanie lakehouse

Lakehouse to platforma danych do przechowywania, zarządzania i analizowania danych strukturalnych i niestrukturalnych w jednym miejscu.
Historia Lakehouse pochodzi z potrzeby systemów bazodanowych, które opierając się na ustrukturyzowanymi danymi
przestały wsytarczać. 

Lakheouse dodaje "data governance" - w Databricks to Unity Catalog i metadane.

Cechy lakehouse:
1. Wsparcie transakcyjności (ACID)

Atomicity - (all transactions complete with success of complete failure). 
Consistency (state of the data is the same for simultaneous operations). 
Isolation (how simultaneous operations potentially confflic with one another - optimistic concurenncy control). 
Durability (commitet changes are permanent). Thanks to: write serializable isolation and optimistic concurenncy control

[ACID](https://docs.databricks.com/aws/en/lakehouse/acid#:~:text=Databricks%20uses%20Delta%20Lake%20by%20default%20for%20all,that%20all%20transactions%20either%20succeed%20or%20fail%20completely.)

2. Dane oddzielone od compute

[Databricks planes](https://docs.databricks.com/aws/en/getting-started/overview)

3. Wsparcie narzędzi BI
4. Otwarty format danych (parquet, delta)

Format Delta Lake składa się trzech części:
- _transaction_log
- pliki z danymi w formacie Parquet
- Checkpoints (co jakiś czas delta tworzy pliki binarne z _transaction_log)
 
 
https://www.datacamp.com/tutorial/delta-lake
   - Parquet to kolumnowy format plików
   - Delta Lake to framework oparty oparty o pliki parquet i log transakcyjny w formacie JSON
   - [Delta lake ] (https://www.databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf)
   - [Concurrency control](https://docs.databricks.com/aws/en/lakehouse/concurrency-control
5. Wsparcie dla różnych języków programowania (SQL, Python, Scala, R)
5. Automatyczne partycjonowanie danych (np. Liquid clustering)
5. Eliminuje proces kopiowania danych pomiędzy różnymi departamentami



# Architektura medalionu

[Architektura medalionu](https://www.databricks.com/glossary/medallion-architecture)
[Medallion architecture delta](https://delta.io/blog/delta-lake-medallion-architecture/#:~:text=Delta%20Lake%20is%20a%20great%20open%20table%20format,how%20to%20build%20a%20Medallion%20architecture%20like%20this%3A)


### Architekura lambda
[Architektura lambda](https://www.databricks.com/glossary/lambda-architecture)

### Architektura databricks
[Architektura Databricks](https://docs.databricks.com/aws/en/lakehouse-architecture/reference)


### Concurency control


### PrzykŁad KPD
S3 -> Volume -> Bronze
Dodatkowo opis standardu delta.
Utworzymy dodatkowy schemat w3, który będzie zawierał tabele w formacie delta.
