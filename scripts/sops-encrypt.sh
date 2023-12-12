#!/bin/bash
sops -e -i ./charts/inecuria/secrets.qa.yaml
sops -e -i ./charts/inecuria/secrets.production.yaml
