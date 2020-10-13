# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)



class AppConfig:
    """ clowdapp deployment configuration for cloud.redhat.com clowdapps
    """

    def __init__(self):

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.webPort = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.metricsPort = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.metricsPath = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.logging = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.kafka = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.database = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.objectStore = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.inMemoryDb = None

        #: clowdapp deployment configuration for cloud.redhat.com clowdapps
        self.endpoints = []

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = AppConfig()

        obj.webPort = dict.get('webPort', None)

        obj.metricsPort = dict.get('metricsPort', None)

        obj.metricsPath = dict.get('metricsPath', None)

        obj.logging = LoggingConfig.dictToObject(dict.get('logging', None))

        obj.kafka = KafkaConfig.dictToObject(dict.get('kafka', None))

        obj.database = DatabaseConfig.dictToObject(dict.get('database', None))

        obj.objectStore = ObjectStoreConfig.dictToObject(dict.get('objectStore', None))

        obj.inMemoryDb = InMemoryDBConfig.dictToObject(dict.get('inMemoryDb', None))

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
    """ kafka configuration
    """

    def __init__(self):

        #: kafka configuration
        self.brokers = []

        #: kafka configuration
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
    """ database configuration
    """

    def __init__(self):

        #: database configuration
        self.name = None

        #: database configuration
        self.username = None

        #: database configuration
        self.password = None

        #: database configuration
        self.hostname = None

        #: database configuration
        self.port = None

        #: database configuration
        self.adminUsername = None

        #: database configuration
        self.adminPassword = None

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
        return obj


class ObjectStoreConfig:
    """ object storage configuration
    """

    def __init__(self):

        #: object storage configuration
        self.buckets = []

        #: object storage configuration
        self.accessKey = None

        #: object storage configuration
        self.secretKey = None

        #: object storage configuration
        self.hostname = None

        #: object storage configuration
        self.port = None

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
        return obj


class InMemoryDBConfig:
    """ In Memory DB configuration
    """

    def __init__(self):

        #: In Memory DB configuration
        self.hostname = None

        #: In Memory DB configuration
        self.port = None

        #: In Memory DB configuration
        self.username = None

        #: In Memory DB configuration
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
    """ broker configuration
    """

    def __init__(self):

        #: broker configuration
        self.hostname = None

        #: broker configuration
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
    """ topic configuration
    """

    def __init__(self):

        #: topic configuration
        self.requestedName = None

        #: topic configuration
        self.name = None

        #: topic configuration
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
    """ object storage bucket
    """

    def __init__(self):

        #: object storage bucket
        self.accessKey = None

        #: object storage bucket
        self.secretKey = None

        #: object storage bucket
        self.requestedName = None

        #: object storage bucket
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


