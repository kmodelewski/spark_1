from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)])

data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

df = spark.createDataFrame(data, schema)
df.show()