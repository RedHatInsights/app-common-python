import json
import os
import tempfile
from .types import AppConfig

KafkaTopics = {}
ObjectBuckets = {}
DependencyEndpoints = {}
PrivateDependencyEndpoints = {}
KafkaServers = []



class SmartAppConfig(AppConfig):

    def rds_ca(self):
        if not hasattr(self, "_rds_ca"):
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                self._rds_ca = tf.name
                tf.write(self.database.rdsCa.encode("utf-8"))

        return self._rds_ca


def isClowderEnabled ():    # noqa
    return bool(os.environ.get("ACG_CONFIG", False))


def loadConfig(filename=None, data=None):   # noqa
    if data is None:
        data = {}
    if filename:
        with open(filename) as f:
            data = json.load(f)
    return SmartAppConfig.dictToObject(data)


def load(config):
    if config.kafka and len(config.kafka.topics) > 0:
        for topic in config.kafka.topics:
            KafkaTopics[topic.requestedName] = topic

    if config.objectStore and len(config.objectStore.buckets) > 0:
        for bucket in config.objectStore.buckets:
            ObjectBuckets[bucket.requestedName] = bucket

    if config.endpoints and len(config.endpoints) > 0:
        for endpoint in config.endpoints:
            if endpoint.app not in DependencyEndpoints:
                DependencyEndpoints[endpoint.app] = {}
            DependencyEndpoints[endpoint.app][endpoint.name] = endpoint

    if config.privateEndpoints and len(config.privateEndpoints) > 0:
        for endpoint in config.privateEndpoints:
            if endpoint.app not in PrivateDependencyEndpoints:
                PrivateDependencyEndpoints[endpoint.app] = {}
            PrivateDependencyEndpoints[endpoint.app][endpoint.name] = endpoint

    if config.kafka and len(config.kafka.brokers) > 0:
        for broker in config.kafka.brokers:
            KafkaServers.append("{}:{}".format(broker.hostname, broker.port))


# default conf from env and load it
LoadedConfig = loadConfig(os.environ.get("ACG_CONFIG"))
load(LoadedConfig)
