import logging

## Logging Configuration ##

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler() # console handler
ch.setLevel(logging.INFO)
fh = logging.FileHandler('logfile.txt')
fh.setLevel(logging.INFO)

fmtr = logging.Formatter('%(asctime)s | [%(levelname)s] | (%(name)s) | %(message)s')
fh.setFormatter(fmtr)

logger.addHandler(fh)
logger.addHandler(ch) #disable this to stop console output.  This better than print statements as you can disable all console output in 1 spot instead of every print statement.

logger.critical(f'testing a critical message from {__name__}')