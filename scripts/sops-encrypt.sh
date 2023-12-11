#!/bin/bash
sops -e -i ./charts/failed-imports/secrets.qa.yaml
sops -e -i ./charts/failed-imports/secrets.production.yaml
