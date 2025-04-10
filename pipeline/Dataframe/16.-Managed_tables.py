from pyspark.sql import SparkSession


spark = SparkSession.builder \
                    .master("local[3]") \
                    .appName("MamagedTable") \
                    .enableHiveSupport() \
                    .getOrCreate()

pokemon = spark.read \
               .format("csv") \
               .option("header", "true") \
               .option("inferSchema", "true") \
               .load("sources/pokemon.csv")

spark.sql("CREATE DATABASE IF NOT EXISTS POKEMON_DB")
spark.catalog.setCurrentDatabase("POKEMON_DB")

pokemon_type = pokemon.where(" generation = 1") \
                      .select("#", "type1") \
                      .groupBy("type1") \
                      .count()

pokemon_type_parquet = pokemon_type.write.mode("overwrite").saveAsTable("pokemon_by_type")

print(spark.catalog.listTables("POKEMON_DB"))
