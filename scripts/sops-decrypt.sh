#!/bin/bash
sops -d -i ./charts/failed-imports/secrets.qa.yaml
sops -d -i ./charts/failed-imports/secrets.production.yaml
