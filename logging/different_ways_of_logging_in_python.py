import math
import logging
from icecream import ic


def square_root(number):
    return math.sqrt(number)


def demo_print():
    print('Square root of 20 is ', square_root(20))
    print('Square root of {0} is {1}'.format(20, square_root(20)))


def demo_log_to_file():
    file_in = open('logging/logfile.txt', 'w')
    file_in.writelines('Square root of {0} is {1}'.format(20, square_root(20))) 


def demo_logging_module():
    #Create and configure logger
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.WARNING)
    #Creating an object
    logger=logging.getLogger()
    
    kwargs = {'number':20, 'squareroot':square_root(20)}
    
    #Test messages
    logger.debug("Square root of {number} is {squareroot}".format(**kwargs))
    logger.info("Square root of {number} is {squareroot}".format(**kwargs))
    logger.warning("Square root of {number} is very high".format(**kwargs))
    logger.error("Number {number} to calculate squareroot cannot be negative".format(**kwargs))
    logger.critical("App crashed due to low memory".format(**kwargs))


def demo_icecream_module():
    ic()
    ic(square_root(20))


if __name__ == '__main__':
    demo_print()
    demo_log_to_file()
    demo_logging_module()
    demo_icecream_module()