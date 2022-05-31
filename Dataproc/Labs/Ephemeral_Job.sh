gcloud dataproc clusters create my-workflow \
--region us-central1 \
--zone us-central1-a \
--master-machine-type n1-standard-2 \
--worker-machine-type n1-standard-2 \
--num-masters 1 \
--num-workers 2 \
--master-boot-disk-size 500 \
--worker-boot-disk-size 500 \
--image-version 2.0-debian10


gcloud dataproc jobs submit pyspark \
--cluster=my-workflow \
--region=us-central1 \
gs://misarchivos/Jobs/logs.py

--jars gs://misarchivos/spark-lib/spark-2.4-bigquery-0.24.2-preview.jar \
--driver-log-levels \

gcloud dataproc clusters delete my-workflow \
--region us-central1