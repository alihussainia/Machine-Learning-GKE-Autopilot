# Creating Deployment and Service
In task-7, we are going to follow these steps:

1. Deploy the `deployment.yaml` manifest file using:
```bash
kubectl create -f $WORKING_DIR/task-7/deployment.yaml
```
2. Watch the deployment status using:
```bash
kubectl get pod --watch
```
4. Deploy the `service.yaml` manifest file using:
```bash
kubectl create -f $WORKING_DIR/task-7/service.yaml
```
