import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Test').getOrCreate()


# We create a RDD
rdd = spark.sparkContext.parallelize([[1,2],
                                      [3,4]])

# Defined name columns with a list
cols = ['id', 'num']

# Convert RDD to Dataframe
df_of_rdd = rdd.toDF(cols)

# Print Dataframe
df_of_rdd.show()

# Print schema of DF
df_of_rdd.printSchema()