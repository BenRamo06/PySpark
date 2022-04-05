----> Run workflow using yaml file

gcloud dataproc workflow-templates instantiate-from-file \
--file=your-template.yaml \
--region=us-central1


----> Export a workflow to YAML

gcloud dataproc workflow-templates export my-workflow \
--destination=template.yaml \
--region=us-central1


----> Import a YAML to workflow

gcloud dataproc workflow-templates import my-workflow \
--source=template2.yaml \
--region=us-central1


---> We read WorkTamplate/template2.yaml with parameters ----


gcloud dataproc workflow-templates instantiate my-workflow \
--region=us-central1 \
--parameters=NUMBER=25,CLUSTER=test1