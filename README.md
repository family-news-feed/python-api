## Python Environment Installation Steps

-   Install Python 3
-   Install Pip 20.0+
-   Install Python Modules
    -   `python -m pip install django psycopg2 --user`
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
-   Replace the DATABASE password with your own in [./src/FamilyNewsFeed/settings.py](./src/FamilyNewsFeed/settings.py)
-   Perform database migrations
    -   `python src/manage.py makemigrations`
    -   `python src/manage.py migrate`

## Running the API

-   If using Git Bash:
    -   `chmod u+x scripts/run.sh` (first time only)
    -   `scripts/run.sh`
-   `python src/manage.py runserver <port>`
    -   Default port is 8000
-   `open http://localhost:8000/`

## Creating a New API Endpoint

-   If using Git Bash:
    -   `chmod u+x scripts/endpoint.sh` (first time only)
    -   `scripts/endpoint.sh <endpointname>`
-   If not using Git Bash:
    -   Copy the folder src/\_template\_ into src/endpoints
    -   Rename the folder to a sensible name
-   Create new URL mappings in [src/FamilyNewsFeed/urls.py](./src/FamilyNewsFeed/urls.py) for the views
