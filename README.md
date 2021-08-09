# helm-charts-tutorial
This repo is a simple helm chart tutorial that deploys a simple FastAPI app dockerized to my local k8 cluster

## FastAPI component
It is a simple endpoint that sums up 3 numbers entered into the API.

Firing up in your local machine:
```
uvicorn app.main:app --reload --debug
```

## Dockerized FastAPI component
Containerize FastAPI into a docker image, and uploads to Docker Hub.

Run the Makefile command, before running the docker image:
```
make build-push
```

Running the docker image locally:
```
docker-compose up
```

Running the docker image from Docker Hub:
```
docker run -p 5555:5555 shumingpeh/addition-model-api-test:test
```

## Helm chart
This is assumed that you have `helm` and `minikube` installed in your local machine

To install the helm chart:
```
helm install simple-addition-api charts/addition-model-api/ -n [NAMESPACE]
```

Depending on the service type set in the `values.yaml`, the way to access the endpoint will be different. If its a `ClusterIP` (which is for this instance) we have to port forward the pods to the container port:
```
export POD_NAME=$(kubectl get pods --namespace personal-projects -l "app.kubernetes.io/name=addition-model-api,app.kubernetes.io/instance=simple-addition-api" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace personal-projects $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Visit http://127.0.0.1:8080 to use your application"
kubectl --namespace personal-projects port-forward $POD_NAME 8080:$CONTAINER_PORT
```
