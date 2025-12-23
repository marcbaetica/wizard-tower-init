# Built-ins.
import os
import sys
import shutil
from pathlib import Path

# 3rd-party libs.
# from pprintpp import pprint   # TODO: See if needed.

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


def log_if_path_exists(path: Path) -> None:
    if path.exists():
        print(f'Resource already exists at [{path}].')
    else:
        print(f'No resource found at [{path}].')


def create_folder(path: Path) -> bool:
    path = path.resolve()
    print(f'Creating folders under path: [{path}]')
    if path.exists():
        return False
    else:
        # Create missing parents also and don't raise error if already exists.
        path.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            raise CreateError(f'Failed to create folder under [{path}].')
        return True


def _is_safe_to_delete(path: Path) -> bool:
    path = path.resolve()
    if HOME_PATH == path or path in HOME_PATH.parents:
        print(HOME_PATH, type(HOME_PATH))
        print(path, type(path))
        print(path.parents, type(path.parents))
        return False
    return True


def delete_path_if_exists(path: Path) -> bool:
    path = path.resolve()
    print(f'Attempting to delete item(s) at path: [{path}].')
    if not _is_safe_to_delete(path):
        raise DeleteError("Refusing to delete home directory [{path}].")
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


def copy_path(src: Path, dest: Path) -> None:
    src = src.resolve()
    dest = dest.resolve()
    print(f'Attempting to copy [{src}] to [{dest}].')
    # If file:
    if dest.is_file():
        delete_path_if_exists(dest)
    try:
        shutil.copytree(src, dest, dirs_exist_ok=True)
    except FileExistsError:
        delete_path_if_exists(dest)
        shutil.copytree(src, dest, dirs_exist_ok=True)
    shutil.copytree(src, dest)


# create folder                 -> Done!
# detele folder & parent dirs   -> Done!
# copy folder


files_of_interest = ['.glzr', '', '']

if __name__ == '__main__':
    '''
    print(sys.path)
    print(HOME_PATH)
    print('Test!')
    pprint(os.listdir(HOME_PATH))
    curr_folder = Path(__file__).resolve().parent
    new_folder = Path(curr_folder, 'lala')
    deep_new_folder = Path(new_folder, 'lala2')
    print(curr_folder)
    print(new_folder)
    print(deep_new_folder)
    create_folder(deep_new_folder)
    delete_path_if_exists(new_folder)
    print(HOME_PATH)
    print(type(HOME_PATH))
    '''

