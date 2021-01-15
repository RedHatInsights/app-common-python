# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)



class AppConfig:
    """ ClowdApp deployment configuration for Clowder enabled apps.
    """

    def __init__(self):

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.webPort = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.metricsPort = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.metricsPath = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.logging = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.kafka = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.database = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.objectStore = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.inMemoryDb = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.featureFlags = None

        #: ClowdApp deployment configuration for Clowder enabled apps.
        self.endpoints = []

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.webPort = dict.get('webPort', None)

        obj.metricsPort = dict.get('metricsPort', None)

        obj.metricsPath = dict.get('metricsPath', None)

        obj.logging = LoggingConfig.dictToObject(dict.get('logging', None))

        obj.kafka = KafkaConfig.dictToObject(dict.get('kafka', None))

        obj.database = DatabaseConfig.dictToObject(dict.get('database', None))

        obj.objectStore = ObjectStoreConfig.dictToObject(dict.get('objectStore', None))

        obj.inMemoryDb = InMemoryDBConfig.dictToObject(dict.get('inMemoryDb', None))

        obj.featureFlags = FeatureFlagsConfig.dictToObject(dict.get('featureFlags', None))

        arrayEndpoints = dict.get('endpoints', [])
        for elemEndpoints in arrayEndpoints:
            obj.endpoints.append(
                DependencyEndpoint.dictToObject(elemEndpoints))
        return obj


class LoggingConfig:
    """ Logging Configuration
    """

    def __init__(self):

        #: Logging Configuration
        self.type = None

        #: Logging Configuration
        self.cloudwatch = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = LoggingConfig()

        obj.type = dict.get('type', None)

        obj.cloudwatch = CloudWatchConfig.dictToObject(dict.get('cloudwatch', None))
        return obj


class KafkaConfig:
    """ Kafka Configuration
    """

    def __init__(self):

        #: Kafka Configuration
        self.brokers = []

        #: Kafka Configuration
        self.topics = []

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = KafkaConfig()

        arrayBrokers = dict.get('brokers', [])
        for elemBrokers in arrayBrokers:
            obj.brokers.append(
                BrokerConfig.dictToObject(elemBrokers))

        arrayTopics = dict.get('topics', [])
        for elemTopics in arrayTopics:
            obj.topics.append(
                TopicConfig.dictToObject(elemTopics))
        return obj


class DatabaseConfig:
    """ Database Configuration
    """

    def __init__(self):

        #: Database Configuration
        self.name = None

        #: Database Configuration
        self.username = None

        #: Database Configuration
        self.password = None

        #: Database Configuration
        self.hostname = None

        #: Database Configuration
        self.port = None

        #: Database Configuration
        self.adminUsername = None

        #: Database Configuration
        self.adminPassword = None

        #: Database Configuration
        self.rdsCa = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = DatabaseConfig()

        obj.name = dict.get('name', None)

        obj.username = dict.get('username', None)

        obj.password = dict.get('password', None)

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.adminUsername = dict.get('adminUsername', None)

        obj.adminPassword = dict.get('adminPassword', None)

        obj.rdsCa = dict.get('rdsCa', None)
        return obj


class ObjectStoreConfig:
    """ Object Storage Configuration
    """

    def __init__(self):

        #: Object Storage Configuration
        self.buckets = []

        #: Object Storage Configuration
        self.accessKey = None

        #: Object Storage Configuration
        self.secretKey = None

        #: Object Storage Configuration
        self.hostname = None

        #: Object Storage Configuration
        self.port = None

        #: Object Storage Configuration
        self.tls = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ObjectStoreConfig()

        arrayBuckets = dict.get('buckets', [])
        for elemBuckets in arrayBuckets:
            obj.buckets.append(
                ObjectStoreBucket.dictToObject(elemBuckets))

        obj.accessKey = dict.get('accessKey', None)

        obj.secretKey = dict.get('secretKey', None)

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.tls = dict.get('tls', None)
        return obj


class InMemoryDBConfig:
    """ In Memory DB Configuration
    """

    def __init__(self):

        #: In Memory DB Configuration
        self.hostname = None

        #: In Memory DB Configuration
        self.port = None

        #: In Memory DB Configuration
        self.username = None

        #: In Memory DB Configuration
        self.password = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = InMemoryDBConfig()

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.username = dict.get('username', None)

        obj.password = dict.get('password', None)
        return obj


class FeatureFlagsConfig:
    """ Feature Flags Configuration
    """

    def __init__(self):

        #: Feature Flags Configuration
        self.hostname = None

        #: Feature Flags Configuration
        self.port = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = FeatureFlagsConfig()

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)
        return obj


class DependencyEndpoint:
    """ Dependent service connection info
    """

    def __init__(self):

        #: Dependent service connection info
        self.name = None

        #: Dependent service connection info
        self.hostname = None

        #: Dependent service connection info
        self.port = None

        #: Dependent service connection info
        self.app = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = DependencyEndpoint()

        obj.name = dict.get('name', None)

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.app = dict.get('app', None)
        return obj


class CloudWatchConfig:
    """ Cloud Watch configuration
    """

    def __init__(self):

        #: Cloud Watch configuration
        self.accessKeyId = None

        #: Cloud Watch configuration
        self.secretAccessKey = None

        #: Cloud Watch configuration
        self.region = None

        #: Cloud Watch configuration
        self.logGroup = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = CloudWatchConfig()

        obj.accessKeyId = dict.get('accessKeyId', None)

        obj.secretAccessKey = dict.get('secretAccessKey', None)

        obj.region = dict.get('region', None)

        obj.logGroup = dict.get('logGroup', None)
        return obj


class BrokerConfig:
    """ Broker Configuration
    """

    def __init__(self):

        #: Broker Configuration
        self.hostname = None

        #: Broker Configuration
        self.port = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = BrokerConfig()

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)
        return obj


class TopicConfig:
    """ Topic Configuration
    """

    def __init__(self):

        #: Topic Configuration
        self.requestedName = None

        #: Topic Configuration
        self.name = None

        #: Topic Configuration
        self.consumerGroup = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = TopicConfig()

        obj.requestedName = dict.get('requestedName', None)

        obj.name = dict.get('name', None)

        obj.consumerGroup = dict.get('consumerGroup', None)
        return obj


class ObjectStoreBucket:
    """ Object Storage Bucket
    """

    def __init__(self):

        #: Object Storage Bucket
        self.accessKey = None

        #: Object Storage Bucket
        self.secretKey = None

        #: Object Storage Bucket
        self.requestedName = None

        #: Object Storage Bucket
        self.name = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ObjectStoreBucket()

        obj.accessKey = dict.get('accessKey', None)

        obj.secretKey = dict.get('secretKey', None)

        obj.requestedName = dict.get('requestedName', None)

        obj.name = dict.get('name', None)
        return obj


