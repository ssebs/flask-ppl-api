# flask-ppl-api

Person Database REST api using flask/sqlite/sqlalchemy

### Requirements to build/run:
- python3
- pip3
    - pysqlite3
    - flask
    - flask-cors
    - sqlalchemy
    - flask_sqlalchemy
    - flask_migrate
- sqlite3

### How to Build / Run:
1. Clone this repo
2. install requirements
    1. `$ apt install nodejs npm python3 python3-pip`
    3. `$ pip3 install flask flask-cors pysqlite3 sqlalchemy flask_sqlalchemy flask_migrate`
3. Run init script for sqlite
    1. `./initdb.sh`
4. Run python file
    1. `$ python3 run.py`


### API urls:
- GET
  - `/people/`
  - e.g.
  ```json
    [
        {
            "id": 1, 
            "first_name": "Bob", 
            "last_name": "Smith", 
            "email": "bob.smith+test@example.com"
        }, 
        {
            "id": 2, 
            "first_name": "Tom", 
            "last_name": "Selic", 
            "email": "Tom.Selic123@example.com"
        }, 
        {
            "id": 3, 
            "first_name": "Janie", 
            "last_name": "Doh", 
            "email": "jdoe45@example.com"
        }, 
        {
            "id": 4, 
            "first_name": "Giselle M.", 
            "last_name": "Reyes", 
            "email": "gmr123@example.com"
        }
    ]
  ``` 
  - `/people?q=bo`
  - e.g.
  ```json
    [
        {
            "id": 1, 
            "first_name": "Bob", 
            "last_name": "Smith", 
            "email": "bob.smith+test@example.com"
        }
    ]
  ``` 
  - `/people/bob`
    - e.g.
    ```json
    {
        "id": 1,
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith+test@example.com"
    }
    ```
  - `/people/:id`
    - e.g.
    ```json
    {
        "id": 1,
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith+test@example.com"
    }
    ```
- POST
  - `/people/`
  - e.g. json needed
    ```json
    {
        "first_name":"Janie",
        "last_name":"Doh",
        "email":"jdoe45@example.com"
    }
    ```
- PATCH / PUT
  - `/people/:id`
  - e.g. json needed
    ```json
    {
        "id": 3, 
        "first_name":"Jane",
        "last_name":"Doh",
        "email":"jdoe45@example.com"
    }
    ```
- DELETE
  - `/people/:id`
