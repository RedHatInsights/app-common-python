# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)

from enum import Enum


class AppConfig:
    """ ClowdApp deployment configuration for Clowder enabled apps.
    """

    def __init__(self, config):
        if config is None:
            return None

        self.privatePort = config.get('privatePort', None)

        self.publicPort = config.get('publicPort', None)

        self.webPort = config.get('webPort', None)

        self.metricsPort = config.get('metricsPort', None)

        self.metricsPath = config.get('metricsPath', None)

        self.logging = LoggingConfig.dictToObject(config.get('logging', None))

        self.metadata = AppMetadata.dictToObject(config.get('metadata', None))

        self.kafka = KafkaConfig.dictToObject(config.get('kafka', None))

        self.database = DatabaseConfig.dictToObject(config.get('database', None))

        self.objectStore = ObjectStoreConfig.dictToObject(config.get('objectStore', None))

        self.inMemoryDb = InMemoryDBConfig.dictToObject(config.get('inMemoryDb', None))

        self.featureFlags = FeatureFlagsConfig.dictToObject(config.get('featureFlags', None))

        self.endpoints = [
            DependencyEndpoint.dictToObject(elemEndpoints)
            for elemEndpoints in config.get('endpoints', [])
        ]


        self.privateEndpoints = [
            PrivateDependencyEndpoint.dictToObject(elemPrivateEndpoints)
            for elemPrivateEndpoints in config.get('privateEndpoints', [])
        ]


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
        obj = cls()

        obj.type = dict.get('type', None)

        obj.cloudwatch = CloudWatchConfig.dictToObject(dict.get('cloudwatch', None))
        return obj


class AppMetadata:
    """ Arbitrary metadata pertaining to the application application
    """

    def __init__(self):

        #: Arbitrary metadata pertaining to the application application
        self.deployments = []

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        arrayDeployments = dict.get('deployments', [])
        for elemDeployments in arrayDeployments:
            obj.deployments.append(
                DeploymentMetadata.dictToObject(elemDeployments))
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
        obj = cls()

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

        #: Database Configuration
        self.sslMode = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.username = dict.get('username', None)

        obj.password = dict.get('password', None)

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.adminUsername = dict.get('adminUsername', None)

        obj.adminPassword = dict.get('adminPassword', None)

        obj.rdsCa = dict.get('rdsCa', None)

        obj.sslMode = dict.get('sslMode', None)
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
        obj = cls()

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
        obj = cls()

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

        #: Feature Flags Configuration
        self.clientAccessToken = None

        #: Feature Flags Configuration
        self.scheme = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.clientAccessToken = dict.get('clientAccessToken', None)

        obj.scheme = FeatureFlagsConfigSchemeEnum.valueForString(dict.get('scheme', None))
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
        obj = cls()

        obj.name = dict.get('name', None)

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.app = dict.get('app', None)
        return obj


class PrivateDependencyEndpoint:
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
        obj = cls()

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
        obj = cls()

        obj.accessKeyId = dict.get('accessKeyId', None)

        obj.secretAccessKey = dict.get('secretAccessKey', None)

        obj.region = dict.get('region', None)

        obj.logGroup = dict.get('logGroup', None)
        return obj


class DeploymentMetadata:
    """ Deployment Metadata
    """

    def __init__(self):

        #: Deployment Metadata
        self.name = None

        #: Deployment Metadata
        self.image = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.image = dict.get('image', None)
        return obj


class BrokerConfig:
    """ Broker Configuration
    """

    def __init__(self):

        #: Broker Configuration
        self.hostname = None

        #: Broker Configuration
        self.port = None

        #: Broker Configuration
        self.cacert = None

        #: Broker Configuration
        self.authtype = None

        #: Broker Configuration
        self.sasl = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.hostname = dict.get('hostname', None)

        obj.port = dict.get('port', None)

        obj.cacert = dict.get('cacert', None)

        obj.authtype = BrokerConfigAuthtypeEnum.valueForString(dict.get('authtype', None))

        obj.sasl = KafkaSASLConfig.dictToObject(dict.get('sasl', None))
        return obj


class TopicConfig:
    """ Topic Configuration
    """

    def __init__(self):

        #: Topic Configuration
        self.requestedName = None

        #: Topic Configuration
        self.name = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.requestedName = dict.get('requestedName', None)

        obj.name = dict.get('name', None)
        return obj


class KafkaSASLConfig:
    """ SASL Configuration for Kafka
    """

    def __init__(self):

        #: SASL Configuration for Kafka
        self.username = None

        #: SASL Configuration for Kafka
        self.password = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.username = dict.get('username', None)

        obj.password = dict.get('password', None)
        return obj


class BrokerConfigAuthtypeEnum(Enum):
    MTLS = 'mtls'
    SASL = 'sasl'

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        elif lowerStringValue == 'mtls':
            return BrokerConfigAuthtypeEnum.MTLS
        elif lowerStringValue == 'sasl':
            return BrokerConfigAuthtypeEnum.SASL
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        elif enumValue == BrokerConfigAuthtypeEnum.MTLS:
            return 'mtls'
        elif enumValue == BrokerConfigAuthtypeEnum.SASL:
            return 'sasl'
        else:
            return ''



class ObjectStoreBucket:
    """ Object Storage Bucket
    """

    def __init__(self):

        #: Object Storage Bucket
        self.accessKey = None

        #: Object Storage Bucket
        self.secretKey = None

        #: Object Storage Bucket
        self.region = None

        #: Object Storage Bucket
        self.requestedName = None

        #: Object Storage Bucket
        self.name = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.accessKey = dict.get('accessKey', None)

        obj.secretKey = dict.get('secretKey', None)

        obj.region = dict.get('region', None)

        obj.requestedName = dict.get('requestedName', None)

        obj.name = dict.get('name', None)
        return obj


class FeatureFlagsConfigSchemeEnum(Enum):
    HTTP = 'http'
    HTTPS = 'https'

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        elif lowerStringValue == 'http':
            return FeatureFlagsConfigSchemeEnum.HTTP
        elif lowerStringValue == 'https':
            return FeatureFlagsConfigSchemeEnum.HTTPS
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        elif enumValue == FeatureFlagsConfigSchemeEnum.HTTP:
            return 'http'
        elif enumValue == FeatureFlagsConfigSchemeEnum.HTTPS:
            return 'https'
        else:
            return ''



