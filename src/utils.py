import os
import sys
import numpy as np
import pandas as pd
import dill
from src.logger import logging

from src.exception import CustomException


def save_object(file_path,obj):
    try:
              
       ## logging.info(f"Path received in Utils:{file_path}")
        dir_path= os.path.dirname(file_path)

       ## logging.info(f"Path Created in Utils:{dir_path}")

        os.makedirs(dir_path,exist_ok=True)

       ## logging.info("Dir created based on path in Utils")

        with open (file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)        
