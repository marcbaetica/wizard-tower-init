from pathlib import Path


for parent_path in Path(__file__).resolve().parents:
    if (parent_path / 'init_tower.py').exists():
        print(f'Found parent path at [{parent_path}].')
        break
else:
    raise RuntimeError('Project root not found.')

PROJECT_ROOT = parent_path
LOCAL_GLAZEWM_CONFIG_FILE_PATH = Path(PROJECT_ROOT, 'glazewm-config', '.glzr', 'glazewm', 'config.yaml').resolve()

HOME_PATH = Path.home().resolve()
GLAZEWM_CONFIG_FOLDER_PATH = Path(HOME_PATH, '.glzr').resolve()
GLAZEWM_CONFIG_FILE_PATH = Path(GLAZEWM_CONFIG_FOLDER_PATH, 'glazewm', 'config.yaml')

APPDATA_LOCAL_PATH = Path(HOME_PATH, 'AppData', 'Local').resolve()
NVIM_CONFIG_PATH = Path(APPDATA_LOCAL_PATH, 'nvim').resolve()   # Config lua files.
NVIM__PATH = Path(APPDATA_LOCAL_PATH, 'nvim-data').resolve()    # Lazy, Mason, etc.
NVIM__PATH = Path(APPDATA_LOCAL_PATH, 'npm-cache').resolve()    # Pyright.

