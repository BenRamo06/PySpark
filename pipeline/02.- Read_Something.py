from tokenize import group
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Test')
sc = SparkContext(conf = conf)


# We create a RDD with a flat file 
read_file = sc.textFile('inputs/data_movies')

for element in read_file.collect():
    print(element)

# sc.stop()