# Built-ins.
import os
from pathlib import Path
from pprint import pprint

# Application libs.
from lib.constants import PROJECT_ROOT, HOME_PATH, LOCAL_GLAZEWM_CONFIG_FILE_PATH, \
                        GLAZEWM_CONFIG_FILE_PATH, GLAZEWM_CONFIG_FOLDER_PATH
# from lib.fs_operations import create_folder, copy_path, delete_path_if_exists, log_if_path_exists

# 3rd-party libs.


print(HOME_PATH)
print(GLAZEWM_CONFIG_FOLDER_PATH)
print(GLAZEWM_CONFIG_FILE_PATH)

from shutil import rmtree


# GlazeMW
# c:\Users\User\.glzr\glazewm\config.yaml
# delete c:\Users\User\.glzr or HOME_PATH\.glzr
if GLAZEWM_CONFIG_FOLDER_PATH.exists():
    print(f'Found [{GLAZEWM_CONFIG_FOLDER_PATH}].')
    rmtree(GLAZEWM_CONFIG_FOLDER_PATH)
    # check if .glzr exists
    print(GLAZEWM_CONFIG_FOLDER_PATH.exists())
# copy config.yaml path from submodule into the home path
# check if .glzr exists
# check if config.yaml file exists

