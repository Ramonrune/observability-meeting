# ELK

## Structure
.
├── docker-compose.yml
├── elk_logger.py
└── promtail/
|    └── config.yml
└── prometheus/
    └── prometheus.yml

## How to run
docker compose up -d


Open Prometheus at http://localhost:9090/
Open Grafana at http://localhost:3000/login (user: admin, pass: admin)
Data Sources → Add Prometheus (http://localhost:9090)
Data Sources → Add Loki (http://localhost:3100) ou http://loki:3100 -> checar se loki está ready http://localhost:3100/ready