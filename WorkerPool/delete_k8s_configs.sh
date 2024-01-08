#!/bin/bash

echo "Deleting Kubernetes resources..."

kubectl delete -f "consumer-deployment.yaml"
kubectl delete -f "producer-deployment.yaml"
kubectl delete -f "rabbitmq-service.yaml"
kubectl delete -f "rabbitmq-deployment.yaml"
kubectl delete -f "persistent-volume-claim.yaml"
kubectl delete -f "persistent-volume.yaml"

echo "All resources have been deleted successfully."