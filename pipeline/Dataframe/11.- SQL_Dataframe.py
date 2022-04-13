from pyspark import SparkContext
from pyspark.sql import SparkSession



spark = SparkSession.builder.master("local").appName('Write Something').getOrCreate()


read = spark.read.options(delimiter=",", header=True).csv("/home/benito.ramos/Desktop/GIT/PySpark/inputs/pokemon.csv")

read.createOrReplaceTempView("pokemon")

spark.sql(sqlQuery= """SELECT NAME,          
                            TYPE1 AS Tipo,   
                            TYPE2 AS Tipo2, 
                            "1" AS Newcol,
                            CASE
                                WHEN TYPE1 IS NOT NULL AND TYPE2 IS NULL THEN "Only Type 1"
                                WHEN TYPE1 IS NOT NULL AND TYPE2 IS NOT NULL THEN "Both Types"
                                ELSE "NO SE"
                            END AS TypeCustom,
                            (SP_ATTACK + 100) AS Attack100,
                            CASE
                                WHEN (SP_ATTACK + 100) BETWEEN 170 AND 500 THEN "HEAVY"
                                ELSE "LIGHT"
                            END AS AttackCustom,
                            current_date(),
                            date_format(current_date(), "dd/MM/yy") AS GetDate_Format,
                            to_date("01-01-2022", "dd-MM-yyyy") AS StringToDate,
                            to_timestamp("01-01-2022 06:10:00", "dd-MM-yyyy HH:mm:ss") AS StringToDate
                      FROM POKEMON
                      WHERE TYPE1 = "ghost"
                      ORDER BY Tipo DESC, Tipo2 DESC """).show()


