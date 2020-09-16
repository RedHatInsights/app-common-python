# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)



class AppConfig:
    """ application deployment configuration for cloud.redhat.com applications
    """

    def __init__(self):

        #: application deployment configuration for cloud.redhat.com applications
        self.webPort = None

        #: application deployment configuration for cloud.redhat.com applications
        self.metricsPort = None

        #: application deployment configuration for cloud.redhat.com applications
        self.metricsPath = None

        #: application deployment configuration for cloud.redhat.com applications
        self.logging = None

        #: application deployment configuration for cloud.redhat.com applications
        self.kafka = None

        #: application deployment configuration for cloud.redhat.com applications
        self.database = None

        #: application deployment configuration for cloud.redhat.com applications
        self.objectStore = None

        #: application deployment configuration for cloud.redhat.com applications
        self.inMemoryDb = None

        #: application deployment configuration for cloud.redhat.com applications
        self.dependencies = None

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

        obj.inMemoryDb = InMemoryDB.dictToObject(dict.get('inMemoryDb', None))

        obj.dependencies = DependenciesConfig.dictToObject(dict.get('dependencies', None))
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
        self.pgPass = None

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

        obj.pgPass = dict.get('pgPass', None)
        return obj


class ObjectStoreConfig:
    """ object storage configuration
    """

    def __init__(self):

        #: object storage configuration
        self.accessKey = None

        #: object storage configuration
        self.secretKey = None

        #: object storage configuration
        self.endpoint = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = ObjectStoreConfig()

        obj.accessKey = dict.get('accessKey', None)

        obj.secretKey = dict.get('secretKey', None)

        obj.endpoint = dict.get('endpoint', None)
        return obj


class InMemoryDB:
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
        obj = InMemoryDB()

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.username = dict.get('username', None)

        obj.password = dict.get('password', None)
        return obj


class DependenciesConfig:
    """ Dependent service connection info
    """

    def __init__(self):
        pass

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = DependenciesConfig()
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


class DependencyConfig:
    """ Dependent service connection info
    """

    def __init__(self):

        #: Dependent service connection info
        self.name = None

        #: Dependent service connection info
        self.hostname = None

        #: Dependent service connection info
        self.port = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = DependencyConfig()

        obj.name = dict.get('name', None)

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)
        return obj


