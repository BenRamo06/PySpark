from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType

spark = SparkSession.builder.appName('ToDataframe').getOrCreate()

rdd_data = spark.sparkContext.textFile('inputs/pokemon.csv').zipWithIndex()

rdd_filter = rdd_data.filter(lambda x: x[1] >= 1).map(lambda x: x[0].split(","))

rdd_get = rdd_filter.map(lambda x: [int(x[0]),x[1]])


schema = StructType([StructField('id', IntegerType(), True),
                     StructField('name', StringType(), True)
                    ])

# create DF with createDataFrame
df_createdf = spark.createDataFrame(data=rdd_get, schema=schema)

# create DF with toDF
df_todf = spark.createDataFrame(data=rdd_get, schema=schema)



print(df_createdf.take(3))

print(df_todf.take(3))





spark.stop()