from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DateType
from pyspark.sql.functions import col, lit, when,  current_date, date_format, desc, asc, to_date, to_timestamp, count, sum


spark = SparkSession.builder.master("local").appName('Join Something').getOrCreate()


schema = StructType([StructField("id", IntegerType(), True),
                     StructField("value", StringType(), True)
                    ])


data = spark.read.csv('/home/benito.ramos/Desktop/GIT/PySpark/inputs/pokemon.csv',header=True )
data = data.filter((data.generation == 1) & (data.pokedex_number.between(1,10))).select(data.name, data.type1, data.pokedex_number) # Get 151 rows

pokemon =  spark.createDataFrame([[1,'Initial'],
                                  [4,'Initial'],
                                  [7,'Initial'],
                                  [1500, 'Initial']], schema= schema)



# Inner Join

# pokemon.join(other= data, on= pokemon.id == data.pokedex_number, how="inner") \
#        .select(pokemon.id, data.name) \
#        .show()


# Left Join

# pokemon.join(other= data, on= pokemon.id == data.pokedex_number, how="left") \
#        .where(data.pokedex_number.isNull()) \
#        .show()


# Right Join

# pokemon.join(other= data, on= pokemon.id == data.pokedex_number, how="right") \
#        .select(pokemon.id, data.name) \
#        .where(pokemon.id.isNull()) \
#        .show()



# Full Join

# pokemon.join(other= data, on= pokemon.id == data.pokedex_number, how="full") \
#        .select(pokemon.id, data.pokedex_number, data.name) \
#        .orderBy(pokemon.id.desc()).show(truncate=False)



# Anti, get only left columns similar to right columns key is null

# pokemon.join(other= data, on=  data.pokedex_number == pokemon.id, how="anti") \
#        .show()

# data.join(other= pokemon, on=  data.pokedex_number == pokemon.id, how="anti") \
#        .show()




# Semi, similar join , returns only columns of LEFT side


# pokemon.join(other= data, on=  data.pokedex_number == pokemon.id, how="semi") \
#        .show()

# data.join(other= pokemon, on=  data.pokedex_number == pokemon.id, how="semi") \
#        .show()




spark.stop()