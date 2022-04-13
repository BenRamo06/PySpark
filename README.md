# PySpark Installation


### 1. Install Python 

---

### 2. Download Spark

We must download file Spark from https://spark.apache.org/downloads.html

After we have downloaded the file, we must do next steps:

*  Unzip the file : 
    ```bash 
        tar -xzf spark-1.2.0-bin-hadoop2.4.tgz 
    ```
    **note**: spark-1.2.0-bin-hadoop2.4.tgz will be unzip file name

* Move unzip file to another location (if you want, you can change name of the folder and it will have a name more comfortable)

* Configure PATHS:
    * Open file bashrc 
        ```bash
            vim ~/.bashrc
        ```

    * Add next variables:

        ```bash
            export SPARK_HOME=<ROOT FOLDER UNZIP>   Example: SPARK_HOME=/home/user/local/spark
            export PATH=$SPARK_HOME/bin:$PATH
        ```

    * Save and exit file 
    
        ```bash 
            ESC --> wq --> enter 
        ```

* Open terminal and type: pyspark

<p align="center">
  <img width="340" src="https://github.com/BenRamo06/PySpark/blob/master/images/SparkInstallation.png")>
</p>



Reference: https://www.sicara.ai/blog/2017-05-02-get-started-pyspark-jupyter-notebook-3-minutes

---

### 3. What is Apache Spark?

Spark is a data processing engine for big data sets. Like Hadoop, Spark splits up large tasks across different nodes. However, it tends to perform faster than Hadoop and it uses random access memory (RAM) to cache and process data instead of a file system

The Spark engine was created to improve the efficiency of MapReduce (Hadoop) and keep its benefits. Even though Spark does not have its file system, it can access data on many different storage solutions. The data structure that Spark uses is called Resilient Distributed Dataset, or RDDs.

RDD is a distributed set of elements stored in partitions on nodes across the cluster. The size of an RDD is usually too large for one node to handle. Therefore, Spark partitions the RDDs to the closest nodes and performs the operations in parallel. The system tracks all actions performed on an RDD by the use of a Directed Acyclic Graph (DAG).

**Note**: Hadoop is a framework with distributed processing in disk (HDFS + Map Reduce)       


<p align="center">
  <img src="https://github.com/BenRamo06/PySpark/blob/master/images/ems5cAs.png">
</p>



The Spark ecosystem consists of five primary modules:

* Spark Core: Underlying execution engine that schedules and dispatches tasks and coordinates input and output (I/O) operations.
* Spark SQL: Gathers information about structured data to enable users to optimize structured data processing.
* Spark Streaming and Structured Streaming: Both add stream processing capabilities. Spark Streaming takes data from different streaming sources and divides it into micro-batches for a continuous stream. Structured Streaming, built on Spark SQL, reduces latency and simplifies programming.
* Machine Learning Library (MLlib): A set of machine learning algorithms for scalability plus tools for feature selection and building ML pipelines. The primary API for MLlib is DataFrames, which provides uniformity across different programming languages like Java, Scala and Python.
* GraphX: User-friendly computation engine that enables interactive building, modification and analysis of scalable, graph-structured data.

We can use PySpark multiple language like to: Java, Scala, Python and R

<p align="center">
  <img src="https://github.com/BenRamo06/PySpark/blob/master/images/EcosystemSpark.png">
</p>


**Use Cases Apache Spark**

*   The analysis of real-time stream data.
*   When time is of the essence, Spark delivers quick results with in-memory computations.
*   Dealing with the chains of parallel operations using iterative algorithms.
*   Graph-parallel processing to model the data.
*   All machine learning applications.


---

### 4. SparkContext and SparkSession

SparkContext is Core API of Spark, after of version 2.0, Spark gave us SparkSession that is an unified API (SparkContext, StreamingContext and SQLContext)

<p align="center">
  <img src="https://github.com/BenRamo06/PySpark/blob/master/images/Session_Context.png">
</p>

<p align="center">
  <img src="https://github.com/BenRamo06/PySpark/blob/master/images/SessionsVsContext.png">
</p>


---

### 5. RDD (Resilient Distributed Datasets)


Collection of elements partitioned across the nodes of the cluster that can be operated on in parallel. 

#### Benefits and concepts

- [x] Unit base of Spark
- [x] They are immutable (Consistency).
- [x] Fail tolerant.
- [x] They do parallel processing as also partitioning across cluster (Performance)
- [x] They don't have defined schema.
- [x] They contain pasive execution
- [x] Compilation errors            

#### Use cases

*   When we want to do low-level transformations        
*   Unstrucutred data       
*   Schema is unimportant      



#### sparkContext

* **_[parallelize():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/01.-Create_RDD.py)_** *Distribute a local Python collection to form an RDD*

* **_[textFile(path,minPartitions):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/02.-Read_Something.py)_** *Read a text file from HDFS, a local file system (available on all nodes), and return it as an RDD*     

* **_stop():_** *Shut down the SparkContext (it must be necessaty in our code).*

* **_getOrCreate():_** *it takes a SparkContext if it exists or it creates one.*


#### RDDs contains:


