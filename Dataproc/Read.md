# HADDOP - SPARK - DATAPROC

What is a cluster
	Cluster is a group of interconnected computers (know as nodes) thant can work together on the same problem.






### **Hadoop (Processing Disk, batch, Compute and Storage together, Master/Slave Architecture)**

#### **Storage --> HDFS (Hadoop Distruibed File System)**
- A file systems are files are arranged in a hierarchy of folders, File systems are designed to allow for random writes anywhere in the file.
- Block Structured file system
- Files are divided into blocks and they are distributed in nodes (workers|slaves) across the cluster
- 128 MB is default configuration block size

- What if a data node crashes? Do we lose this piece of data?				

     When a block is created it is replicated and stored on different data nodes (Replication Method/Factor, 3 nodes replication by default)
   
     Hence, HDFS doesn't lose data even if a node crashed (FAIL TOLERANT)	
		  


#### **Process --> MapReduce (big data processing, parallel processing)**
- Split data in parts to process and every part will be processed separtly  in different data node
- Has 4 phases:

	* Split				= Input is split into shards (Block)
	* Mapper phases		= Each block will have a map task (parse, tranform, filter data), where it will process 
						zero to N key-value pair.
	* Combiner          = can group data un map phase, Reduces amout of data to move over network.
	* Partitioner      = Splits KV pairs into shards, one per reducer
	* Shuffle and sort  = Downloads partitioners data, sorts and groups by key i
	* Reduce phase 		= Runs reduce function once per key grouping to aggregate, filter or combine. It sends zero to N KV pairs
	* Output			= Transalate final KV pair and writes



#### **Execution --> YARN (Yet another resource negotiator)**

- Manage Resources = RAM, network, bandwith and cpu
- Resource manager = assign resource
- Node manager     = handle nodes and monitor resources in the node


#### **Name Node (Master)**
- Maintains and manages blocks on the DataNodes (slave nodes)
- Record metadata of the blocks (location(node), size, permissions, hierarchy)
- There are two files associated with the metadata:
	* FsImage: It contains the complete state of the file system namespace since the start of the NameNode.
	* EditLogs: It contains all the recent modifications made to the file system with respect to the most recent FsImage.
- Receives a Heartbeat and a block report from all the DataNodes in the cluster to ensure that the DataNodes are live.
- Responsible to take care of the replication factor of all the blocks
- In case of the DataNode failure, the NameNode chooses new DataNodes for new replicas,


#### **Data nodes (Slaves)**
- Store actual data
- Process data
- They send heartbeats to the NameNode periodically to report the overall health of HDFS, by default, this frequency is set to 3 seconds.


#### **Secondary NameNode/CheckpointNode**
- Works concurrently with the primary NameNode as a helper daemon
- The Secondary NameNode is one which constantly reads all the file systems and metadata from the RAM of the NameNode and writes it into the hard disk or the file system.

#### **Disventages**

it's part of the cluster which means even if you're not running jobs that use the compute hardware on the cluster you still have to pay for that power for the cluster to persist all of that storage this is the disadvantage of tying together compute and storage
Storage and Processing are join


#### **When uset it**

