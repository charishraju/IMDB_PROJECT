import logging

# Logger Configuration
LOG_FILE = "app.log"  # Log file name

# Define log format
log_format = "%(asctime)s - [%(levelname)s] - (%(filename)s:%(lineno)d) - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Create logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Set the logging level

# Console Handler (Prints to console)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Change to logging.INFO if needed
console_handler.setFormatter(logging.Formatter(log_format, date_format))

# File Handler (Writes to file)
file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_format, date_format))

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
