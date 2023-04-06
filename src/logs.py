import logging

log_filename = '/var/log/gate/gate.log'

def   logIt( idCard, status=treu ):
  # create a logger and set its level
  logger = logging.getLogger('myprogram')
  logger.setLevel(logging.DEBUG)



# create a file handler and set its level
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG)

# create a formatter and set it on the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(file_handler)

# log a message
logger.info('Starting myprogram')
