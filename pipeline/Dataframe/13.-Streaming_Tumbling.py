from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import window, count

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


# We create a tumbling window on timeReceived field with 10 minutes of difference between each window
# We select initial,end window and count of rows between windows
tumbling = windowing_df.groupBy(window("timeReceived", "10 minutes")) \
                       .agg(count("eventId").alias("conteo")) \
                       .select("window.start","window.end", "conteo" ).orderBy("window.start")

tumbling.show(truncate=False)


# We have another view where We show its respective window for each row

tumbling = windowing_df.select("eventId","timeReceived",window("timeReceived", "10 minutes"), "window.start","window.end")


tumbling.show(truncate=False)