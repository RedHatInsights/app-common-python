#!/bin/bash
cd pkg/api/v1
wget https://raw.githubusercontent.com/RedHatInsights/clowder/master/controllers/cloud.redhat.com/config/schema.json -O schema.json
podman run -v `pwd`:/resources:Z --rm -t okieoth/yacg:latest --models /resources/schema.json --singleFileTemplates pythonBeans=/resources/app_common_python/types.py
