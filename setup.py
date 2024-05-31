# ============================ Importing necessary packages ==============================
from setuptools import setup, find_packages
from typing import List
import warnings
warnings.filterwarnings('ignore')

# ==================================== Setup ===============================================

# basic info:
PKG_NAME= "mdb_connect_pkg"
__version__ = "1.1.1"
AUTHOR_USER_NAME = "yuvaneshkm"
REPO_NAME = "mongodb-connector-pkg"
AUTHOR_EMAIL = "yuvaneshkm27@gmail.com"

# long description:
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# setup:
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=read_file('README.rst'),
    long_description_content_type="text/x-rst",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
    )