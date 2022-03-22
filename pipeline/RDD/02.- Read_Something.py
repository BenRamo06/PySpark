
from pyspark import SparkConf, SparkContext

sc = SparkContext(master='local', appName='ReadSomethingRDD')


# We create a RDD with a flat file 
read_file = sc.textFile('inputs/data_movies')

# print for each elemnt
for element in read_file.collect():
    print(element)

sc.stop()