# My API Service

This repository contains the source code, Docker Compose file, and Helm charts for My API Service.

## Prerequisites

- Docker: [https://www.docker.com/get-started](https://www.docker.com/get-started)
- Kubernetes: [https://kubernetes.io/docs/setup/](https://kubernetes.io/docs/setup/)
- Helm: [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Building and Running the Service Locally with Docker Compose

Clone this repository to your local machine:


git clone https://github.com/your-username/my-api-service.git
Navigate to the project directory:



cd my-api-service
Build and run the service using Docker Compose:



docker-compose up -d
This will build the Docker image and start the service in detached mode.

Test the service by making a request:

curl http://localhost:8080/
You should receive a response from the service indicating that it is running successfully.

To stop the service, run:

docker-compose down

Deploying the Service to Kubernetes with Helm
Install the Helm chart:

helm install my-api-service ./charts/my-api-service
This will deploy the service to your Kubernetes cluster using the default configuration values specified in values.yaml.

Wait for the deployment to complete:


kubectl get pods
Ensure that the pods are running and ready.

Obtain the service IP address:


kubectl get service my-api-service
Note the IP address listed under the "EXTERNAL-IP" column. This is the address from which you can access the service.

Testing the Service
Make a request to the service:

curl http://<service-ip-address>/
Replace <service-ip-address> with the IP address obtained in the previous step.

You should receive a response from the service indicating that it is running successfully.