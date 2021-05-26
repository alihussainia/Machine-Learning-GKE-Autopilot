# Creating GKE-Autopilot Cluster

In the task-3, we are going to follow these steps:

1. Set the CLUSTER_NAME environment variable using:
```bash
export CLUSTER_NAME=ml-gke-cluster
```
2. Create a `3 node` Kubernetes cluster on GKE using:
```bash
gcloud container clusters create-auto $CLUSTER_NAME \
    --region us-west1 \
    --project=$PROJECT_ID
```
3. Connect to the cluster using:
```bash
gcloud container clusters get-credentials $CLUSTER_NAME \
    --region us-west1 \
    --project=$PROJECT_ID
```
Reference: https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster
