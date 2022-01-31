from tokenize import group
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Test')
sc = SparkContext(conf = conf)


def read_file_divide(element, sep):
    return element.split(sep)


read_file = sc.textFile('inputs/data_movies')

divide_element = read_file.map(lambda x: read_file_divide(x,sep=','))

for element in divide_element.collect():
    print(element)
