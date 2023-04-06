import logging


def   valideCard( idCard, status=True ):

    log_filename = '/var/log/gate/gate.log'
      # create a logger and set its level
    logger = logging.getLogger('gate')
    logger.setLevel(logging.INFO)

    # create a file handler and set its level
    file_handler = logging.FileHandler(log_filename)
    # file_handler.setLevel(logging.INFO)

    # create a formatter and set it on the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    # add the handler to the logger
    logger.addHandler(file_handler)
    return logger