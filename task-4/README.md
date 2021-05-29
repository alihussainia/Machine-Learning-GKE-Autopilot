# Creating `Docker-Image` in Google Container Registry
In task-5, we are going to follow these steps:

1. Change directory to task-4 using:
```bash
cd task-4/
```
2. Move Dockerfile to task-4 directory using:
```bash
mv ../task-5/Dockerfile .
```
3. Build the project's docker image using:
```bash
gcloud builds submit --tag gcr.io/ml-gke-project/dogimgclassifier .
```
4. Change back the directory to main using:
```bash
cd ../
```
