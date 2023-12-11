#!/bin/bash
# Replaces the string "REPLACE_IMAGE_TAG" in the Helm charts
IMAGE_TAG=$1
echo "Replacing image tag with \"${IMAGE_TAG}\""
sed -i "s/REPLACE_IMAGE_TAG/${IMAGE_TAG}/g" charts/failed-imports/Chart.yaml
