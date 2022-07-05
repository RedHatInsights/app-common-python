app-common-python
=================

Simple client access library for the config for the Clowder operator.

Usage
-----

To access configuration, see the following example

```python
from app_common_python import LoadedConfig, isClowderEnabled

def main():
    if isClowderEnabled():
        print(f"Public Port: {LoadedConfig.PublicPort}")
```

The ``clowder`` library also comes with several other helpers

* ``LoadedConfig.rds_ca()`` - creates a temporary file with the RDSCa and
  returns the filename.
* ``LoadedConfig.kafka_ca()`` - creates a temporary file with the KafkaCa and
  returns the filename from the frist broker in the list.
* ``KafkaTopics`` - returns a map of KafkaTopics using the requestedName
  as the key and the topic object as the value.
* ``KafkaServers`` - returns a list of Kafka Broker URLs.
* ``ObjectBuckets`` - returns a list of ObjectBuckets using the requestedName
  as the key and the bucket object as the value.
* ``DependencyEndpoints`` - returns a nested map using \[appName\]\[deploymentName\]
  for the public services of requested applications.
* ``PrivateDependencyEndpoints`` - returns a nested map using \[appName\]\[deploymentName\]
  for the private services of requested applications.

Testing
-------

``ACG_CONFIG="test.json" pytest``
