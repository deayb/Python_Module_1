import sys
import os


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix 

def main() -> None:
    venv_name = os.path.basename(sys.prefix)
    venv_path = sys.prefix
    