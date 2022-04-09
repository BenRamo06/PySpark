# import libraries
from pyspark import SparkConf, SparkContext

# We create configuration 
# This procees will be executed in local
# And its name is Test

sc = SparkContext(master='local', appName='CreateRDD')


# We create a RDD with a list 
rdd = sc.parallelize([1,2,3,4])

print('print rdd full')
for c in rdd.collect():
    print(c)


# We can create a emprty RDD
rdd_empty = sc.emptyRDD()


print('print empty rdd')
for c in rdd_empty.collect():
    print(c)




sc.stop()