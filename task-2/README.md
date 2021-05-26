# Setting-up Environment:

In this task-2, we are going to set up a working environment for our project using the following steps:

1. Enable the `Google Kubernetes Engine (GKE) API` using:
```bash
gcloud services enable container.googleapis.com
```
2. Set the default `region/zone` using:
```bash
gcloud config set compute/region us-west1
gcloud config set compute/zone us-west1-a 
```
3. Set the `PROJECT_ID` environment variable using:
```bash
export PROJECT_ID=ml-gke-01
```
4. Clone the `GitHub repository` using:
```bash
git clone https://github.com/alihussainia/Machine-Learning-GKE-Autopilot.git
```
5. Change to the `Machine-Learning-GKE-Autopilot` directory using:
```bash
cd Machine-Learning-GKE-Autopilot
```
6. Set the `WORKING_DIR` environment variable using:
```bash
export WORKING_DIR=$(pwd)
```
