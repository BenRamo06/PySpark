from asyncore import read
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Test').getOrCreate()

# conf = SparkConf().setMaster('local').setAppName('Test')
# sc = SparkContext(conf = conf)


read_file = spark.read.csv('inputs/data_movies')


print(type(read_file))


# struct_elemement = read_file.map(lambda x: x.split(','))



# for element in read_file.collect():
#     print(element)