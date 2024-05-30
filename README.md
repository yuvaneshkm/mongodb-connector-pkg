# MongoDB connector package

## Overview
**mdb_connect_pkg** is a Python package designed to simplify the process of connecting to and interacting with MongoDB databases. This package provides a streamlined API for performing CRUD (Create, Read, Update, Delete) operations, handling connections, and managing MongoDB collections with ease.

## Features
* Easy connection management to MongoDB instances
* Simple CRUD operations
* Handling of MongoDB collections

## Installation
To install the package, use pip:
```
pip install mdb_connect_pkg
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
### * Create
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
### * Read