- When you have thousands of partitions and directories, and each file size is relatively small
- When you modify the HDFS data currently (apppend) or you rename directories
- You have a lot of partitioned writes (spark.read().write.partitionBy(...).parquet(gs://...))



### **Spark (Processing Memory, batch and streaming)**
Bounded - DataFrames
UnBounded - DStreams

Diferences between RDDs, DataFrames and Dataset

RDD's --> data without schema
Datafranes --> data with schema


**Schema-on-write**

The data structure must be created before ingest and data will be validate against this data structure.

Schema-on-write helps to execute the query faster because the data is already loaded in a strict format and you can easily find the desired data. However, this requires much more preliminary preparation and continuous transformation of incoming data, and the cost of making changes to the schema is high and should be avoided.

**Schema on-read**
The data structures are not applied or initiated before the ingested; it is created during the ETL process

Schema-on-read, on the other hand, can provide flexibility, scalability, and prevent some human mistakes. It is generally recommended that data is stored in the original raw format (just in case) and optimized in another format suitable for further data processing

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Schemas_versus_2.png")>
</p>

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Schemas_versus.png")>
</p>


### **More components Ecosystem Hadoop**

**Hudi ( Hadoop Updates, Deletes and Inserts):**  
Datalake, we use file based storage (parquet, ORC) to store data in query optimized columnar format.
Handle Updates, deletes and insert operation  
ACID properties like in case of a RDBMS.
Hudi maintains a timeline of all actions performed on the table at different points in time

Hudi supports two table types: copy-on-write and merge-on-read. The copy-on-write table type stores data using exclusively columnar file formats (e.g., Apache Parquet). Via copy-on-write, updates simply version and rewrite the files by performing a synchronous merge during write.

The merge-on-read table type stores data using a combination of columnar (e.g., Apache parquet) and row based (e.g., Apache Avro) file formats. Updates are logged to delta files and later compacted to produce new versions of columnar files synchronously or asynchronously.


**Nifi (Niagara Files)**
Designed to handle big amounts of data and automate dataflow. It’s a simple, powerful data processing and distribution system, allowing for the creation of scalable directed graphs of data routing and transformation. Data may be filtered, adjusted, joined, divided, enhanced, and verified. NiFi 

NiFi is an ETL tool typically used for long-running jobs, suitable for processing both periodic batches and streaming data.

 **Apache Ranger** 
Is a framework to enable, monitor and manage comprehensive data security across the Hadoop platform.

Apache Ranger uses two key components for authorization:

Apache Ranger policy admin server - This server allows you to define the authorization policies for Hadoop applications

Apache Ranger plugin - This plugin validates the access of a user against the authorization policies defined in the Apache Ranger policy admin server


**Apache Sqqop**
Is a tool designed for efficiently transferring bulk data between Apache Hadoop and structured datastores such as relational databases.


**Delta Lake**
It’s an open-source data format and transactional data management system, based on Parquet, that makes your data lake reliable by implementing ACID transactions on top of cloud object storage. Delta Lake tables unify batch and streaming data processing right out of the box. And finally, Delta Lake is designed to be 100% compatible with Apache Spark


### **Hive**

Hive was developed with a vision to incorporate the concepts of tables, columns just like SQL. Hive is a data warehouse system which is used for querying and analyzing large datasets stored in HDFS. Hive uses a query language call HiveQL which is similar to SQL.

**Hive Metastore**

Metastore is the central repository of Apache Hive metadata. It stores metadata for Hive tables (like their schema and location) and partitions in a relational database. It provides client access to this information by using metastore service API.

**Migration Hive Metastore**
Service in GCP to store Hive Metastore.

You must now prepare the metadata stored in your Hive metastore database for import by making a **MySQL** or **AVRO** dump file and placing it into a Cloud Storage bucket.
**note:** For best results, use Cloud Storage buckets that are located in the same region as your Dataproc Metastore service

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Hive_Metastore.png")>
</p>

``` bash
gcloud metastore services import gcs SERVICE \
--import-id=IMPORT_ID \
--location=LOCATION \
--description=DESCRIPTION \
--dump-type=DUMP_TYPE \
--database-dump=DATABASE_DUMP 
```

**_SERVICE:_** The name of the service.
**_IMPORT_ID:_** The ID of this metadata import.
**_LOCATION:_** Refers to a Google Cloud region.
**_DESCRIPTION:_** Optional: The import description. You can edit this later using gcloud metastore services imports update IMPORT
**_DUMP_TYPE:_** The type of the external database. Defaults to mysql.
**_DATABASE_DUMP:_** The path to the Cloud Storage folder for Avro or object for MySQL containing the database files. It must begin with gs://.


After you create a Dataproc Metastore service, you can attach either of the following to use the service as its Hive metastore:

* Option 1

``` bash
 gcloud dataproc clusters create CLUSTER_NAME \
--dataproc-metastore=projects/PROJECT_ID/locations/LOCATION/services/SERVICE \
--region=LOCATION
```
 
**_CLUSTER_NAME:_** with the name of the new cluster.
**_PROJECT_ID:_** with the project ID of the project you created your Dataproc Metastore service in.
**_LOCATION:_** with the same region you specified for the Dataproc Metastore service.
**_SERVICE:_** with the Dataproc Metastore service name.

* Option 2

``` bash
gcloud dataproc clusters create CLUSTER_NAME \
--properties="hive:hive.metastore.uris=$ENDPOINT_URI,hive:hive.metastore.warehouse.dir=$WAREHOUSE_DIR/hive-warehouse"
```

**_ENDPOINT_URI:_** Dataproc --> Metastore --> Configuration --> URI
**_WAREHOUSE_DIR:_** Dataproc --> Metastore --> Configuration --> Metastore config overrides --> hive.metastore.warehouse.dir


**Connect with Spark**

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Hive_Metastore.png")>
</p>



### **spark shell or spark submit**

 * spark-shell should be used for interactive queries, it needs to be run in yarn-client mode so that the machine you're running on acts as the driver.

 * spark-submit  you submit jobs to the cluster then the task runs in the cluster. Normally you would run in cluster mode so that YARN can assign the driver to a suitable node on the cluster with available resources.

 
 pyspark supports stand alone in the so called "local mode" which means the driver runs on the machine that submits the job. Only Yarn supports cluster mode for pyspark unfortuantely.


### **Data Proc (Compute and Storage separated)**

**Architecture**

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Arquitecture_DataProc.png")>
</p>



**Best Practices**


- Use GCS rather than HDFS
- DataProc and GCS must be in the same region or near for Latency purpose
- If we have more than 10K input file. We need to create files with more capacity
- Use Pereemptible VMs lower cost
- Create cluster with mix of VMS and PVMS consider evaluating the correct ratio between preemptible nodes and non-preemptible nodes, by performing job runs’ tests. Use preemptible for non-critical jobs
- Divide cluster on-premise in many cluster ephemeral.
- Create labels on clusters and jobs to find logs faster.
- Separate your development and production environments onto different clusters.



<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Arquitecture_Best_DataProc.png")>
</p>


**Benefits**


- Low cost  --> 1 c per virtual cpu per cluster per hour		

Ex: 6 clusters (1 main + 5 workers) of 4 CPUs each ran for 2 hours would cost $.48.  	
Dataproc charge = # of vCPUs * hours * Dataproc price = 24 * 2 * $0.01 = $0.48

- Fast 		--> to start, scale and shut down near 90 seconds or less on average  
- Reizable  --> Cluster can be created and scaled quickly
- Open Source --> You can use hadoop or spark, because Dataproc manages updates
- Versioning --> Allows you to switch different version of hadoop or any tool (spark, hive, pig)
- High Availability -->
- Fully managed --> You can't worry for mantaining 


**Configuration**

- Single node (1 master: 0 workers)
- Standard  (1 master: n workers)
- High Availability (3 master: n workers)	

Initialization actions --> which are executables or scripts that Cloud Dataproc will run on all nodes in the cluster as soon as it’s set up. (libraries, environments, etc...)

**Versioning**

When you create a new Dataproc cluster, the latest available Debian image version will be used by default. You can select a Debian, Rocky Linux or Ubuntu image version when creating a cluster.

Those images can contain different version of product for example:

1.5 Debian version = Hadoop 1.5 and Spark 2.4.8
2.0 Debian version = Hadoop 3.2.2 and Spark 3.2.1

With that, Dataproc contain versions of images to specific scenario.


**Cluster**


- **Cluster Monolithic|long-running**
	* Cluster involves frequent batch jobs or streaming jobs wich run 24x7
	* it's mandatory a cluster in warm conditions all the time
	* There is a need to let analysis quickly (ad hoc analytical queries)
		Note: Create a ephemeral cluster takes around 90 seconds (you can change long live to ephemeral)
- **Cluster ephemeral** (one cluster per workflow)
	* Required resources are active only when being used (On-demand).
	* You only pay for what you use. 
	* Create Cluster --> Run Cluster -->  Delete Cluster

		**Pros**
		* Can pick appropriate configuration such as machine type and GPUs on a per-job basis
		* Can use auto zone placement to find a GCE zone with capacity for job
		* Jobs are isolated from one another so do not compete for resources
		* Each job can run as a separate service account
		* Fast cluster startup time (< 90s) is negligible for jobs that take > 10m.

		**Cons**
		* This disadvantage is related to the cluster startup time, it takes around 90 seconds to spin up the cluster and for that reason, this architecture doesn’t work or wasn't designed for short jobs or interactive jobs. 

<p align="center">
<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Ephemeral.png")>
</p>
Ephemeral clusters means that you spin up a cluster when you need to run a job and then the cluster is deleted when the job is completed.


- **Pooled**
	* It works using labels (Labels are key-value pairs that can be tagged to Dataproc clusters and jobs)
	* A Set of clusters that can process a job,
	* Labels can be added to a group of clusters or a single cluster.

		**Pros**
		* This architecture provides higher utilization for shorter jobs.
		* Start time for applications such as Hive is instantaneous 
		* Cluster pools is a good use for autoscaling feature.
		* If one cluster gets into an ERROR the pool is still working because it is resilient.
		* Jobs can be labelled individually for chargeback

		**Cons**

		* Set up and manage a cluster pool requires more effort compared to Ephemeral clusters.
		* There is a consideration about auto-scaling: Cluster pools are not great for larger jobs. Jobs which are larger than graceful decommissioning time-out. in general, you want to pick a graceful timeout that’s longer than your longest job (e.g. 1h). If you have jobs that take more than 30 minutes, you should move them to their own ephemeral clusters to avoid blocking graceful decommissioning.


<p align="center">
<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Pool.png")>
</p>
We have 3 clusters. The group label is  pool-1 and is set to the three clusters. 	
Every job submitted that contains this label would run in any of these three Clusters.	 

Besides each cluster have its own label set, for example the third cluster has the cluster label set as cluster-3. So if a job is submitted with the two labels, pool-1 and cluster-3, that job will run in the third Cluster. 

**Preemptible VMs (PVMs)**

PVMs are highly affordable, **short-lived** compute instances suitable for **batch jobs and fault-tolerant workloads**. Their price is significantly lower than normal VMs but they can be taken away from clusters at any time without any notice. *Using a certain percentage of PVMs in clusters running fault tolerant workloads can reduce costs*. However, remember that using a high percentage of PVMs or using it for jobs which are not fault tolerant can result in failed jobs or other related issues.

 Prreemptible instance are used to add capacity, they are not used for data storage.


 If a PVM is beign reclaimed for GCE(Google compute engine), it will slow down, but job won't be stopped, only it will be processed in a VM "permanent"

**graceful decommissioning**
To control shutting down a worker after its jobs are completed



**Auto Scaling**

Auto scaling enables clusters to scale up or down based on YARN memory metrics. Determining the correct auto scaling policy for a cluster may require careful monitoring and tuning over a period of time.

Scaling down can be less straightforward than scaling up and can result in task reprocessing or job failures. This is because map tasks store intermediate shuffle data on the local disk. When nodes are decommissioned, shuffle data can be lost for running jobs. Some common symptoms for this are:

- MapReduce Jobs - “Failed to fetch” 
- Spark - “FetchFailedException”, “Failed to connect to


**Storage**

- **GCS**
	*	Google Cloud Storage is the preferred storage option for all **persistent storage (data)** needs. 
	*	Also GCS is a object **storage**, a object storage are more like a “key value store,” where objects are arranged in flat buckets. Object storage systems only allow atomic replacement of entire object

	* Good if:
		Your data in ORC, Parquet, Avro, or any other format will be used by different clusters or jobs, and you need data persistence if the cluster terminates.
		You need high throughput and your data is stored in files larger than 128 MB.
		You need cross-zone durability for your data.
		You need data to be highly available—for example, you want to eliminate HDFS NameNode as a single point of failure.

- **HDFS** storage on Dataproc
	*	It is built on top of persistent disks (PDs) attached to worker nodes. This means data stored on HDFS is transient with relatively higher storage costs.
	*	Zonal disks have higher read/write throughput than regional ones.
	*	PDs come in a few different types to accommodate different performance and cost considerations (Solid State Drives SSD, persisten disk). 
	*	Local SSDs can provide faster read and write times than persistent disk. 

	*	Good if:
		Your jobs require a lot of metadata operations—for example, you have thousands of partitions and directories, and each file size is relatively small.
		You modify the HDFS data frequently or you rename directories. (Cloud Storage objects are immutable, so renaming a directory is an expensive operation because it consists of copying all objects to a new key and deleting them afterwards.)
		You heavily use the append operation on HDFS files.
		You have workloads that involve heavy I/O. For example, you have a lot of partitioned writes, such as the following:
		``` python
		spark.read().write.partitionBy(...).parquet("gs://")
		```
		You have I/O workloads that are especially sensitive to latency. For example, you require single-digit millisecond latency per storage operation.

**Logging**

Your Google Cloud jobs send their logs to Cloud Logging, where the logs are easily accessible. You can get your logs in these ways:

- With a browser-based graphical interface using Logs Explorer in Google Cloud Console.
- From a local terminal window using the Google Cloud CLI.
- From scripts or applications using the Cloud Client Libraries for the Cloud Logging API.
- By calling the Cloud Logging REST API.

Aditional when send a job, we can use propertie --driver-log-levels (parameter to control the level of logging into Cloud Logging, send jobs to cluster )
- gcloud dataproc jobs submit hadoop --driver-log-levels 

In our code , we can add 
- spark.sparkContext.setLogLevel("DEBUG")  = code jobs


**Orchestation**


What is a DAG ?
The Directed Acyclic Graph (DAG) itself doesn't care about what is happening inside the tasks; it is merely concerned with how to execute them
		
<p align="center">
<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/DAG.png")>
</p>


- **Work Templates** (reusable workflow configuration, for managing and executing workflows. ) 

	* **Managed cluster**
		The workflow will **create** this **"ephemeral" cluster** to **run jobs**, and then **delete the cluster** when the workflow is finished.


		<p align="center">
		<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Work_Templates_Architecture.png")>
		</p>

		<p align="center">
		<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Work_Templates_Example.png")>
		</p>

	* **Cluster selector**
		A workflow template can specify an existing cluster on which to run workflow jobs by specifying one or more user labels that were previously applied to one or more clusters. 
		The workflow will run on a cluster that matches all of the specified labels. If multiple clusters match the label(s), 
		Dataproc will select the cluster with the most YARN available memory to run all workflow jobs. 
		At the end of workflow, the selected cluster is not deleted

- **Cloud Composer**
	 
We can use Coud composer to generate DAGs y schedule us clusters.

**_[Ephemeral:](https://github.com/BenRamo06/PySpark/blob/master/Dataproc/Scheduler/composer_ephemeral_dataproc.py)_** 
**_[Worktemplate:](https://github.com/BenRamo06/PySpark/blob/master/Dataproc/Scheduler/composer_worktemplate_dataproc.py)_** 



### **Migration to GCP**

**Move data**
Both models use Hadoop DistCp to copy data from your on-premises HDFS clusters to Cloud Storage:
- Check push model (the source cluster runs the distcp jobs on its data nodes and pushes files directly to Cloud Storage)
- Check pull model (An ephemeral Dataproc clust         er runs the distcp jobs on its data nodes, pulls files from the source cluster, and copies them to Cloud Storage)


**Move Job to GCP**
- Move data to GCS
- Create dataproc cluster to run job
- Submit job to cluster
- Monitor with cloud logging 
- Check output also in GCS
- Delete cluster after use


**Define kind of migration**

- Lift & shift migration (e.g. copy dta to GCS, Update prefix hdfs:// to gs://, Create a Cloud Dataproc cluster and run your job on the cluster against the data you copied to Cloud Storage.)
- Migration into cloud components (e.g. Dataproc with several optimizations: ephemeral jobs, long live jobs )
- Migration into most-optimized cloud services (e.g. migrate Spark into Beam with Dataflow in GCP)


**Migrate code**

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Migrate_code.png")>
</p>


<!-- 
Change hdsf:// by gsc://

File System
	it is organized jerarquie like a tree
	no immutable
Object System
	it doesn't have a jerarquie
	Immutable
	Versioning -->



experiencia en spark --> map reduce (tetxo)
API SPARK --> 
SPARK SQL -->
Experiencia (texto)
hdfs similar a gsutil



# Aditional

## Databricks

A data lakehouse is a data solution concept that combines elements of the data warehouse with those of the data lake.

A data lakehouse enables a single repository for all your data (structured, semi-structured, and unstructured) while enabling best-in-class machine learning, business intelligence, and streaming capabilities.

<p align="center">
<img width="750" src="https://github.com/BenRamo06/PySpark/blob/master/images/Data_Lakehouse.png")>
</p>


### ACID
ACID is a concept (and an acronym) that refers to the four properties of a transaction in a database system, which are: Atomicity, Consistency, Isolation and Durability.

**Atomicity**
The transaction should be completely executed or fails completely

**Consistency**
The transaction maintains data integrity constraints, leaving the data consistent and won't corrupt the database.
The data that is saved in the database must always be valid (the data will be valid according to defined rules, including any constraints, cascades, and triggers that have been applied on the database), this way the corruption of the database that can be caused by an illegal transaction is avoided.


**Isolation**
Ensure that the transaction will not be changed by any other concurrent transaction
It means that each transaction in progress will not be interfered by any other transaction until it is completed.

**Durability**
Once a transaction is completed and committed, its changes are persisted permanently in the database. This property ensures that the information that is saved in the database is immutable until another update or deletion transaction affects it.



### CAP

**Consistency**
Consistency means that the user should be able to see the same data no matter which node they connect to on the system. This data is the most recent data written to the system.

**Availability**
Availability is of importance when it is required that the client or user be able to access the data at all times, even if it is not consistent (it might not be the most recent). 

**Partition Tolerance**
Meaning if a node fails to communicate, then one of the replicas of the node should be able to retrieve the data required by the user.

Partition is mandatory in every system


**Examples AP**
* Cassandra
* DynamoDB
* Cosmos DB

**Examples CP**
* MongoDB
* Redis
* HBase