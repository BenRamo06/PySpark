from tokenize import group
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Test')
sc = SparkContext(conf = conf)


read_file = sc.textFile('inputs/data_movies')

divide_element = read_file.map(lambda x: x.split(','))

for element in divide_element.collect():
    print(element)
