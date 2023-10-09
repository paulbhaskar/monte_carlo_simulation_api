import sys
import logging as lg

logger = lg.getLogger('backend_logger')


class Log:
    @staticmethod
    def debug(msg):
        file_name = sys._getframe().f_back.f_code.co_filename
        function_name = sys._getframe().f_back.f_code.co_name
        logger.debug(file_name.__add__(
            ' - Function: ').__add__(function_name).__add__(' - Message: ').__add__(msg))  # NOSONAR

    @staticmethod
    def info(msg):
        file_name = sys._getframe().f_back.f_code.co_filename
        function_name = sys._getframe().f_back.f_code.co_name
        logger.info(file_name.__add__(
            ' - Function: ').__add__(function_name).__add__(' - Message: ').__add__(msg))

    @staticmethod
    def error(msg, exception=None):
        file_name = sys._getframe().f_back.f_code.co_filename
        function_name = sys._getframe().f_back.f_code.co_name
        logger.error(file_name.__add__(
            ' - Function: ').__add__(function_name).__add__(' - Message: ').__add__(msg).__add__(f' {exception if exception else ""}'))

    @staticmethod
    def warning(msg):
        file_name = sys._getframe().f_back.f_code.co_filename
        function_name = sys._getframe().f_back.f_code.co_name
        logger.warning(file_name.__add__(
            ' - Function: ').__add__(function_name).__add__(' - Message: ').__add__(msg))
