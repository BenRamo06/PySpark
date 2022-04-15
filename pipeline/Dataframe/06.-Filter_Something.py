from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DateType


spark = SparkSession.builder.master("local").appName('Filter Something').getOrCreate()

data = spark.read.csv('inputs/pokemon.csv',header=True )


generations_get = [1,2]


data.filter((data.type1 == 'Ghost') & (data.generation.isin(generations_get))) \
    .filter(data.is_legendary.cast(IntegerType()) != 1) \
    .select(data.name, data.type1, data.type2, data.sp_attack, data.generation, data.is_legendary) \
    .show()


# We use "~" not operation to get differents values of condition

# data.filter((data.type1 == 'ghost') & (~data.generation.isin(generations_get))) \
#     .select(data.name, data.type1, data.type2, data.sp_attack, data.generation, data.is_legendary) \
#     .show()


spark.stop()