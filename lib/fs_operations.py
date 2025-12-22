# Built-ins.
import os
import sys
import shutil
from pathlib import Path

# Application libs.
# TODO: Clean this up later!
try:
    from lib.constants import HOME_PATH
    from lib.exceptions import CreateError, DeleteError
except ModuleNotFoundError as e:
    print(f'ERROR: {e}')
    print('Loading another way...')
    from constants import HOME_PATH
    from exceptions import CreateError, DeleteError


def create_folder(path: Path) -> bool:
    path = path.resolve()
    if path.exists():
        return False
    else:
        # Create missing parents also and don't raise error if already exists.
        path.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            raise CreateError(f'Failed to create folder under [{path}].')
        return True


def delete_path_if_exists(path: Path) -> bool:
    path = path.resolve()
    print(f'Attempting to delete item(s) at path: [{path}].')
    if not path.exists():
        print('Nothing to remove.')
        return True
    else:
        return _delete_path(path)


def _delete_path(path: Path) -> bool:
    if not path.exists():
        return False
    # TODO: Handle exceptions for path and shutil calls.
    if path.is_symlink() or path.is_file():
        # If symlink remove the pointer, not the target.
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)
    if path.exists():
        raise DeleteError(f'Failed to remove path. Contents of parent dir:\n{os.listdir(path.parent)}')
    print('File succesfully removed.')
    return True


# create folder -> Done!
# detele file   -> Done!

from pprint import pprint

files_of_interest = ['.glzr', '', '']

if __name__ == '__main__':
    '''
    print(sys.path)
    print(HOME_PATH)
    print('Test!')
    pprint(os.listdir(HOME_PATH))
    '''
    curr_folder = Path(__file__).resolve().parent
    new_folder = Path(curr_folder, 'lala')
    print(curr_folder)
    print(new_folder)
    create_folder(new_folder)
    delete_path_if_exists(new_folder)
