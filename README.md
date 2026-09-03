# Iceberg Spark Mobile Agent

A mobile agent application for managing Apache Iceberg tables using Apache Spark, with Modal + Local Docker setup.

## Overview

This project provides a mobile-first agent interface for:
- Managing Iceberg table schemas and metadata
- Executing Spark queries and transformations
- Monitoring data lake operations
- Real-time data updates and sync

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.9+

### Local Development

```bash
git clone https://github.com/corkumandrew557-tech/iceberg-spark-mobile-agent.git
cd iceberg-spark-mobile-agent
docker-compose -f docker/docker-compose.yml up -d
pip install -r requirements.txt
python -m app.main
```

### Access Points
- API: http://localhost:8000
- Spark UI: http://localhost:4040
- MinIO: http://localhost:9001
- Iceberg REST: http://localhost:8181

## Features

- Iceberg table management
- Spark SQL query execution
- Real-time data synchronization
- REST API
- Docker containerization

## License

MIT
