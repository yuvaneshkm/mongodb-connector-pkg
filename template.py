# importing necessary libraries:
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# package name:
package_name = 'mdb_connect_pkg'

# creating a list of files and folders required for this project:
list_of_files = [

    # creating a yaml file:
    '.github/workflows/ci.yaml',
    '.github/workflows/python-publish.yaml',


    # creating src folder:
    'src/__init__.py',
    # src ----- mongodb_connect:
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/mongo_crud.py',


    # creating tests folder:
    'tests/__init__.py',
    # tests --- unit:
    'tests/unit/__init__.py',
    'tests/unit/test_unit.py',
    # tests --- integration:
    'tests/integration/__init__.py',
    'tests/integration/test_integration.py',


    # setup files:
    'init_setup.sh',
    'setup.py',
    'setup.cfg',
    # requirements:
    'requirements.txt',
    'requirements_dev.txt',
    # toml file:
    'pyproject.toml',
    # ini file:
    'tox.ini',
    # rst file:
    'README.rst',
    # experiments notebook:
    'experiments/experiments.ipynb'

]


# creating folders and files:
for filepath in list_of_files:
    filepath = Path(filepath)
    # getting file directory and file name by splitting filepath:
    filedir, filename = os.path.split(filepath)
    # CREATING DIRECTORY:
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
    # CREATING FILES:
    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath, 'w') as f:
            pass
        f.close()