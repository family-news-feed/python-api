## Python Environment Installation Steps

-   Install Python 3
-   Install Pip 20.0+
-   Install VirtualEnv:
    -   ```powershell
        python -m pip install virtualenv --user
        virtualenv --python $env:LocalAppData\Programs\Python\Python38\python.exe venv
        ```
-   Install Python Modules
    -   `pip install django psycopg2 --user`
-   Add to [System Hosts](file:///C:/Windows/System32/drivers/etc/hosts):
    -   `127.0.0.1           localhost`
- Install [PostgreSQL 13](https://www.postgresqltutorial.com/install-postgresql/)
    -   store password for `postgres` user in password manager
    -   don't bother with stack builder, we don't need any add-ins yet
    -   Create a new database user
        -   username: `fnfadmin`
        -   password: generate a strong one and store it in password manager
        -   is super user
        -   can log in
        -   connection limit -1
    -   Create a new local testing database
        -   set owner = `fnfadmin`
        -   set name = `fnf-localtest`
-   Replace the DATABASE password with your own in [./src/configs/dev.py](./src/config/dev.py)
-   Perform database migrations
    -   `python .\src\manage.py makemigrations`
    -   `python .\src\manage.py migrate`

## Running the API

-   Using Powershell:
    -   Activate dev environment
        -   `.\scripts\activate.ps1 dev`
    -   Start the server
        -   `.\scripts\run.ps1`
-   `open http://localhost:8000/`

## Creating a New API Endpoint

-   If using Git Bash:
    -   `chmod u+x scripts/endpoint.sh` (first time only)
    -   `scripts/endpoint.sh <endpointname>`
-   If not using Git Bash:
    -   Copy the folder src/\_template\_ into src/endpoints
    -   Rename the folder to a sensible name
-   Create new URL mappings in [src/FamilyNewsFeed/urls.py](./src/FamilyNewsFeed/urls.py) for the views
