from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType


spark = SparkSession.builder.master("local").appName('Read Something').getOrCreate()

schema_data = StructType([
                          StructField("Character", StringType, False),
                          StructField("Movie", IntegerType, False)
                        ])

data = spark.read.csv('/home/benito.ramos/Desktop/GIT/PySpark/inputs/data_movies',inferSchema=True, header=False )

data.show()

data.printSchema()

spark.stop()