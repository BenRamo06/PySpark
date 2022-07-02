from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import window, count, session_window

spark = SparkSession.builder.master("local").appName("Windowing_tumbling").getOrCreate()

# Sample Data is generated for windowing examples
windowingData = (
("12", "2019-01-02 15:30:00"),
("12",  "2019-01-02 15:30:30"),
("12",  "2019-01-02 15:31:00"),
("12",  "2019-01-02 15:31:50"),
("12",  "2019-01-02 15:31:55"),
("16",  "2019-01-02 15:33:00"),
("16",  "2019-01-02 15:35:20"),
("16",  "2019-01-02 15:37:00"),
("20",  "2019-01-02 15:30:30"),
("20",  "2019-01-02 15:31:00"),
("20",  "2019-01-02 15:31:50"),
("20",  "2019-01-02 15:31:55"),
("20",  "2019-01-02 15:33:00"),
("20",  "2019-01-02 15:35:20"),
("20",  "2019-01-02 15:37:00"),
("20",  "2019-01-02 15:40:00"),
("20",  "2019-01-02 15:45:00"),
("20",  "2019-01-02 15:46:00"),
("20",  "2019-01-02 15:47:30"),
("20",  "2019-01-02 15:48:00"),
("20",  "2019-01-02 15:48:10"),
("20",  "2019-01-02 15:48:20"),
("20",  "2019-01-02 15:48:30"),
("20",  "2019-01-02 15:50:00"),
("20",  "2019-01-02 15:53:00"),
("20",  "2019-01-02 15:54:30"),
("20",  "2019-01-02 15:55:00"),
("22",  "2019-01-02 15:50:30"),
("22",  "2019-01-02 15:52:00"),
("22",  "2019-01-02 15:50:30"),
("22",  "2019-01-02 15:52:00"),
("22",  "2019-01-02 15:50:30"),
("22",  "2019-01-02 15:52:00"))

columns = ["eventId", "timeReceived"]

# We create our DF
windowing_df = spark.createDataFrame(data = windowingData, schema = columns)

# Order DF to see the result
windowing_df = windowing_df.sort(windowing_df.timeReceived.asc())

# Print DF
windowing_df.show(40, truncate=False)



session = windowing_df.groupBy(session_window("timeReceived", "5 minutes")) \
                       .agg(count("eventId").alias("conteo")) 
                    

session.show(truncate=False)


# We have another view where We show their respective window for each row

session = windowing_df.select("eventId","timeReceived",session_window("timeReceived", "5 minutes")).orderBy("timeReceived")


session.show(truncate=False)