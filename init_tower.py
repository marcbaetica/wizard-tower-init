# Built-ins.
import os
from pathlib import Path

# Application libs.
from os import waitpid
from lib.constants import HOME_PATH, GLAZEWM_CONFIG_FILE_PATH, GLAZEWM_CONFIG_PATH
from lib.fs_operations import create_folder, copy_path, delete_path_if_exists, log_if_path_exists

# 3rd-party libs.


# GlazeMW
# c:\Users\User\.glzr\glazewm\config.yaml
# delete c:\Users\User\.glzr or HOME_PATH\.glzr
# check if .glzr exists
# copy .glzr folder from submodule into the home path
# check if .glzr exists
# check if config.yaml file exists
from pprint import pprint

print(HOME_PATH)
print(GLAZEWM_CONFIG_FILE_PATH)
print(GLAZEWM_CONFIG_PATH)

# log_if_path_exists(GLAZEWM_CONFIG_FILE_PATH)
log_if_path_exists(GLAZEWM_CONFIG_PATH)
delete_path_if_exists(GLAZEWM_CONFIG_PATH)
log_if_path_exists(GLAZEWM_CONFIG_PATH)
NEW_GLAZE_CONFIG_FOLDER_PATH = Path(os.getcwd(), 'glazewm-config', '.glzr')
print(NEW_GLAZE_CONFIG_FOLDER_PATH)
log_if_path_exists(NEW_GLAZE_CONFIG_FOLDER_PATH)  # TODO: Flagged as a file currently.
copy_path(NEW_GLAZE_CONFIG_FOLDER_PATH, HOME_PATH)
log_if_path_exists(GLAZEWM_CONFIG_FILE_PATH)
log_if_path_exists(GLAZEWM_CONFIG_PATH)