* **RDD transformations** – Are a kind of operation that takes an RDD as input and produces another RDD as output. Once a transformation is applied to an RDD, it returns a new RDD, the original RDD remains the same and thus are immutable


    * **_[map():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/03.-Process_Lambda.py)_** *Transformation is used the apply operations on each elemnt in our RDD*

    * **_[filter():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/05.-Filter_Somenthing.py)_** *Transformation is used to filter the records in an RDD*

    * **_[toDF():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/06.-RDD_to_DF.py)_** *Transformation is used to create a Dataframe of a RDD*

    * **_sortByKey():_** *sorts the input data by keys from key-value pairs either in ascending or descending order*

    * **_[groupByKey():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/08.-GroupByKey_Somenthing.py)_** *groups all the values in the given data with the same key together*


    
* **RDD actions** – These methods are applied on a resultant RDD and produces a non-RDD value

    * **_count():_** *Returns the number of elements of our RDD.*

    * **_distinct():_** *get distinct values in the RDD*
    
    * **_collect():_** *Returns a list of all the elements of the RDD (we don't use it in production environments, because retrieve all aelemnts of the dataset in all * nodes)*
    
    * **_take(num):_** *returns n first elements from the RDD*
    
    * **_[saveAsTextFile(path):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py)_** *serve the resultant RDD as a file*
    
    * **_[getNumPartitions():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py)_** *used to know how partitions have the RDD.*
    
    * **_[repartition(num):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py)_** *used to increase or decrease the RDD partitions*
    
    * **_[coalesce(num):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py)_** *used to only decrease the RDD partitions*
    
    * **_union(rdd):_** *union between RDDS*
    
    * **_zip():_** *create tuples win two RDD rdd1.zip(rdd2)*


---

### 6. Dataframes


#### Benefits and concepts

- [x] They contain a schema (columns and data types) or it can be infer.
- [x] They do parallel processing
- [x] Runtime errors

#### Use cases

* structured and semistructured data
* Data requires a structure
* Transformations are high-level.



#### Spark Session

* **_[.createDataFrame(data[, schema, …]):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/01.-Create_Dataframe.py)_** *Creates a DataFrame from an RDD, a list or a pandas.DataFrame*

* **_.stop():_** *Shut down the SparkContext (it must be necessaty in our code).*

* **_.builder.appName(name):_** *Sets a name for the application*
 
* **_.getOrCreate():_** *it takes a SparkContext if it exists or it creates one.*

* **_[.read():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/04.-Read_something.py)_** *Read from a file to Dataframe*

* **_[.sparkContext:](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/09.-DF_process_RDD.py)_** *Returns the underlying SparkContext*

#### Attributes Dataframe

* **_.columns:_** *get name columns in Dataframe*

* **_.dtypes:_** *get columns and datatype in tuples*

* **_.schema:_** *get schema in format StrcutType and StructField*


#### Methods Dataframe

* **_[.select():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/05.-Select_Somenthing.py)_** *get columns of Dataframe*

* **_[.where/filter():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/06.-Filter_Something.py)_** *filter dataframe*

* **_[.join():](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/08.-Join_Something.py)_** *join dataframes with different ways*

* **_.union():_** *union two dataframes with the same schema (this include duplicated values)*

* **_.distinct():_** *eliminate duplicated rows*

* **_[.createOrReplaceTempView(name) / .createTempView(name):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/11.-SQL_Dataframe.py)_** *The lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame*
    
* **_[.createOrReplaceGlobalTempView(name) / .createGlobalTempView(name):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/11.-SQL_Dataframe.py)_** *The lifetime of this temporary view is tied to this Spark application.*

* **_[groupBy(cols):](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/07.-GroupBy_Having_Somenthing.py)_** *Group by columns* <br>
  **_.agg(function_agg(col)):_** *function of aggregation*
        


#### Functions

* **_.alias(name):_** *set name of a column in Dataframe*

* **_.lit(value):_** *add literall value*

* **_.cast(new_data_type):_** *convert column a new data type*

* **_.when():_** *expresion of conditions like to Case in ANSI-SQL*

* **_.isNotNull():_** *validate if a column is not null*

* **_.isNull():_** *validate if a column is null*

* **_.between(ini,end):_** *if a columns*

* **_.asc(col):_** *Return ascending of columns*

* **_.desc(col):_** *Return descending of columns*

* **_.coalesce(col,col):_** *return first column not null*

* **_.current_date():_** *return current_date*

* **_.date_add(date, days):_** *add days a date give*

* **_.date_format(date,format):_** *convert date to format string*

* **_.date_sub(date, days):_** *sub days to date give*

* **_.to_date(col, format):_** *cast col to date*

* **_.drop(col):_** *drop column*

* **_.fillna(value, subset):_** *replace null values in subset(column)*

* **_.countDistinct(col1,[col2]..):_** *return count distinct values*

* **_.sumDistinct(col1,[col2]..):_** *return sum distinct values*


#### Window Functions

* **_.row_number():_** *Returns a sequential number starting from 1 within a window partition

* **_.rank():_** *Returns the rank of rows within a window partition, with gaps.*

* **_.dense_rank():_** *Returns the rank of rows within a window partition without any gaps. Where as Rank() returns rank with gaps.*

* **_.lag(Col, offset):_** *returns the value that is `offset` rows before the current row, and `null` if there is less than `offset` rows before the current row.*

* **_.lead(Col, offset):_** *returns the value that is `offset` rows after the current row, and `null` if there is less than `offset` rows after the current row.*


