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
if LoadedConfig.kafka != None and len(LoadedConfig.kafka.topics) > 0:
	for topic in LoadedConfig.kafka.topics:
		KafkaTopics[topic.requestedName] = topic