from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType

spark = SparkSession.builder.appName('ToDataframe').getOrCreate()


# We read a file with minPartitions equal 3

rdd_data = spark.sparkContext.textFile('inputs/pokemon.csv',minPartitions=5).zipWithIndex()

rdd_filter = rdd_data.filter(lambda x: x[1] >= 1).map(lambda x: x[0].split(","))

rdd_get = rdd_filter.map(lambda x: [ x[1],x[2] ])



# Get partitions of RDD

print(rdd_get.getNumPartitions())

# Modify partition with repartition (repartition can up and down partitions)
rdd_5part = rdd_get.repartition(8)
print(rdd_5part.getNumPartitions())


# Modify partition with coalesce (coalesce can only down partitions)
rdd_1part = rdd_get.coalesce(3)
print(rdd_1part.getNumPartitions())

# When save as text a RDD it uses the num of parttitons to create the output in this case 3 files with the data
rdd_1part.saveAsTextFile('outputs/RDD/07/exercise')

spark.stop()