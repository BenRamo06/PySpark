
from pyspark import SparkConf, SparkContext

sc = SparkContext(master='local', appName='LambdaRDD')

read_file = sc.textFile('inputs/data_movies')

divide_element = read_file.map(lambda x: x.split(','))

for element in divide_element.collect():
    print(element)


print(divide_element.take(5))


sc.stop()