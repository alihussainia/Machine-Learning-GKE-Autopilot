# Creating `Docker-Image` in Google Container Registry
In task-4, we are going to follow these steps:

1. Change directory to task-3 using:
```bash
cd task-3/
```
2. Move Dockerfile to task-3 directory using:
```bash
mv ../task-4/Dockerfile .
```
3. Build the project's docker image using:
```bash
gcloud builds submit --tag gcr.io/ml-gke-project/dogimgclassifier .
```
4. Change back the directory to main using:
```bash
cd ../
```
