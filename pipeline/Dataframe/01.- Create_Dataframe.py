import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


# We create (builder) a Spark Session where:
    # Spark is a distribuided processing in the master local
    # Our process (appName) will be called Test
spark = SparkSession.builder.master("local").appName('Test').getOrCreate()


# Defined schema
schema = StructType([StructField('id', StringType(), True),  # name col, data type, is nullable?
                     StructField('num', IntegerType(), True)
                    ])


# Create DF with defined schema
df = spark.createDataFrame([[1,2],
                            [3,4]], schema)


df.printSchema()


# We always need to close session spark

spark.close()