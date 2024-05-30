# ============================ Importing necessary packages ==============================
from setuptools import setup, find_packages
from typing import List
import warnings
warnings.filterwarnings('ignore')

# ==================================== Setup ===============================================

# basic info:
PKG_NAME= "mdb_connect_pkg"
__version__ = "0.0.4"
AUTHOR_USER_NAME = "yuvaneshkm"
REPO_NAME = "mongodb-connector-pkg"
AUTHOR_EMAIL = "yuvaneshkm27@gmail.com"

# long description (reading the README.md file):
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()  
f.close()

# requirements:
HYPEN_E_DOT = '-e .'
def get_requirements(requirements_file_path: str) -> List[str]:

    with open(requirements_file_path, 'r') as f:
        require = f.read()
        requirements = require.split('\n')
        # remove -e .
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    f.close()

    return requirements
   
# setup:
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements('requirements.txt'),
    extras_require = {'dev': get_requirements('requirements_dev.txt')}
    )