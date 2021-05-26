# Testing the Web Application
In task-8, we will follow these steps:

1. Find the `external ip` using:
```bash
kubectl get svc --watch
```
2. Open a new tab in the browser and visit:
```bash
http://<external-ip-address>
```
3. Upload sample images of dogs and test the application using:
- Lhasa Dog:
```url
http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02098413-Lhasa/n02098413_11048.jpg
```
- Samoyed Dog:
```url
http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02111889-Samoyed/n02111889_11729.jpg
```
Note: Replace external-ip-address with the external-ip found in the step 1.
