# app-common-python

Python client library for accessing [Clowder operator][clowder-operator] configuration in Red Hat Insights applications. The library provides a simple API for reading environment-based configuration and accessing Kafka, database, object storage, and service dependency settings.

## Installation

Install from PyPI:

```sh
pip install app-common-python
```

## Prerequisites

- Python 3.10+
- Applications running in a Clowder-enabled environment with the `ACG_CONFIG` environment variable set

## Usage

### Basic Configuration Access

The library loads configuration automatically from the `ACG_CONFIG` environment variable when imported. Use `isClowderEnabled()` to detect whether Clowder is active, then access settings via the `LoadedConfig` object:

```python
from app_common_python import LoadedConfig, isClowderEnabled

def main():
    if isClowderEnabled():
        print(f"Public Port: {LoadedConfig.publicPort}")
        print(f"Hostname: {LoadedConfig.hostname}")
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
* ``DependencyEndpointsV2`` - returns a nested map using \[appName\]\[endpointName\]
  for V2 dependency endpoints with simplified connection info.
* ``get_v2_dependency_endpoint(app, endpoint)`` - returns a single V2 endpoint
  or ``None`` if not found.
* ``PrivateDependencyEndpointsV2`` - returns a nested map using \[appName\]\[endpointName\]
  for V2 private dependency endpoints with simplified connection info.
* ``get_v2_private_dependency_endpoint(app, endpoint)`` - returns a single V2 private
  endpoint or ``None`` if not found.

V2 Dependency Endpoints
-----------------------

V2 endpoints provide simplified, opinionated configuration for service-to-service
connections. Each endpoint includes a single URI, an authentication flag, and an
optional CA certificate path.

```python
from app_common_python import DependencyEndpointsV2, get_v2_dependency_endpoint, isClowderEnabled

if isClowderEnabled():
    # Access via the nested map
    rbac = DependencyEndpointsV2["rbac"]["service"]
    print(f"URI: {rbac.uri}")
    print(f"Authenticated: {rbac.authenticated}")
    if rbac.ca_certificate:
        print(f"CA Cert: {rbac.ca_certificate}")

    # Or use the helper function
    ep = get_v2_dependency_endpoint("rbac", "service")
    if ep:
        print(f"URI: {ep.uri}")
```

V2 endpoint fields:
* ``uri`` - Full URI for the service (e.g. ``https://rbac-service.env.svc:8443``)
* ``authenticated`` - ``True`` for cross-cluster (ClowdAppRef), ``False`` for in-cluster
* ``ca_certificate`` - Path to CA certificate for TLS (only present for in-cluster TLS)


### API Overview

The library provides several convenience accessors for common configuration lookups:

#### Certificate Helpers

- **`LoadedConfig.rds_ca()`** — Creates a temporary file containing the RDS CA certificate and returns the file path. Useful for database libraries that require CA certificates as file paths.
- **`LoadedConfig.kafka_ca()`** — Creates a temporary file containing the Kafka CA certificate from the first broker and returns the file path.

#### Kafka Configuration

- **`KafkaTopics`** — Dictionary mapping `requestedName` (your application's topic name) to `TopicConfig` objects containing the actual Kafka topic name and configuration.
- **`KafkaServers`** — List of Kafka broker URLs in `hostname:port` format.

Example:

```python
from app_common_python import KafkaServers, KafkaTopics

# Connect to Kafka brokers
brokers = KafkaServers  # ["kafka-broker-1:9092", "kafka-broker-2:9092"]

# Look up the actual topic name for a requested topic
topic_config = KafkaTopics["my-topic"]
actual_topic_name = topic_config.name
```

#### Object Storage

- **`ObjectBuckets`** — Dictionary mapping `requestedName` to `ObjectStoreBucket` objects containing bucket name, access credentials, and endpoint information.

#### Service Dependencies

- **`DependencyEndpoints`** — Nested dictionary `[app_name][deployment_name]` → `DependencyEndpoint` for accessing public service endpoints of other applications.
- **`PrivateDependencyEndpoints`** — Nested dictionary `[app_name][deployment_name]` → `PrivateDependencyEndpoint` for accessing private service endpoints.

Example:

```python
from app_common_python import DependencyEndpoints

# Access another service's endpoint
other_service = DependencyEndpoints["other-app"]["api"]
service_url = f"http://{other_service.hostname}:{other_service.port}"
```

For a detailed explanation of the library's schema-driven design and code generation pipeline, see the [Architecture documentation][architecture-doc].

## Development

### Local Setup

Clone the repository and create a virtual environment:

```sh
git clone https://github.com/RedHatInsights/app-common-python.git
cd app-common-python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### Running Tests

Tests use a static configuration file (`test.json`) to verify the runtime API. Run the test suite with:

```sh
ACG_CONFIG=test.json pytest
```

### Regenerating Types

The library uses code generation to stay in sync with the upstream Clowder schema. To regenerate the `types.py` file after schema changes:

```sh
./sync_config.sh
```

This script requires Podman and fetches the latest schema from the Clowder project, then regenerates the Python types using the [yacg code generator][yacg-project].

### Linting

The project uses flake8 for code style checks:

```sh
flake8 app_common_python tests
```

Configuration is in `setup.cfg` (max line length: 100, ignores: E128, E811, W503, E203).

### Contributing

See the [Contributing guidelines][contributing-doc] for information on commit signing, pull request workflow, and code review process.

## License

**License information not found in repository.** Contributors should clarify licensing with project maintainers before submitting changes.

## Related Documentation

- [Architecture][architecture-doc] — Schema-driven design and code generation pipeline
- [Contributing][contributing-doc] — Commit signing, pull request workflow, and guidelines
- [Clowder Operator][clowder-operator] — Upstream Kubernetes operator project

[clowder-operator]: https://github.com/RedHatInsights/clowder
[architecture-doc]: ./ARCHITECTURE.md
[contributing-doc]: ./CONTRIBUTING.md
[yacg-project]: https://github.com/OkieOth/yacg
