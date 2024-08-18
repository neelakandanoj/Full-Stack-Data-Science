## Configuration logging
import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
##Logging message
logging.debug("This is a debug message.")
logging.info('This is an info message.')
logging.warning('This is an warning message.')
logging.error('This is an error meesage.')
logging.critical('This is an critical.')