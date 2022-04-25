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

Initialization actions --> install additional components of the cluster. (libraries, environments, etc...)

**Cluster**


- Cluster long live
	* Cluster involves frequent batch jobs or streaming jobs wich run 24x7
	* it's mandatory a cluster in warm conditions all the time
	* There is a need to let analysis quickly (ad hoc analytical queries)
		Note: Create a ephemeral cluster takes around 90 seconds (you can change long live to ephemeral)
- Cluster ephemeral (one cluster per workflow)
	* Required resources are active only when being used (On-demand).
	* You only pay for what you use. 
	* Create Cluster --> Run Cluster -->  Delete Cluster

		Pros
		* Can pick appropriate configuration such as machine type and GPUs on a per-job basis
		* Can use auto zone placement to find a GCE zone with capacity for job
		* Jobs are isolated from one another so do not compete for resources
		* Each job can run as a separate service account
		* Fast cluster startup time (< 90s) is negligible for jobs that take > 10m.

		Cons
		* This disadvantage is related to the cluster startup time, it takes around 90 seconds to spin up the cluster and for that reason, this architecture doesn’t work or wasn't designed for short jobs or interactive jobs. 

<p align="center">
<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Ephemeral.png")>
</p>
Ephemeral clusters means that you spin up a cluster when you need to run a job and then the cluster is deleted when the job is completed.


- Pooled
	* It works using labels (Labels are key-value pairs that can be tagged to Dataproc clusters and jobs)
	* A Set of clusters that can process a job,
	* Labels can be added to a group of clusters or a single cluster.

		Pros
		* This architecture provides higher utilization for shorter jobs.
		* Start time for applications such as Hive is instantaneous 
		* Cluster pools is a good use for autoscaling feature.
		* If one cluster gets into an ERROR the pool is still working because it is resilient.
		* Jobs can be labelled individually for chargeback

		Cons

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



**Auto Scaling**

Auto scaling enables clusters to scale up or down based on YARN memory metrics. Determining the correct auto scaling policy for a cluster may require careful monitoring and tuning over a period of time.

Scaling down can be less straightforward than scaling up and can result in task reprocessing or job failures. This is because map tasks store intermediate shuffle data on the local disk. When nodes are decommissioned, shuffle data can be lost for running jobs. Some common symptoms for this are:

- MapReduce Jobs - “Failed to fetch” 
- Spark - “FetchFailedException”, “Failed to connect to


**Storage**

- GCS
	*	Google Cloud Storage is the preferred storage option for all **persistent storage (data)** needs. 
	*	Also GCS is a object **storage**, a object storage are more like a “key value store,” where objects are arranged in flat buckets. Object storage systems only allow atomic replacement of entire object

- HDFS storage on Dataproc
	*	It is built on top of persistent disks (PDs) attached to worker nodes. This means data stored on HDFS is transient with relatively higher storage costs.
	*	Zonal disks have higher read/write throughput than regional ones.
	*	PDs come in a few different types to accommodate different performance and cost considerations (Solid State Drives SSD, persisten disk). 
	*	Local SSDs can provide faster read and write times than persistent disk. 

**Logging**


- gcloud dataproc jobs submit hadoop --driver-log-levels  = parameter to control the level of logging into Cloud Logging, send jobs to cluster 
- spark.sparkContext.setLogLevel("DEBUG")  = code jobs


**Orchestation**


What is a DAG ?
The Directed Acyclic Graph (DAG) itself doesn't care about what is happening inside the tasks; it is merely concerned with how to execute them
		
<p align="center">
<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/DAG.png")>
</p>


- Work Templates (reusable workflow configuration, for managing and executing workflows. ) 

	* Managed cluster
		The workflow will create this "ephemeral" cluster to run workflow jobs, and then delete the cluster when the workflow is finished.


		<p align="center">
		<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Work_Templates_Architecture.png")>
		</p>

		<p align="center">
		<img width="440" src="https://github.com/BenRamo06/PySpark/blob/master/images/Work_Templates_Example.png")>
		</p>

	* Cluster selector
		A workflow template can specify an existing cluster on which to run workflow jobs by specifying one or more user labels that were previously applied to one or more clusters. 
		The workflow will run on a cluster that matches all of the specified labels. If multiple clusters match the label(s), 
		Dataproc will select the cluster with the most YARN available memory to run all workflow jobs. 
		At the end of workflow, the selected cluster is not deleted

- Cloud Composer

	 
		We can use Coud composer to generate DAGs y schedule us clusters.




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
