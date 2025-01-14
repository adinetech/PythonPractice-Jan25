## Simple Logging: Use Python’s logging module to log info and error messages in a script.

import logging

def log_info():
    logging.basicConfig(filename='info.log', level=logging.INFO)
    logging.info('This is an info message.')

def log_error():
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error('This is an error message.')

log_info()
log_error()