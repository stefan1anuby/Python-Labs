# Master-Worker Web Scraper

## Project Overview

This is a aplication that elegantly orchestrates the distribution and execution of web scraping tasks using a Master-Worker paradigm, fully encapsulated within Docker containers and orchestrated by Kubernetes. It showcases the seamless integration of Docker and Kubernetes in managing distributed tasks, specifically focusing on dynamic web page downloads.

## Key Features

* Distributed Task Management: Utilizes a Master-Worker model developed in Python to distribute web scraping tasks via RabbitMQ.
* Dockerized Environment: Each component of the application (Master, Worker, RabbitMQ) is containerized for easy deployment and scalability.
* Kubernetes Orchestration: Ready-to-deploy Kubernetes configurations to manage the application in a cloud-native environment.

## Installation and setup

#### 1.Clone the Repository:
```
git clone https://github.com/stefan1anuby/Python-Labs.git
cd WorkerPool
```
#### 2.Build Docker Images:
```
docker build -t py-consumer-image ./Consumer
docker build -t py-producer-image ./Producer
```
#### 3.Run the Containers or Deploy on Kubernetes:

```
kubectl apply -f "persistent-volume.yaml"
kubectl apply -f "persistent-volume-claim.yaml"
kubectl apply -f "rabbitmq-deployment.yaml"
kubectl apply -f "rabbitmq-service.yaml"
kubectl apply -f "producer-deployment.yaml"
kubectl apply -f "consumer-deployment.yaml"
```

#### 4.Cleaning up:
```
kubectl delete -f "consumer-deployment.yaml"
kubectl delete -f "producer-deployment.yaml"
kubectl delete -f "rabbitmq-service.yaml"
kubectl delete -f "rabbitmq-deployment.yaml"
kubectl delete -f "persistent-volume-claim.yaml"
kubectl delete -f "persistent-volume.yaml"
```

## License
This project is released under the MIT License.
