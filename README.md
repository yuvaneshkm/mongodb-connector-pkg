# MongoDB connector package

# Overview
**mdb_connect_pkg** is a Python package designed to simplify the process of connecting to and interacting with MongoDB databases. This package provides a streamlined API for performing CRUD (Create, Read, Update, Delete) operations, handling connections, and managing MongoDB collections with ease.

# Features
* Easy connection management to MongoDB instances
* Simple CRUD operations
* Handling of MongoDB collections

# Directory Structure
```plaintext
mongodb-connector-pkg/
├── .github/
│   └── workflows/
│       └── ci.yaml
│       └── python-publish.yaml
├── src/
│   └── mdb_connect_pkg/
│       └── mongo_crud.py
├── tests/
│   ├── unit/
│   │   └── test_unit.py
│   └── integration/
│       └── test_integration.py
├── .gitignore
├── init_setup.sh
├── LICENSE
├── pyproject.toml
├── README.md
├── README.rst
├── requirements_dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── template.py
└── tox.ini
```

## requirements_dev.txt we use for the testing
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

## difference between requirements_dev.txt and requirements.txt

requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

## tox.ini
We use if for the testing in the python package testing against different version of the python 

### how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox


## pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system
such as the build tool used package name version author license and dependencies

## setup.cfg
In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec

## Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

*Mode of testing*
1. Unit testing
2. Integration tests

*Testing frameworks*

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

## check with the code style formatting and syntax(coding standard)

1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle

## CI/CD
 Implemented a robust CI/CD pipeline using GitHub Actions to automate testing, building, and deployment of this package to the PyPI repository. This ensures that every change is thoroughly tested and seamlessly deployed, maintaining the highest quality standards.

# How to use this package?

## Installation
To install the package, use pip:
```bash
pip install mdb-connect-pkg==1.1.1
```

## Usage
### Connecting to MongoDB
First, import the package and create a connection instance:
```py
# Importing the package
from mdb_connect_pkg import mongo_crud

# Initialize the connector
db_connection_url = 'mongodb://localhost:27017'
database_name = 'mydatabase'
collection_name = 'mycollection'
mongo = mongo_crud.MongoDBConnection(db_connection_url, database_name, collection_name)

# Creating the client and connect to the database
mongo.create_mongo_client()
mongo.database_()
mongo.collection_()
```

## CRUD Operations

### Create
To insert a single record into the collection:
```py
mongo.single_insert({"name": "John Doe", "age": 30, "email": "johndoe@example.com"})
```
To insert a JSON file into the collection:
```py
json_file_path = 'example.json'
mongo.bulk_insert(json_file_path)
```
To insert a CSV file into the collection:
```py
csv_file_path = 'example.csv'
mongo.bulk_insert(csv_file_path)
```

### Read
To load the data from the MongoDB database to a pandas DataFrame:
```py
df = mongo.load_data()
df.head()
```

### Update
To update the records in the collection:
```py
mongo.update_data({"name": "John Doe"},{"$set": {"age": 31}})
```

### Delete
To delete records in the collection:
```py
mongo.delete_record({"name": "John Doe"})
```
To delete the entire collection:
```py
mongo.drop_collection()
```
To delete the entire database:
```py
mongo.drop_database()
```

# Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

# License
This project is licensed under the MIT License.

# Contact
For any questions or suggestions, please contact [yuvaneshkm05@gmail.com](yuvaneshkm05@gmail.com)

# Connect
Connect with me on [LinkedIn](https://www.linkedin.com/in/yuvaneshkm)
