import os
import logging
import sys

def error_message_detail(error:Exception,error_detail:sys)->sys:
    '''exports detailed error'''
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    lineno=exc_tb.tb_lineno
    error_message=f"error occured at file {file_name} at line no {lineno} : {str(error)}"
    logging.error(error_message)
    return error_message


class MyException(Exception):
    def __init__(self,error_message:str,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message