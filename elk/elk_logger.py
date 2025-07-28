import logging
import logging.handlers
import json
import socket
from datetime import datetime

class LogstashFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'filename': record.filename,
            'lineno': record.lineno,
        }
        return json.dumps(log_record)

logger = logging.getLogger("elk-logger")
logger.setLevel(logging.INFO)

logstash_handler = logging.handlers.SocketHandler("localhost", 5000)
logstash_handler.setFormatter(LogstashFormatter())
logger.addHandler(logstash_handler)

# Test logs
logger.info("Ola como vai?")
logger.warning("Potential issue detected")
logger.error("Something went wrong")
