from pyspark.sql import SparkSession


spark = SparkSession.builder.master("local").appName('Read Something').getOrCreate()

data = spark.read.csv('/home/benito.ramos/Desktop/GIT/PySpark/inputs/data_movies',inferSchema=True, header=False )

data.show()

data.printSchema()

spark.stop()