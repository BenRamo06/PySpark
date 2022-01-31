from tokenize import group
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Test')
sc = SparkContext(conf = conf)


def read_file_divide(element):
    return element.split(',')


read_file = sc.textFile('inputs/data_movies')

divide_element = read_file.map(read_file_divide)

filter_Anakin = divide_element.filter(lambda x: x[0] == 'ANAKIN SKYWALKER')

for element in filter_Anakin.collect():
    print(element)
