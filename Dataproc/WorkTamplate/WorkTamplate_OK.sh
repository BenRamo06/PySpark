
gcloud dataproc workflow-templates create my-workflow \
--region us-central1 \
--project qwiklabs-gcp-00-57719af056b2



gcloud dataproc workflow-templates set-managed-cluster my-workflow \
--region us-central1 \
--zone us-central1-a \
--master-machine-type n1-standard-2 \
--worker-machine-type n1-standard-2 \
--num-masters 1 \
--num-workers 2 \
--master-boot-disk-size 500 \
--worker-boot-disk-size 500 \
--image-version 2.0-debian10 \
--cluster-name cluster-template



gcloud dataproc workflow-templates add-job pyspark \
--region us-central1 \
--step-id step1_PI \
--workflow-template my-workflow \
gs://qwiklabs-gcp-00-57719af056b2/PI.py -- 20


gcloud dataproc workflow-templates add-job pyspark \
--region us-central1 \
--step-id step2_DF \
--start-after step1_PI \
--workflow-template my-workflow  \
gs://qwiklabs-gcp-00-57719af056b2/DF.py



gcloud dataproc workflow-templates instantiate my-workflow \
--region us-central1