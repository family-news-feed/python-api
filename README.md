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
-   Ignore changes to the env files
    -   `git update-index --assume-unchanged src/configs/dev.py scripts/activate.ps1`
-   Replace the DATABASE password with your own in [the dev config file](./src/config/dev.py)
-   Set the DJANGO_SECRET_KEY in [the virtualenv activation script](./scripts/activate.ps1)
    -   Ask Ben for new Secret Key
-   Perform database migrations
    -   `python .\src\manage.py makemigrations`
    -   `python .\src\manage.py migrate`

## Running the API

-   Using Powershell:
    -   Activate dev environment
        -   `.\scripts\activate.ps1 dev`
    -   Start the server
        -   `.\scripts\run.ps1`
    -   Deactivate the dev environment
        -   `.\scripts\deactivate.ps1`

## Creating a New API Endpoint

-   Using Powershell:
    -   `.\scripts\endpoint.ps1 <endpoint_name>`
        -   Script will prevent duplicates and empty names
-   Create new URL mappings in [src/FamilyNewsFeed/urls.py](./src/FamilyNewsFeed/urls.py) for the views
