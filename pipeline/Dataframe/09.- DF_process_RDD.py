from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DateType
from pyspark.sql.functions import col, lit, when,  current_date, date_format, desc, asc, to_date, to_timestamp, count, sum


spark = SparkSession.builder.master("local").appName('DF_process_RDD').getOrCreate()


schema = StructType([StructField("id", IntegerType(), True),
                     StructField("value", StringType(), True)
                    ])


data = spark.read.csv('/home/benito.ramos/Desktop/GIT/PySpark/inputs/pokemon.csv',header=True )

rdd_data = data.rdd.filter(lambda x: int(x.is_legendary) == 1)

rdd_gen = rdd_data.map(lambda x: (x.generation, x.name))

# rdd_group = rdd_gen.groupByKey().map(lambda x: (x[0], list(x[1])))
rdd_group = rdd_gen.groupByKey().mapValues(list)


df_pokemon = rdd_group.toDF()


df_pokemon.show()

spark.stop()