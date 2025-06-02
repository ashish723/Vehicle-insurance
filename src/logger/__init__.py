import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

log_dir='logs'
log_file=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
max_log_file=5*1024*1024
backup_count=3

log_dir_path=os.path.join(from_root(),log_dir)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path=os.path.join(log_dir_path,log_file)

def config_logger():
    ''' config handler with the rotating file handle and console fille handler'''
    logger=logging.getLogger()
    logger.setLevel(level='DEBUG')
    formatter= logging.Formatter('%(asctime)s %(message)s %(name)s %(levelname)s')

    file_handler=RotatingFileHandler(log_file_path,maxBytes=max_log_file,backupCount=backup_count)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler=logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

config_logger()