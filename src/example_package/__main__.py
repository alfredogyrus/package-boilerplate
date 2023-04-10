import sys
from pathlib import Path

import toml
from dotenv import load_dotenv

from example_package.module1.module1 import my_sum
from example_package.module2 import module2_function

if __name__ == "__main__":
    ROOT_PATH = Path(__file__).parent.parent.parent
    dotenv_path = Path(ROOT_PATH, '.env')
    load_dotenv(dotenv_path=dotenv_path)

    with open(Path(ROOT_PATH, 'config.toml'), 'r') as f:
        config = toml.load(f)

    param2 = config['key']['param2']
    module2_function()
    args = sys.argv[1:]
    print(my_sum(*args, param2))