# ELK

## Structure
.
├── docker-compose.yml
├── elk_logger.py
└── logstash/
    └── logstash.conf


## How to run
docker compose up -d
elk_logger

Open Kibana at http://localhost:5601, and navigate to "Discover", create index pattern python-logs-*