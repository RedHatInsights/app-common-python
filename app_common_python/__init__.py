import json
import os
import tempfile
from typing import List, Optional
from .types import AppConfig

class KafkaBrokersClass():

    _items = None

    def __init__(self, info):
        self._items = []
        for broker in info:
            self._items.append(KafkaBroker(broker))

    def __getitem__(self, i):
        return self._items[i]

class KafkaBroker():
    def __init__(self, info):
        for k, v in info.__dict__.items():
            setattr(self, k, v)

    @property
    def kafka_ca(self):
        if not hasattr(self, "_kafka_ca"):
            if self.cacert:
                with tempfile.NamedTemporaryFile(delete=False) as tf:
                    self._kafka_ca = tf.name
                    tf.write(self.cacert.encode("utf-8"))
            else:
                return None
        return self._kafka_ca

    @property
    def broker_url(self):
        return "{}:{}".format(broker.hostname, broker.port)

class SmartAppConfig(AppConfig):

    def rds_ca(self):
        if not hasattr(self, "_rds_ca"):
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                self._rds_ca = tf.name
                tf.write(self.database.rdsCa.encode("utf-8"))

        return self._rds_ca

def isClowderEnabled ():
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

KafkaBrokers = None
if LoadedConfig.kafka and len(LoadedConfig.kafka.brokers) > 0:
    KafkaBrokers = KafkaBrokersClass(LoadedConfig.kafka.brokers)
    # for broker in LoadedConfig.kafka.brokers:
    #     KafkaBrokers.append(KafkaBroker(broker))
