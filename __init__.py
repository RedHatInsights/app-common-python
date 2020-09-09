from pydantic import BaseModel
import json
import os
from typing import List, Optional

class CloudWatchConfig(BaseModel):
    accessKeyID:     str
    secretAccessKey: str
    region:          str
    logGroup:        str

class LoggingConfig(BaseModel):
    type:       str
    cloudWatch: Optional[CloudWatchConfig]

class BrokerConfig(BaseModel):
	hostname: str
	port:     int

class TopicConfig(BaseModel):
	name:              str
	consumerGroupName: str

class KafkaConfig(BaseModel):
	brokers: List[BrokerConfig]
	topics:  List[TopicConfig]

class ObjectStoreConfig(BaseModel):
	accessKey: str
	secretKey: str
	endpoint:  str

class DatabaseConfig(BaseModel):
	name:     str
	username:     str
	password:     str
	hostname: str
	port:     int
	pgPass:   str

class AppConfig(BaseModel):
	webPort:     int
	metricsPort: int
	metricsPath: str
	logging:     LoggingConfig
	kafka:       KafkaConfig
	database:    DatabaseConfig
	objectStore: ObjectStoreConfig

def loadConfig(filename):
    with open(filename) as f:
        data = json.load(f)
    return AppConfig(**data)

LoadedConfig = loadConfig(os.environ.get("ACG_CONFIG"))