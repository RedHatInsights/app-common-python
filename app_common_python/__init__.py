import json
import os
import tempfile
from .types import AppConfig


class SmartAppConfig(AppConfig):
    def rds_ca(self):
        if not hasattr(self, "_rds_ca"):
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                self._rds_ca = tf.name
                tf.write(self.database.rdsCa.encode("utf-8"))

        return self._rds_ca


def isClowderEnabled():
    return bool(os.environ.get("ACG_CONFIG", False))


def loadConfig(filename):
    if not filename:
        data = {}
    else:
        with open(filename) as f:
            data = json.load(f)
    return SmartAppConfig.dictToObject(data)


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

PrivateDependencyEndpoints = {}
if LoadedConfig.privateEndpoints and len(LoadedConfig.privateEndpoints) > 0:
    for endpoint in LoadedConfig.privateEndpoints:
        if endpoint.app not in PrivateDependencyEndpoints:
            PrivateDependencyEndpoints[endpoint.app] = {}
        PrivateDependencyEndpoints[endpoint.app][endpoint.name] = endpoint

KafkaServers = []
if LoadedConfig.kafka and len(LoadedConfig.kafka.brokers) > 0:
    for broker in LoadedConfig.kafka.brokers:
        KafkaServers.append("{}:{}".format(broker.hostname, broker.port))
