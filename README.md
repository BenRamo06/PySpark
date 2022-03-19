# PySpark Installation


### 1. Install Python 

### 2. Download Spark

We must download file Spark from https://spark.apache.org/downloads.html

After we downloaded the file, we must to do next steps:

*  Unzip the file : tar -xzf spark-1.2.0-bin-hadoop2.4.tgz
Note: spark-1.2.0-bin-hadoop2.4.tgz downloaded file

* Move unzip file to another location (if you want, you can change name of the folder and it will have a name more comfortable)

* Configure PATHS:
    * Open file bashrc (vim ~/.bashrc)
    * Add next variables:
        - export SPARK_HOME=<ROOT FOLDER UNZIP>   Example: SPARK_HOME=/home/user/local/spark
        - export PATH=$SPARK_HOME/bin:$PATH
    * Save and exit file (ESC --> wq --> enter)

* Open terminal and type: pyspark

Reference: https://www.sicara.ai/blog/2017-05-02-get-started-pyspark-jupyter-notebook-3-minutes


### 3. Apache Spark

Spark is a framework with distributed processing in memory (More faster)
Spark contains modules to process ML, Streaming and Batchs


Hadoop is a framework with distributed processing in disk
Hadoop is more useful with Batch data

We can use PySpark multiple language like to: Java, Scala, Python and R

![a](https://github.com/BenRamo06/PySpark/blob/master/images/ems5cAs.png)