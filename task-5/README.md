# Creating GKE-Autopilot Cluster

In the task-3, we are going to follow these steps:

1. Set the `PROJECT_ID` environment variable using:
```bash
export PROJECT_ID=<enter-your-project-id>
```
2. Set the `CLUSTER_NAME` environment variable using:
```bash
export CLUSTER_NAME=ml-gke-cluster
```
3. Create a `Kubernetes cluster` on GKE-Autopilot using:
```bash
gcloud container clusters create-auto $CLUSTER_NAME \
    --region us-west1 \
    --project=$PROJECT_ID
```
4. Connect to the `ml-gke-cluster` cluster using:
```bash
gcloud container clusters get-credentials $CLUSTER_NAME \
    --region us-west1 \
    --project=$PROJECT_ID
```
Reference: https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster
