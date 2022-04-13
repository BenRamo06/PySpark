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

* * **[parallelize()](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/01.-Create_RDD.py)** * *Distribute a local Python collection to form an RDD*

* **[textFile(path,minPartitions)](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/02.-Read_Something.py)** *Read a text file from HDFS, a local file system (available on all nodes), and return it as an RDD*     

* **stop()** *Shut down the SparkContext (it must be necessaty in our code).*

* **getOrCreate()** *it takes a SparkContext if it exists or it creates one.*


#### RDDs contains:


* **RDD transformations** – Are a kind of operation that takes an RDD as input and produces another RDD as output. Once a transformation is applied to an RDD, it returns a new RDD, the original RDD remains the same and thus are immutable


    * [*map():* ](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/03.-Process_Lambda.py)* : Transformation is used the apply operations on each elemnt in our RDD

    * *[filter(): ]*(https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/05.-Filter_Somenthing.py) : Transformation is used to filter the records in an RDD

    * [*toDF(): *](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/06.-RDD_to_DF.py) : Transformation is used to create a Dataframe of a RDD

    * sortByKey(): sorts the input data by keys from key-value pairs either in ascending or descending order

    * [*groupByKey(): *](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/08.-GroupByKey_Somenthing.py)  groups all the values in the given data with the same key together       


    
* **RDD actions** – These methods are applied on a resultant RDD and produces a non-RDD value

    * count() : Returns the number of elements of our RDD. 

    * distinct(): get distinct values in the RDD
    
    * collect(): Returns a list of all the elements of the RDD (we don't use it in production environments, because retrieve all aelemnts of the dataset in all * nodes) 
    
    * take(num): returns n first elements from the RDD
    
    * [*saveAsTextFile(path):*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py) serve the resultant RDD as a file
    
    * [*getNumPartitions()*:](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py) used to know how partitions have the RDD.
    
    * [*repartition(num):*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py) used to increase or decrease the RDD partitions
    
    * [*coalesce(num):*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/RDD/07.-Task_Partitions.py) used to only decrease the RDD partitions
    
    * union(rdd): union between RDDS 
    
    * zip(): create tuples win two RDD rdd1.zip(rdd2)


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

* [*.createDataFrame(data[, schema, …]) : *](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/01.-Create_Dataframe.py) Creates a DataFrame from an RDD, a list or a pandas.DataFram

* *.stop():* Shut down the SparkContext (it must be necessaty in our code).

* *.builder.appName(name):* Sets a name for the application
 
* *.getOrCreate():* it takes a SparkContext if it exists or it creates one.

* [*.read() : *](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/04.-Read_something.py) Read from a file to Dataframe

* [*.sparkContext:*: ](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/09.-DF_process_RDD.py) Returns the underlying SparkContext

#### Attributes Dataframe

* .columns : get name columns in Dataframe

* .dtypes: get columns and datatype in tuples

* .schema: get schema in format StrcutType and StructField


#### Methods Dataframe

* [*.select() :*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/05.-Select_Somenthing.py) get columns of Dataframe

* [*.where/filter() :*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/06.-Filter_Something.py) filter dataframe

* [*.join() :*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/08.-Join_Something.py) join dataframes with different ways

* [*.union() :*]() union two dataframes with the same schema (this include duplicated values)

* [*.distinct() :*]() eliminate duplicated rows

* [*.createOrReplaceTempView(name) / .createTempView(name) : *](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/11.-SQL_Dataframe.py) The lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame
    

* [*.createOrReplaceGlobalTempView(name) / .createGlobalTempView(name) :*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/11.-SQL_Dataframe.py) The lifetime of this temporary view is tied to this Spark application.

* [*.groupBy(cols) :*](https://github.com/BenRamo06/PySpark/blob/master/pipeline/Dataframe/07.-GroupBy_Having_Somenthing.py) Group by columns
    .agg(function_agg(col))
        


#### Functions

* alias(name): set name of a column in Dataframe

* lit(value): add literall value

* cast(new_data_type) : convert column a new data type

* when() : expresion of conditions like to Case in ANSI-SQL

* isNotNull() : validate if a column is not null

* isNull() : validate if a column is null

* between(ini,end): if a columns 

* asc(col): Return ascending of columns

* desc(col): Return descending of columns

* coalesce(col,col): return first column not null

* current_date() : return current_date

* date_add(date, days): add days a date give

* date_format(date,format): convert date to format string

* date_sub(date, days): sub days to date give

* to_date(col, format)_: cast col to date

* drop(col) : drop column

* fillna(value, subset): replace null values in subset(column)

* countDistinct(col1,[col2]..): return count distinct values

* sumDistinct(col1,[col2]..): return sum distinct values


#### Window Functions

* row_number(): Returns a sequential number starting from 1 within a window partition

* rank(): Returns the rank of rows within a window partition, with gaps.

* dense_rank(): Returns the rank of rows within a window partition without any gaps. Where as Rank() returns rank with gaps.

* lag(Col, offset): returns the value that is `offset` rows before the current row, and `null` if there is less than `offset` rows before the current row.

* lead(Col, offset): returns the value that is `offset` rows after the current row, and `null` if there is less than `offset` rows after the current row.


