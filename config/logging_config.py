import logging

import json_log_formatter


def setup_logging():
    """
    This function configures a logger that outputs logs in JSON format to the console.
    It uses the `json_log_formatter` library to format the logs as JSON.
    The logger is set to the INFO level, meaning it will capture all logs at this level
    and above (INFO, WARNING, ERROR, CRITICAL).

    Return:
        logger (logging.Logger): Configured logger instance.
    """

    # Create a stream handler with the JSON formatter
    json_handler = logging.StreamHandler()
    json_handler.setFormatter(json_log_formatter.JSONFormatter())

    # Create a logger and set its level
    logger = logging.getLogger("app_logger")
    logger.addHandler(json_handler)
    logger.setLevel(logging.INFO)

    return logger
