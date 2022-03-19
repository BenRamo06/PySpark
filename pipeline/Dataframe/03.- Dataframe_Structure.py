import pyspark


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


spark = SparkSession.builder.appName('Test').getOrCreate()



# Defined a structure 
schema = StructType([StructField('id', StringType(), True),
                     StructField('num', IntegerType(), True)
                    ])


# We create a DF with a defined schema
df = spark.createDataFrame([[1,2],
                            [3,4]],schema)


df.printSchema()