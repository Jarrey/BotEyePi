#!/usr/bin/python
import logging
import logging.handlers
import setting as s

handler = logging.handlers.RotatingFileHandler(s.log_file, maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('speedpro')
logger.addHandler(handler)
logger.setLevel(logging.INFO)