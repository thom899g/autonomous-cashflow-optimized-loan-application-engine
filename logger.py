import logging
from datetime import datetime

class CustomLogger:
    """
    A custom logging class that extends Python's built-in logging module.
    Implements a file handler and a console handler with specific formatting.
    """

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Prevent adding handlers multiple times
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            file_handler = logging.FileHandler('loan_app_engine.log')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message):
        """
        Logs an informational message.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Logs a warning message.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Logs an error message and includes timestamp.
        """
        self.logger.error(f"{datetime.now()}: {message}")

    def critical(self, message):
        """
        Logs a critical message that should be immediately addressed.
        """
        self.logger.critical(message)