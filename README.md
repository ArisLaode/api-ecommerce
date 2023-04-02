# Documentation
* Create environment
    ```bash
    pip install virtualenv
    ```
    ```bash
    virtualenv -p python3 env
    ```
* Active environment:
    ```bash
        source env/bin/activate
    ```

* Install all package needed
    ```bash
        pip install -r requirements.txt
    ```
* Setup environment flask
    ```bash
        DB_HOST=localhost
        DB_USERNAME=your-db-username
        DB_PASSWORD=your-db-password
        DB_NAME=your-db-name
    ```

* Setup & Migrate Database 
  - create your database. In this project my database name : ecommerce 
  - create a migration repository
    ```bash
        flask db init
    ```
  - generate migration
    ```bash
        flask db migrate
    ```
  - Migrate script to your database
      ```bash
        flask db upgrade
    ```
* Running API
    ```bash
         bash boot.sh
    ```

* Running via Docker
    ```bash
         
    ```