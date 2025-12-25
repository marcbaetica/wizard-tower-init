# Built-ins.
import os
from pathlib import Path
from pprint import pprint
from shutil import copy2, rmtree

# Application libs.
from lib.constants import PROJECT_ROOT, HOME_PATH, LOCAL_GLAZEWM_CONFIG_FILE_PATH, \
                        GLAZEWM_CONFIG_FILE_PATH, GLAZEWM_CONFIG_FOLDER_PATH
from lib.exceptions import DeleteError
# from lib.fs_operations import create_folder, copy_path, delete_path_if_exists, log_if_path_exists

# 3rd-party libs.




# GlazeMW
# c:\Users\User\.glzr\glazewm\config.yaml
# delete c:\Users\User\.glzr if folder exists and confirm that it was deleted. Otherwise raise DelteError.
print(f'Removing .glzr config folder from [{GLAZEWM_CONFIG_FOLDER_PATH}].')
if GLAZEWM_CONFIG_FOLDER_PATH.exists():
    print(f'Found [{GLAZEWM_CONFIG_FOLDER_PATH}]. Deleting...')
    rmtree(GLAZEWM_CONFIG_FOLDER_PATH)
    if GLAZEWM_CONFIG_FOLDER_PATH.exists():
        raise DeleteError(f'Failed to delete folder under [{GLAZEWM_CONFIG_FOLDER_PATH}].')
else:
    print(f'Nothing to delete. HOME dotfiles were:')
    pprint([item for item in os.listdir(GLAZEWM_CONFIG_FOLDER_PATH.parent) if item[0] == '.'])

def log_resource_exists(resource: Path) -> None:
    print(f'{resource.exists()} {resource}')

# copy config.yaml path from submodule glazewm-config into c:\Users\User\.glzr\glazewm\config.yaml
# check if c:\Users\User\.glzr\glazewm\config.yaml exists
print(f'Copying new config definition from [{LOCAL_GLAZEWM_CONFIG_FILE_PATH}] to [{GLAZEWM_CONFIG_FILE_PATH}].')
try:
    copy2(LOCAL_GLAZEWM_CONFIG_FILE_PATH, GLAZEWM_CONFIG_FILE_PATH)
except FileNotFoundError as e:
    print(f'Could not find directory to copy to [{e}]. Retrying...')
    # parents -> create all missing parent directories in the path
    # exist_ok -> don't raise an error if the directory already exists.
    log_resource_exists(GLAZEWM_CONFIG_FILE_PATH.parent)
    GLAZEWM_CONFIG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    log_resource_exists(GLAZEWM_CONFIG_FILE_PATH.parent)
    log_resource_exists(GLAZEWM_CONFIG_FILE_PATH)
    copy2(LOCAL_GLAZEWM_CONFIG_FILE_PATH, GLAZEWM_CONFIG_FILE_PATH)
    log_resource_exists(GLAZEWM_CONFIG_FILE_PATH)
print(HOME_PATH)
print(GLAZEWM_CONFIG_FOLDER_PATH)
print(GLAZEWM_CONFIG_FILE_PATH)

