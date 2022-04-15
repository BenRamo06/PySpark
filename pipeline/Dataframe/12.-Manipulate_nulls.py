from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DateType
import numpy as np

spark = SparkSession.builder.master("local").appName('Filter Something').getOrCreate()

schema = StructType([StructField('id', IntegerType(), True),  # name col, data type, is nullable?
                     StructField('num', IntegerType(), True),
                     StructField('num2', IntegerType(), True)
                    ])


# Create DF with defined schema
df = spark.createDataFrame([[1,None,3],
                            [4,5,None],
                            [None,7,8]], schema)

df.show()


# df.na.drop().show()  # Eliminate row if it one column contains a null value  (note: "how=any" by default)

# df.na.drop(how='all').show() #Eliminate column if all columns contain a null value 

#df.na.drop(how='any', subset=['num','num2']).show() # Eliminate rows if contains any null value in num and num2 columns

# df.na.fill(0).show() # fill all null values witj zero

# df.na.fill(0,['num','num2']).show() # fill a value in columns specified

# df.na.fill({'id':4, 'num2': 100})


# df.na.replace(8, 99).show() # replace a value with other.

# df.na.replace({8: 99}).show() # replace a value with other.

# df.na.replace([8,1],[99,99]).show() # replace  list vs list

# df.na.replace([5,7],[99,99], subset=['num']).show() # replace  list vs list in a column specified

spark.stop()