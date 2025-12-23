from pathlib import Path


HOME_PATH = Path.home().resolve()
GLAZEWM_CONFIG_PATH = Path(HOME_PATH, '.glzr').resolve()
GLAZEWM_CONFIG_FILE_PATH = Path(GLAZEWM_CONFIG_PATH, 'glazewm', 'config.yaml')

APPDATA_LOCAL_PATH = Path(HOME_PATH, 'AppData', 'Local').resolve()
NVIM_CONFIG_PATH = Path(APPDATA_LOCAL_PATH, 'nvim').resolve()   # Config lua files.
NVIM__PATH = Path(APPDATA_LOCAL_PATH, 'nvim-data').resolve()    # Lazy, Mason, etc.
NVIM__PATH = Path(APPDATA_LOCAL_PATH, 'npm-cache').resolve()    # Pyright.

