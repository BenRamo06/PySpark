import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName('Tets').getOrCreate()


# Defined schema
schema = StructType([StructField('id', StringType(), True),  # name col, data type, is nullable?
                     StructField('num', IntegerType(), True)
                    ])


# Create DF with defined schema
df = spark.createDataFrame([[1,2],
                            [3,4]], schema)


df.printSchema()