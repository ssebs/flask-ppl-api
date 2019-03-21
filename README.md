# flask-ppl-api

Person Database REST api using flask/sqlite

### Requirements to build/run:
- python3
- pip3
    - pysqlite3
    - flask
    - flask-cors
- sqlite3

### How to Build / Run:
1. Clone this repo
2. install requirements
    1. `$ apt install nodejs npm python3 python3-pip`
    3. `$ pip3 install flask flask-cors pysqlite3 `
3. Run init script for sqlite (optional, should run on first use for python)
    1. `./init_db.sh`
4. Run python file
    1. `$python3 main.py`

### API urls:
- GET
  - `/people/all`
  - e.g.
  ```json
    [
        {
            "id": 1, 
            "first": "Bob", 
            "last": "Smith", 
            "email": "bob.smith+test@example.com"
        }, 
        {
            "id": 2, 
            "first": "Tom", 
            "last": "Selic", 
            "email": "Tom.Selic123@example.com"
        }, 
        {
            "id": 3, 
            "first": "Janie", 
            "last": "Doh", 
            "email": "jdoe45@example.com"
        }, 
        {
            "id": 4, 
            "first": "Giselle M.", 
            "last": "Reyes", 
            "email": "gmr123@example.com"
        }
    ]
  ``` 
  - `/people/bob`
    - e.g.
    ```json
    {
        "id": 1,
        "first": "Bob",
        "last": "Smith",
        "email": "bob.smith+test@example.com"
    }
    ```
  - `/people/1`
    - e.g.
    ```json
    {
        "id": 1,
        "first": "Bob",
        "last": "Smith",
        "email": "bob.smith+test@example.com"
    }
    ```
- POST
  - `/people/create`
  - e.g. json needed
    ```json
    {
        "first":"Janie",
        "last":"Doh",
        "email":"jdoe45@example.com"
    }
    ```
- PATCH
  - `/people/update`
  - e.g. json needed
    ```json
    {
        "id": 3, 
        "first":"Janie",
        "last":"Doh",
        "email":"jdoe45@example.com"
    }
    ```
- DELETE
  - `/people/delete`
  - e.g. json needed
    ```json
    {
        "id": "3"
    }
    ```
