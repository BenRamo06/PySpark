from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, DateType
from pyspark.sql.functions import col, lit, when,  current_date, date_format, desc, asc, to_date, to_timestamp, count, sum


spark = SparkSession.builder.master("local").appName('Group Something').getOrCreate()

data = spark.read.csv('/home/benito.ramos/Desktop/GIT/PySpark/inputs/pokemon.csv',header=True )

data = data.select(
                # Select a column of dataframe
                   data.name,
                   data.generation, 
                   data.is_legendary,
                # Select a column with new alias
                   data.type1.alias("Tipo"), 
                   data.type2.alias("Tipo2"),
                # create a column with a value   
                   lit(1).alias("NewCol").cast(IntegerType()),
                # create a column with a case sentence    
                   when(data.type1.isNotNull() & data.type2.isNull()  , 'Only Type 1')
                   .when(data.type1.isNull() & data.type2.isNotNull()  , 'Only Type 2')
                   .when(data.type1.isNotNull() & data.type2.isNotNull()  , 'Both Types')
                   .otherwise('No se').alias('TypeCustom'),
                # create a column with arithmetic operation
                   (data.sp_attack + 100).alias('Attack100'),
                # create a column with sentence between
                   when((data.sp_attack + 100).between(170,500), 'HEAVY')
                   .otherwise('LIGHT').alias('AttackCustom'),

                # get current date
                   current_date().alias('GetDate'),
                # date to format string
                   date_format(current_date(), 'dd/MM/yy').alias('GetDate_Format'),

                # string to date
                  to_date(lit('01-01-2022'), 'dd-MM-yyyy').alias("StringToDate"),
                # string to datetime
                  to_timestamp(lit('01-01-2022 06:10:00'), 'dd-MM-yyyy HH:mm:ss').alias("StringToDate")

                # Order by descendent for new column "Tipo"
                  ).orderBy(desc("Tipo"))



# ------ Group by One function ------ 

# data.groupBy(data.generation).count().show()


# ------ Group by One function multiple columns ------ 

# data.groupBy(data.generation).sum("Attack100","NewCol").show()


# ------ Group by many function ------ 

# data.where(data.is_legendary == 1) \
#     .groupBy(data.generation) \
#       .agg(count(data.NewCol).alias("Conteo"),
#            sum(data.Attack100).alias("SumAttack")) \
#     .show()



# ------ Group by with where, having and order by ------ 


data.where(data.is_legendary == 1) \
    .groupBy(data.generation) \
      .agg(count(data.NewCol).alias("Conteo"),
           sum(data.Attack100).alias("SumAttack")) \
    .where(col('Conteo') >= 10) \
    .orderBy(asc('SumAttack')).show()

spark.stop()