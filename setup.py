# ============================ Importing necessary packages ==============================
from setuptools import setup, find_packages
from typing import List
import warnings
warnings.filterwarnings('ignore')

# ==================================== Setup ===============================================

# basic info:
PKG_NAME= "mdb_connect_pkg"
__version__ = "0.0.5"
AUTHOR_USER_NAME = "yuvaneshkm"
REPO_NAME = "mongodb-connector-pkg"
AUTHOR_EMAIL = "yuvaneshkm27@gmail.com"

# long description:
with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()
f.close()

# setup:
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
    )