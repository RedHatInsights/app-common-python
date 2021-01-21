import json
import os
import tempfile
from typing import List, Optional
from .types import AppConfig, DependencyEndpointTypeEnum


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
_dep_endpoints_map = {}
if LoadedConfig.endpoints and len(LoadedConfig.endpoints) > 0:
    for endpoint in LoadedConfig.endpoints:
        write_endpoint = False
        if hasattr(endpoint, "type") and endpoint.type == DependencyEndpointTypeEnum.PUBLIC:
            write_endpoint = True
        elif hasattr(endpoint, "type") and endpoint.type == None:
            write_endpoint = True
        elif not hasattr(endpoint, "type"):
            write_endpoint = True
        if write_endpoint:
            if endpoint.app not in DependencyEndpoints:
                DependencyEndpoints[endpoint.app] = {}
            DependencyEndpoints[endpoint.app][endpoint.name] = endpoint

        if endpoint.app not in _dep_endpoints_map:
            _dep_endpoints_map[endpoint.app] = {}
        if endpoint.name not in _dep_endpoints_map[endpoint.app]:
            _dep_endpoints_map[endpoint.app][endpoint.name] = {}
        if hasattr(endpoint, "type") and endpoint.type != None:
            if endpoint.type not in _dep_endpoints_map[endpoint.app][endpoint.name]:
                _dep_endpoints_map[endpoint.app][endpoint.name][endpoint.type.valueAsString(endpoint.type)] = endpoint
        elif hasattr(endpoint, "type"):
            endpoint.type=DependencyEndpointTypeEnum.PUBLIC
            _dep_endpoints_map[endpoint.app][endpoint.name][endpoint.type.valueAsString(endpoint.type)] = endpoint

KafkaServers = []
if LoadedConfig.kafka and len(LoadedConfig.kafka.brokers) > 0:
    for broker in LoadedConfig.kafka.brokers:
        KafkaServers.append("{}:{}".format(broker.hostname, broker.port))

def get_dependency_endpoint(app_name, service_name, itype):
    try:
        return _dep_endpoints_map[app_name][service_name][itype]
    except KeyError:
        raise "Endpoint doesn't exist in config"
