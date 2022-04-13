from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType

spark = SparkSession.builder.appName('ToDataframe').getOrCreate()


# We read a file with minPartitions equal 3

rdd_data = spark.sparkContext.textFile('inputs/pokemon.csv',minPartitions=5).zipWithIndex()

rdd_filter = rdd_data.filter(lambda x: x[1] >= 1) \
                     .map(lambda x: x[0].split(",")) \
                     .filter(lambda x: int(x[11])==1)

rdd_get = rdd_filter.map(lambda x: ( x[2],x[1] ) )

out = rdd_get.groupByKey().mapValues(list)

print(out.take(10))

spark.stop()