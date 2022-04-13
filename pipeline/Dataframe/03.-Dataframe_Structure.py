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


# Define a nested structure


data = [(("James",None,"Smith"),"OH","M"),
        (("Anna","Rose",""),"NY","F"),
        (("Julia","","Williams"),"OH","F"),
        (("Maria","Anne","Jones"),"NY","M"),
        (("Jen","Mary","Brown"),"NY","M"),
        (("Mike","Mary","Williams"),"OH","M")
        ]

schema = StructType([
    StructField('name', StructType([
         StructField('firstname', StringType(), True),
         StructField('middlename', StringType(), True),
         StructField('lastname', StringType(), True)
         ])),
     StructField('state', StringType(), True),
     StructField('gender', StringType(), True)
     ])

df2 = spark.createDataFrame(data = data, schema = schema)
df2.printSchema()


spark.stop()