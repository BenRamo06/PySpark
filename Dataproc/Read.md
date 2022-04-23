# HADDOP - SPARK - DATAPROC

What is a cluster
	Cluster is a group of interconnected computers (know as nodes) thant can work together on the same problem.






### **Hadoop (Processing Disk, batch, Compute and Storage together, Master/Slave Architecture)**

#### **Storage --> HDFS (Hadoop Distruibed File System)**
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


### **Data Proc (Compute and Storage separated)**



**Best Practices**


- Use GCS rather than HDFS
- DataProc and GCS must be in the same region or near for Latency purpose
- If we have more than 10K input file. We need to create files with more capacity
- Use Pereemptible VMs lower cost
- Create cluster with mix of VMS and PVMS consider evaluating the correct ratio between preemptible nodes and non-preemptible nodes, by performing job runs’ tests. Use preemptible for non-critical jobs
- Divide cluster on-premise in many cluster ephemeral
- Create labels on clusters and jobs to find logs faster

**Benefits**


- Low cost  --> 1 c per virtual cpu per cluster per hour
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

Initialization actions --> install additional components of the cluster. (libraries, environments, etc...)

**Cluster**


- Cluster long live
	* Cluster involves frequent batch jobs or streaming jobs wich run 24x7
	* ad hoc analytical queries?
- Cluster ephemeral
	* Required resources are active only when being used. You only pay for what you use. 
	* Create Cluster --> Run Cluster -->  Delete Cluster

**Logging**


- gcloud dataproc jobs submit hadoop --driver-log-levels 
- spark.sparkContext.setLogLevel("DEBUG")


**Orchestation**


What is a DAG? (images/Work_Templates_Architecture.png, images/Work_Templates_Example.png)

<p align="left">
  <img width="340" src="https://github.com/BenRamo06/PySpark/blob/master/images/Work_Templates_Architecture.png")>
</p>

<p align="right">
  <img width="340" src="https://github.com/BenRamo06/PySpark/blob/master/images/Work_Templates_Example.png")>
</p>

- Work Templates (reusable workflow configuration, for managing and executing workflows. ) 

	* Managed cluster
		The workflow will create this "ephemeral" cluster to run workflow jobs, and then delete the cluster when the workflow is finished.

	* Cluster selector
		A workflow template can specify an existing cluster on which to run workflow jobs by specifying one or more user labels that were previously applied to one or more clusters. 
		The workflow will run on a cluster that matches all of the specified labels. If multiple clusters match the label(s), 
		Dataproc will select the cluster with the most YARN available memory to run all workflow jobs. 
		At the end of workflow, the selected cluster is not deleted

- Cloud Composer

	 












### **Migration to GCP**

**Move data (two options)**
- Check push model (using distcp in the on-prem to push to GCS)
- Check pull model (using distcp in the cloud (Dataproc) to pull files from on-prem)


**Move Job to GCP**
- Move data to GCS
- Create dataproc cluster to run job
- Submit job to cluster
- Monitor with cloud logging 
- Check output also in GCS
- Delete cluster after use


**Define kind of migration**

- Lift & shift migration (maintain hadoop cluster with some VMs)
- Migration into cloud components (e.g. Dataproc with several optimizations)
- Migration into most-optimized cloud services (e.g. migrate Spark into Beam with Dataflow in GCP)


<!-- 
Change hdsf:// by gsc://

File System
	it is organized jerarquie like a tree
	no immutable
Object System
	it doesn't have a jerarquie
	Immutable
	Versioning


serverless
metastore?
preemtable / on demand.
spark shell   spark submit
spark 
productos
apache hudi  vs  delta lake
ranger (similar IAM) 
-->
