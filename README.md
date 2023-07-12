# FastAPI App Deployment and Database Provisioning

This project aims to deploy a FastAPI-powered application on Heroku and provision a SQL database to store basic data, including a user list. The deployment process involves configuring Heroku to run Python, implementing FastAPI framework. Additionally, database provisioning is performed by adding an SQL database type as an add-on on Heroku. Optional tasks include implementing Alembic database migrations and writing a migration to establish the initial database structure.

## Part 2: Deploy Initial FastAPI App

1. Create a Heroku app.
2. Configure the app to run Python and deploy FastAPI.
3. Push the initial FastAPI application code to the dev branch on GitHub.
4. Verify successful auto-deployment to Heroku.
5. Access the `/health` endpoint, which returns a JSON payload with the following structure:

```json
{
  "timestamp": "#",
  "status": "OK"
}
```

6. [BONUS] Enable FastAPI's automatic documentation generator using the `/docs` route.

## Part 3: Provision Database

1. Add an SQL database as an add-on on Heroku (Heroku Postgres).
2. Implement Alembic database migrations to programmatically configure and update the database during each deployment to Heroku.
3. Write a migration to establish the initial database structure based on the following schema and push the migration for successful execution:

**Database Schema:**

Table: `users`
Columns:
- `id` (INT)
- `CreatedAt` (DATE/TIME)
- `LastSeen` (DATE/TIME)
- `IsActive` (BOOL)
- `AccessToken` (TEXT)

4. Verify that the database structure has been successfully deployed to the attached database instance.
5. Extend the JSON response of the `/health` endpoint to include basic database insights:

```json
{
  "timestamp": "#",
  "status": "OK",
  "database": {
    "totalRows": "#",
    "totalTables": "#"
  }
}
```


## Project Setup


- Install pipenv
```commandline
python -m pip install pipenv
```

- Activate pipenv
```commandline
pipenv shell
```

- Install dependency
```commandline
pipenv install
```

- Create and run initial migration 
```commandline
sh initial.sh
```

- Run web-server
```commandline
uvicorn app.main:app --reload
```
You can access the server on http://127.0.0.1:8000


## Database Migrations

- Create database migrations
```commandline
alembic revision --autogenerate -m 'Migration message'
```

- Apply migrations
```commandline
alembic upgrade head 
```

## TESTING
```commandline
pytest app/tests.py
```