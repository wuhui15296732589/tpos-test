import unittest


from common.Log import MyLog as Log
import cx_Oracle
from common import commonORBD

log = Log.get_log()
logger = log.logger

class StartEnd(unittest.TestCase):
    logger = logger

    def setUp(self):
        logger.info('=======================setup================')

    def tearDown(self):
        logger.info('=======================tearDown=============')
