# FastAPI Book API

This is a simple FastAPI based  RESTful API for managing books. It allows you to perform basic operations like adding, showing, deleting, and searching for books in your collection

# Prerequisites 
Check if `python` and `pip` are Installed:

1. Open your terminal and run the following command to check if `python` is already installed 
    ```
    python --version 
    ```
2. Open your terminal and run the following command to check if `pip` is already installed 
    ```
    pip --version 
    ```
`pip` is a package management system usually installed when installing python

To install Python, please check the [Documentation](https://wiki.python.org/moin/BeginnersGuide/Download)



# Installation 
To get stared with this API, follow these steps:

1. Clone this repository to your local machine 
   ```sh
   git clone https://github.com/leinadanul/fastapi_example.git
   ```
2. In the folder of this project Create a virtual environment
    ```
    py -m venv venv 
    ```
3. Activate venv
    ```
    .\venv\Scripts\activate
    ```
4. Install the required dependencies using pip:
    ``` 
    pip install -r requeriments.txt
    ```
5. Run the FastAPi server:
    ```
    uvicorn main:app --reload 
    ```
6. Open docs Swagger UI
    ```
    http://127.0.0.1:8000/docs
    ```

# Example
Here are some example requests and responses:


## Add a new Book

#### Request body:
POST/books

 content-type: application/json
```
{
  "isbn": "6811038951690",
  "title": "Don Quixote",
  "author": "Miguel de Cervantes",
  "genre": "Psychological fiction",
  "copies": 1000
}

``` 

 #### Response body:

```
{
  "isbn": "6811038951690",
  "title": "Don Quixote",
  "author": "Miguel de Cervantes",
  "genre": "Psychological fiction",
  "copies": 1000
}
```

## List of Book

 #### Response body:
 
GET/books

content-type: application/json 

```
[
  {
    "isbn": "1234567891014",
    "title": "string                                                                                                                                                                                                                                                          ",
    "author": "sting                                                                                                                                                                                                                                                       ",
    "genre": "sting                                                                                                                                                                                                                                                 ",
    "copies": 10000
  },
{
    "isbn": "6811038951690",
    "title": "Don Quixote                                                                                                                                                                                                                                                    ",
    "author": "Miguel de Cervantes                                                                                                                                                                                                                                            ",
    "genre": "Psychological fiction                                                                                                                                                                                                                                          ",
    "copies": 1000
  }
]

```










