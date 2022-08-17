from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Basics").getOrCreate()

df = spark.read.json("people.json")

print(df.show())

print(df.printSchema())

print(df.columns)

print(df.dscribe().show())

from pyspark.sql.types import (StructField, StringType, 
                                IntegerType, StructType)

data_schema= [StructField("age", IntegerType(), True),
                StructField("name", StringType(), True)]

final_struc = StructType(fields=data_schema)

df = spark.read.json

