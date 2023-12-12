#!/bin/bash
sops -d -i ./charts/inecuria/secrets.qa.yaml
sops -d -i ./charts/inecuria/secrets.production.yaml
