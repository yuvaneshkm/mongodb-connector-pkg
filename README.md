# MongoDB connector package

# Overview
**mdb_connect_pkg** is a Python package designed to simplify the process of connecting to and interacting with MongoDB databases. This package provides a streamlined API for performing CRUD (Create, Read, Update, Delete) operations, handling connections, and managing MongoDB collections with ease.

# Features
* Easy connection management to MongoDB instances
* Simple CRUD operations
* Handling of MongoDB collections

# Directory Structure
```
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
├── requirements_dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── template.py
└── tox.ini
```

# How to use this package
## Installation
To install the package, use pip:
```
pip install mdb-connect-pkg==0.0.4
```
## Usage
### Connecting to MongoDB
First, import the package and create a connection instance:
```
# Importing the package:
from mdb_connect_pkg import mongo_crud

# Initialize the connector:
db_connection_url = 'mongodb://localhost:27017'
database_name = 'mydatabase'
collection_name = 'mycollection'
mongo = mongo_crud.MongoDBConnection(db_connection_url, database_name, collection_name)

# Creating the client and connect to the database:
mongo.create_mongo_client()
mongo.database_()
mongo.collection_()
```
## CRUD Operations
### Create
To insert a single record into the collection:
```
mongo.single_insert({"name": "John Doe", "age": 30, "email": "johndoe@example.com"})
```
To insert a json file into the collection:
```
json_file_path = 'example.json'
mongo.bulk_insert(json_file_path)
```
To insert a csv file into the collection:
```
csv_file_path = 'example.csv'
mongo.bulk_insert(csv_file_path)
```
### Read
To load the data from mongodb database to pandas dataframe:
```
df = mongo.load_data()
df.head()
```
### Update
To update the records in the collection:
```
mongo.update_data({you can use mongodb query here to update any records})
```
### Delete
To delete records in the collection:
```
mongo.delete_record({you can use mongodb query here to delete any records})
```
To delete the entire collection:
```
mongo.drop_collection()
```
To delete the entire database:
```
mongo.drop_database()
```

# Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

# License
This project is licensed under the MIT License.

# Contact
For any questions or suggestions, please contact [Email](yuvaneshkm05@gmail.com)

# Connect
Connect with me on [Linkedin](https://www.linkedin.com/in/yuvaneshkm/)
