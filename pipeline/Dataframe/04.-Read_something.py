from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType


# Define our Spark session
spark = SparkSession.builder.master("local") \
                    .appName('Read Something') \
                    .getOrCreate()

# Define our Dataframe structure
schema_data = StructType([
                          StructField("Character", StringType(), False),
                          StructField("Movie", IntegerType(), False)
                        ])

# Read our file (Three ways to do)
data = spark.read.csv("inputs/data_movies", inferSchema=True, header=False )

data = spark.read \
            .format("csv") \
            .options(inferSchema=True, header=False).schema(schema_data) \
            .load("inputs/data_movies")

data = spark.read \
            .format("csv") \
            .option("inferSchema", "true") \
            .option("header", "true") \
            .option("schema", schema_data) \
            .load("inputs/data_movies")


data.show()
data.printSchema()

spark.stop()
