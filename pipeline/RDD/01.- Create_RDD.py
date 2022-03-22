# import libraries
from pyspark import SparkConf, SparkContext

# We create configuration 
# This procees will be executed in local
# And its name is Test

sc = SparkContext(master='local', appName='CreateRDD')


# We create a RDD with a list 
rdd = sc.parallelize([1,2,3,4])

for c in rdd.collect():
    print(c)

sc.stop()