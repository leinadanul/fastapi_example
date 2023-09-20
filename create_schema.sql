-- Create the "Books" table
CREATE TABLE IF NOT EXISTS books (
    isbn CHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    copies BIGINT NOT NULL
);

-- Create the "Client" table
CREATE TABLE IF NOT EXISTS client (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    rented_book CHAR[]
);



