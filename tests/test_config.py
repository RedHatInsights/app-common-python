from app_common_python import (
    LoadedConfig, KafkaTopics, DependencyEndpoints, ObjectBuckets,
    KafkaServers, isClowderEnabled, PrivateDependencyEndpoints,
    DependencyEndpointsV2, get_v2_dependency_endpoint,
    PrivateDependencyEndpointsV2, get_v2_private_dependency_endpoint,
    loadConfig,
)
from app_common_python.types import V2Endpoint


def test_load_config():
    assert LoadedConfig.kafka.brokers[0].port == 27015, "Port failed to be found"
    assert KafkaTopics["originalName"].name == "someTopic"
    assert DependencyEndpoints["app1"]["endpoint1"].port == 8000
    assert DependencyEndpoints["app2"]["endpoint2"].name == "endpoint2"
    assert DependencyEndpoints["app1"]["endpoint1"].apiPath == "app1-api-path"
    assert DependencyEndpoints["app2"]["endpoint2"].apiPath == "app2-api-path"
    assert PrivateDependencyEndpoints["app1"]["endpoint1"].port == 10000
    assert PrivateDependencyEndpoints["app2"]["endpoint2"].name == "endpoint2"
    assert ObjectBuckets["reqname"].name == "name"
    assert KafkaServers[0] == "broker-host:27015"
    assert LoadedConfig.kafka.brokers[0].securityProtocol == "plaintext"
    with open(LoadedConfig.rds_ca()) as fp:
        ca_content = fp.read()
        assert ca_content == "ca"
    with open(LoadedConfig.kafka_ca()) as fp:
        ca_content = fp.read()
        assert ca_content == "kafkaca"
    assert isClowderEnabled() == True
    assert LoadedConfig.featureFlags.hostname == "ff-server.server.example.com"
    assert LoadedConfig.hostname == "testing"


def test_v2_dependency_endpoints_parsed():
    assert "app1" in DependencyEndpointsV2
    assert "app2" in DependencyEndpointsV2
    assert "service" in DependencyEndpointsV2["app1"]
    assert "api" in DependencyEndpointsV2["app2"]


def test_v2_endpoint_fields():
    ep = DependencyEndpointsV2["app1"]["service"]
    assert isinstance(ep, V2Endpoint)
    assert ep.uri == "https://app1-service.env.svc:8443"
    assert ep.ca_certificate == "/cdapp/certs/service-ca.crt"
    assert ep.authenticated is False


def test_v2_endpoint_authenticated_cross_cluster():
    ep = DependencyEndpointsV2["app2"]["api"]
    assert ep.uri == "https://app2-api.env.svc:8443"
    assert ep.ca_certificate is None
    assert ep.authenticated is True


def test_get_v2_dependency_endpoint():
    ep = get_v2_dependency_endpoint("app1", "service")
    assert ep is not None
    assert ep.uri == "https://app1-service.env.svc:8443"


def test_get_v2_dependency_endpoint_missing_app():
    assert get_v2_dependency_endpoint("nonexistent", "service") is None


def test_get_v2_dependency_endpoint_missing_endpoint():
    assert get_v2_dependency_endpoint("app1", "nonexistent") is None


def test_v2_missing_from_config():
    config = loadConfig(None)
    assert config.dependencyEndpoints is None


def test_v2_private_dependency_endpoints_parsed():
    assert "app1" in PrivateDependencyEndpointsV2
    assert "app2" in PrivateDependencyEndpointsV2
    assert "internal" in PrivateDependencyEndpointsV2["app1"]
    assert "worker" in PrivateDependencyEndpointsV2["app2"]


def test_v2_private_endpoint_fields():
    ep = PrivateDependencyEndpointsV2["app1"]["internal"]
    assert isinstance(ep, V2Endpoint)
    assert ep.uri == "https://app1-internal.env.svc:10443"
    assert ep.ca_certificate == "/cdapp/certs/internal-ca.crt"
    assert ep.authenticated is False


def test_v2_private_endpoint_authenticated():
    ep = PrivateDependencyEndpointsV2["app2"]["worker"]
    assert ep.uri == "https://app2-worker.env.svc:10443"
    assert ep.ca_certificate is None
    assert ep.authenticated is True


def test_get_v2_private_dependency_endpoint():
    ep = get_v2_private_dependency_endpoint("app1", "internal")
    assert ep is not None
    assert ep.uri == "https://app1-internal.env.svc:10443"


def test_get_v2_private_dependency_endpoint_missing_app():
    assert get_v2_private_dependency_endpoint("nonexistent", "internal") is None


def test_get_v2_private_dependency_endpoint_missing_endpoint():
    assert get_v2_private_dependency_endpoint("app1", "nonexistent") is None


def test_v2_private_missing_from_config():
    config = loadConfig(None)
    assert config.privateDependencyEndpoints is None


def test_v1_endpoints_unchanged():
    assert DependencyEndpoints["app1"]["endpoint1"].port == 8000
    assert PrivateDependencyEndpoints["app1"]["endpoint1"].port == 10000