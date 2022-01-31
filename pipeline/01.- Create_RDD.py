# import libraries
from pyspark import SparkConf, SparkContext

# We create configuration 
# This procees will be executed in local
# And its name is Test
conf = SparkConf().setMaster('local').setAppName('Test')

# We create SparkContext with configuration previosly created
sc = SparkContext(conf = conf)


# We create a RDD with a list 
rdd = sc.parallelize([[1,2],
                      [3,4]])


for element in rdd.collect():
    print(element)

# sc.stop()