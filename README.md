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


    Hadoop is a framework with distributed processing in disk (HDFS + Map Reduce)
    Hadoop is more useful with Batch data

    We can use PySpark multiple language like to: Java, Scala, Python and R

![a](https://github.com/BenRamo06/PySpark/blob/master/images/ems5cAs.png)


### 4. RDD (Resilient Distributed Datasets)

* Unit base of Spark
* They are immutable.
* Fail tolerant.
* They do parallel processing as also partitioning across cluster
* They don't have defined structure.
* They contain pasive  execution


### 5. Dataframes

* They contain columns and data types.

This structure must be used if we will use high level task like to: filter, mapping, agregations, avarages or sums



### 6. SparkContext and SparkSession

SparkContext is Core API of Spark, after of version 2.0, Spark gave us SparkSession that is an unified API (SparkContext, StreamingContext and SQLContext)

![a](https://github.com/BenRamo06/PySpark/blob/master/images/SessionsVsContext.png)



### HADDOP


Spark (Processing Memory, batch and streaming)
	Bounded - DataFrames
	UnBounded - DStreams


Data Proc (Compute and Storage separated)

	Best Practices

		- Use GCS rather than HDFS
		- DataProc and GCS must be in the same region for Latency purpose
		- If we have more than 10K input file. We need to create files with more capacity

	Benefits
		- Low cost  --> 1 c per virtual cpu per cluster per hour
		- Fast 		--> to start, scale and shut down near 90 seconds or less on average  
		- Reizable  --> Cluster can be created and scaled quickly
		- Open Source --> You can use hadoop or spark, because Dataproc manages updates
		- Versioning --> Allows you to switch different version of hadoop or any tool (spark, hive, pig)
		- High Availability


Hadoop (Processing Disk, batch, Compute and Storage together, Master/Slave Architecture)


	Storage --> HDFS (Hadoop Distruibed File System)
					- Block Structured file system
					- Files is divided into blocks across cluster
					- 128 MB is default block storage

					- What if a data node crashes?
					  Do we lose this piece of data?
					  When a block is created it is replicated and stored on different data nodes (Replication Method/Factor, 3 nodes replication by default)
					  Hence, HDFS doesn't lose data even if a node crashed (FAIL TOLERANT)
					  


	Process --> MapReduce
					- Split data in parts to process and every part will be processed separtly  in different data node
					- Has 4 phases:
						
						* Split				= Input is split into fragments (Block) across cluster.
						* Mapper phases		= Each block will have a map task, where it will process a set of key-value pair.
						* Shuffle and sort  = Key value pair is sorted and grouped in 
						* Reduce phase 		= All grouped words are counted




	Execution --> YARN (Yet another resource negotiator)

					- Manage Resources = RAM, network, bandwith and cpu
					- Resource manager = assign resource
					  Node manager     = handle nodes and monitor resources in the node






	Name Node (Master)
					- Maintains and manages blocks on the DataNodes (slave nodes)
					- Record metadata of the blocks (location(node), size, permissions, hierarchy)
						There are two files associated with the metadata:
							FsImage: It contains the complete state of the file system namespace since the start of the NameNode.
							EditLogs: It contains all the recent modifications made to the file system with respect to the most recent FsImage.
					- Receives a Heartbeat and a block report from all the DataNodes in the cluster to ensure that the DataNodes are live.
					- Responsible to take care of the replication factor of all the blocks
					- In case of the DataNode failure, the NameNode chooses new DataNodes for new replicas,
	Data nodes (Slaves)
					- Store actual data
					- Process data
					- They send heartbeats to the NameNode periodically to report the overall health of HDFS, by default, this frequency is set to 3 seconds.
					


	Secondary NameNode/CheckpointNode:
					- Works concurrently with the primary NameNode as a helper daemon
					- The Secondary NameNode is one which constantly reads all the file systems and metadata from the RAM of the NameNode and writes it into the hard disk or the file system.

	Disventages:

		 it's part of the cluster which means even if you're not running jobs that use the compute hardware on the cluster you still have to pay for that power for the cluster to persist all of that storage this is the disadvantage of tying together compute and storage







What is a cluster
	Cluster is a group of interconnected computers (know as nodes) thant can work together on the same problem.


What is ACID?



Work Tamplates (crear cluster y destruirlos.)
3 Sección --> 

Cluster long live?
Cluster Ephimeros?




#### Questions

¿Qué tendría que hacer para migrar mis proceso a GCP?
¿Que desventajas se tienen si se queda el storage en on-premise?
¿Cómo paso mis datos a GCS?
	¿Conocer el tamaño de la información y qué necesito?.
		¿Cloud Connector?
		Si es menos de 1 TB por gsutil.
		Si es más de 1TB por Transfer Appliance.
¿Como gastar menos en Storage? --> Cambio de clase para menor costo
¿Como gastar menos en procesamiento?
	Pre-empable --> 
	Cluster Ephimeral --> 


Tu puedes hacer una reserva de Pre-mtible machines y correr sobre esa reserva.

Un cluster debe de contener:
	%on demand
	%prem-tible 


El cluster es tolerante a fallo, no la maquina.



Alta disponibilidad --> Que los recursos esten disponibles (nodo primario a secundario, puede ser primario.)
