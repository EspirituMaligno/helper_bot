# adaptive_logger.py
import logging
import sys
import json
from typing import Optional
from src.core.config import settings
import datetime


class AdaptiveJsonFormatter(logging.Formatter):
    def __init__(self, service_name: str):
        super().__init__()
        self.service_name = service_name

    def formatTime(self, record, datefmt=None):

        dt = datetime.datetime.fromtimestamp(record.created)

        return dt.strftime("%Y-%m-%d %H:%M:%S") + f",{int(dt.microsecond / 1000):03d}"

    def format_source_info(self, record):
        result = dict()

        result["module"] = record.module

        if record.levelno >= logging.ERROR:
            result["path"] = record.pathname

        if record.funcName != "<module>":
            result["func"] = record.funcName

        return result

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "@Timestamp": self.formatTime(record),
            "Message": record.getMessage(),
            "Properties": {
                "Level": record.levelname,
                "ServiceName": self.service_name,
                "logger": record.name,
            },
        }
        source_info = self.format_source_info(record=record)
        log_entry["Properties"].update(source_info)

        return json.dumps(log_entry, ensure_ascii=False)


class AppLogger:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        name: str = "app_logger",
        service_name: str = "Unknown Service",
        log_to_console: bool = True,
        log_to_file: Optional[str] = None,
    ):
        if self._initialized:
            return
        self._initialized = True

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        self.logger.handlers.clear()

        formatter = AdaptiveJsonFormatter(service_name=service_name)

        if log_to_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        if log_to_file:
            file_handler = logging.FileHandler(log_to_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


logger = AppLogger(
    name="helper_bot",
    service_name="HelperBot",
    log_to_console=True,
    log_to_file=settings.LOG_PATH,
).get_logger()
