from pyspark.sql.functions import col, lit, when,  current_date, date_format, desc, asc, to_date, to_timestamp, count, sum, udf
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession



def parse_generation(generation) -> str:

    match generation:
        case 1:
            return "First generation"
        case 2:
            return "Second generation"
        case 3:
            return "Third generation"
        case _:  # The wildcard pattern acts as the default case
            return "Invalid option"
        

spark = SparkSession.builder \
                    .master("local[3]") \
                    .appName("Udf Function") \
                    .getOrCreate()

pokemon = spark.read \
               .format("csv") \
               .option("header", "true") \
               .option("inferSchema", "true") \
               .load("sources/pokemon.csv")


pokemon_type = pokemon.select("#", "generation", "type1") \
                      .groupBy("generation", "type1") \
                      .count()
 
parse_generation_udf = udf(parse_generation, StringType())
pokemon_gen = pokemon_type.withColumn("generation", parse_generation_udf("generation"))


pokemon_gen.show()
