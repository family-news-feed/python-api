## Python Environment Installation Steps

-   Install [Python 3.8.6](https://www.python.org/downloads/release/python-386/ "Download Python 3.8.6")
-   Install Pip 20.0+
-   Install VirtualEnv:
    -   ```powershell
        python -m pip install virtualenv --user
        virtualenv --python $env:LocalAppData\Programs\Python\Python38\python.exe venv
        ```
-   Install Python Modules:
    -   `python -m pip install -r requirements.txt`
-   Add to [System Hosts](file:///C:/Windows/System32/drivers/etc/hosts "Click to go to Windows Host File"):
    -   ```
        127.0.0.1           localhost
        127.0.0.1           local.familynewsfeed.com
        ```
-   Install [PostgreSQL 13](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "Download PostgreSQL 13"):
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
-   Ignore changes to the env files:
    -   `git update-index --assume-unchanged src/configs/dev.py scripts/activate.ps1`
-   Replace the DATABASE password with your own in [the dev config file](./src/config/dev.py)
-   Ask Ben for all required environment variables in [the virtualenv activation script](./scripts/activate.ps1)
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
    -   Import views using existing conventions so we keep our views straight