import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "basic": {
            "format": "%(asctime)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console_info": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "basic",
            "stream": "ext://sys.stdout"
        },
        "file_info": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "basic",
            "filename": "app_info.log",
            "mode": "a"
            },
        "file_error": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "basic",
            "filename": "app_errors.log",
            "mode": "a"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console_info", "file_error", "file_info"]
    }
}

logging.config.dictConfig(LOGGING_CONFIG)