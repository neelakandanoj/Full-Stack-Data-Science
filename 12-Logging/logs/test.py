from logger import logging

def add(a,b):
    logging.debug('Addition is taking place.')
    return a+b
logging.debug("Addition function is called.")
add(9,7)