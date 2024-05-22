# ====================> importing necessary packages <========================
from setuptools import setup, find_packages
import warnings
warnings.filterwarnings('ignore')


# ======================> SETUP <============================

# basic info:
PKG_NAME = 'mongodbconnect'
__version__ = '0.0.1'
AUTHOR_USER_NAME = 'yuvaneshkm'
AUTHOR_EMAIL = 'yuvaneshkm05@gmail.com'
REPO_NAME = 'mongodb-connector-pkg'

# long description (reading the README.md file):
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
f.close()

# requirements:
def get_requirements(requirements_file_path:str):

    with open(requirements_file_path, 'r') as f:
        require = f.read()
        requirements = require.split('\n')
        # remove '-e .
        if '-e .' in requirements:
            requirements.remove('-e .')
    f.close()

    return requirements

# setup:
setup(
    name = PKG_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = 'Python Package for connecting MongoDB Database',
    long_description =  LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    url = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker':f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir = {'':'src'},
    packages = find_packages(where='src'),
    install_requires = get_requirements('requirements.txt')
)