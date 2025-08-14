(spark.read
  .format("csv")
  .option("mode", "PERMISSIVE")
  .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
)

SELECT * FROM read_files(
  's3://<bucket>/<path>/<file>.csv',
  format => 'csv',
  header => false,
  schema => 'id string, date date, event_time timestamp')

https://docs.databricks.com/aws/en/ingestion/file-metadata-column


```sql
| CREATE TABLE transportation_dept.bronze.kpd
AS
SELECT *, input_file_name() AS file, current_timestamp() AS ingest_to_bronze, _metadata
FROM read_files(
  'dbfs:/Volumes/transportation_dept/bronze/s3/kpd/csv/',
  format => 'csv',
  header => true,
  quote => '"',
  inferSchema => true,
  delimiter => ',',
  mode => 'PERMISSIVE'
);
```


```python

df = spark.read \
  .format("csv") \
  .schema(schema) \
  .load("dbfs:/tmp/*") \
  .select("*", "_metadata")
```
https://www.youtube.com/watch?v=k2AVOmUS7i0&t

display(df)