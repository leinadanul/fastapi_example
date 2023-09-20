Welcome to the fastapi_example wiki!

# Description 


The Library API database is a crucial component of our project. Its primary purpose is to support operations such as adding, listing, searching, and deleting books within our library application. The database stores and manages key information related to books and clients, enabling our API to provide efficient and accurate services to end-users.


## Database Setup
This section provides step-by-step instructions for setting up the database schema required for the Library API project.

### Prerequisites

- PostgreSQL installed and configured.

### Creating the Database Schema

1. Open a terminal and navigate to the directory containing the `create_schema.sql` file.

2. Execute the SQL script to create the database schema:

 ```
   psql -U your_username -d your_database_name -a -f create_schema.sql
```

Verify the Database Schema has been created


# Another way

If we dont  get `create_schema.sql` file we can create database manually 

## Create Database schema
First we need create a database

```
CREATE DATABASE library
```
The next step we should be create two news tables in the schema 

```
--Create the "Books" table
CREATE TABLE IF NOT EXISTS books (
    isbn CHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    copies BIGINT NOT NULL
);
```
```
-- Create the "Client" table
CREATE TABLE IF NOT EXISTS client (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    rented_book CHAR[]
);
```


