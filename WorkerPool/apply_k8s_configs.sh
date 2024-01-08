#!/bin/bash

echo "Aplying Kubernetes resources..."

kubectl apply -f "persistent-volume.yaml"
kubectl apply -f "persistent-volume-claim.yaml"
kubectl apply -f "rabbitmq-deployment.yaml"
kubectl apply -f "rabbitmq-service.yaml"
kubectl apply -f "producer-deployment.yaml"
kubectl apply -f "consumer-deployment.yaml"

echo "All resources have been applied successfully."