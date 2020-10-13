import json
import os
from typing import List, Optional
from .types import AppConfig


def loadConfig(filename):
    with open(filename) as f:
        data = json.load(f)
    return AppConfig.dictToObject(data)

LoadedConfig = loadConfig(os.environ.get("ACG_CONFIG"))

KafkaTopics = {}
if LoadedConfig.kafka and len(LoadedConfig.kafka.topics) > 0:
	for topic in LoadedConfig.kafka.topics:
		KafkaTopics[topic.requestedName] = topic

ObjectBuckets = {}
if LoadedConfig.objectStore and len(LoadedConfig.objectStore.buckets) > 0:
	for bucket in LoadedConfig.objectStore.buckets:
		ObjectBuckets[bucket.requestedName] = bucket

DependencyEndpoints = {}
if LoadedConfig.endpoints and len(LoadedConfig.endpoints) > 0:
    for endpoint in LoadedConfig.endpoints:
        if endpoint.app not in DependencyEndpoints:
            DependencyEndpoints[endpoint.app] = {}
        DependencyEndpoints[endpoint.app][endpoint.name] = endpoint
