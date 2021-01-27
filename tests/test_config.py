from app_common_python import LoadedConfig, KafkaTopics, DependencyEndpoints, ObjectBuckets, KafkaServers, isClowderEnabled, PrivateDependencyEndpoints

def test_load_config():
    assert LoadedConfig.kafka.brokers[0].port == 27015, "Port failed to be found"
    assert KafkaTopics["originalName"].name == "someTopic"
    assert DependencyEndpoints["app1"]["endpoint1"].port == 8000
    assert DependencyEndpoints["app2"]["endpoint2"].name == "endpoint2"
    assert PrivateDependencyEndpoints["app1"]["endpoint1"].port == 10000
    assert PrivateDependencyEndpoints["app2"]["endpoint2"].name == "endpoint2"
    assert ObjectBuckets["reqname"].name == "name"
    assert KafkaServers[0] == "broker-host:27015"
    with open(LoadedConfig.rds_ca()) as fp:
        ca_content = fp.read()
        assert ca_content == "ca"
    assert isClowderEnabled() == True
    assert LoadedConfig.featureFlags.hostname == "ff-server.server.example.com"
