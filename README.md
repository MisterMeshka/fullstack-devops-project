#Fullstack DevOps Project

A containerized full-stack application built with **FastAPI, PostgreSQL, Docker Compose, Nginx, SQLAlchemy and Alembic**.

The project was created as a practical DevOps learning project to practice containerization, database management, service networking, health checks and application deployment.

#Architecture

                    ┌──────────────┐
                    │    Client    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Nginx     │
                    │ Reverse Proxy│
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   FastAPI    │
                    │   Backend    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  PostgreSQL  │
                    │   Database   │
                    └──────────────┘

All services run in Docker containers and communicate through a dedicated Docker network.

#Technologies

#Backend

* Python 3.12
* FastAPI
* Uvicorn
* SQLAlchemy
* Alembic
* PostgreSQL

#DevOps / Infrastructure

* Docker
* Docker Compose
* Nginx
* Linux
* Git / GitHub
* Docker networking
* Docker volumes
* Container health checks

#Project Structure

fullstack-devops-project/
│
├── backend/
│   ├── alembic/
│   │   └── versions/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── database.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── alembic.ini
│
├── nginx/
│   └── nginx.conf
│
├── docker-compose.yml
├── .gitignore
└── README.md

#Docker Architecture

The application consists of three main services:

#Backend

The FastAPI application runs inside its own Docker container.

The container:

* exposes port `8000`
* runs Uvicorn
* connects to PostgreSQL
* provides a `/health` endpoint
* uses a non-root user inside the container

#PostgreSQL

PostgreSQL runs as a separate container.

Database data is stored in a Docker named volume:

postgres-data

This allows database data to persist when the PostgreSQL container is recreated.

#Nginx

Nginx works as a reverse proxy in front of the backend application.

The service exposes port `80` and forwards requests to the FastAPI backend.

#Docker Compose

The complete application can be started with Docker Compose:

bash
docker compose up -d --build

Check running containers:

bash
docker compose ps

View logs:

bash
docker compose logs -f


Stop the application:

bash
docker compose down


#Environment Variables

The project uses environment variables for database configuration.

Create a `.env` file in the project root:

env
POSTGRES_DB=devops_db
POSTGRES_USER=devops
POSTGRES_PASSWORD=your_password

DB_HOST=postgres
DB_PORT=5432

Do not commit the real `.env` file or production credentials to GitHub.

Use `.env.example` to document required environment variables.

#Database Migrations

The project uses **Alembic** for database migrations.

Create a migration:

docker compose exec backend alembic revision --autogenerate -m "migration message"


Apply migrations:

bash
docker compose exec backend alembic upgrade head


Check the current migration:

bash
docker compose exec backend alembic current


# Health Check

The backend provides a health endpoint:

text
GET /health


Docker Compose uses this endpoint to check whether the backend service is responding.

You can test it with:

bash
curl http://localhost/health


#API

The FastAPI application provides REST API endpoints for working with users.

Swagger API documentation is available at:

text
http://localhost/docs


ReDoc:

text
http://localhost/redoc


#Useful Commands

Start containers:

bash
docker compose up -d


Rebuild containers:

bash
docker compose up -d --build

Show containers:

bash
docker compose ps


Show logs:

bash
docker compose logs -f backend


Open a shell inside the backend container:

bash
docker compose exec backend bash


Restart the application:

bash
docker compose restart


Stop containers:

bash
docker compose down


#What I Practiced

This project helped me gain practical experience with:

* Linux command line
* Git and GitHub
* Docker containerization
* Dockerfile creation
* Docker Compose
* Docker networking
* Docker volumes
* PostgreSQL
* FastAPI
* SQLAlchemy
* Alembic database migrations
* Nginx reverse proxy
* Environment variables
* Container health checks
* Debugging container and database connectivity issues

#Future Improvements

Planned improvements:

* [ ] GitHub Actions CI/CD
* [ ] Automated Docker image builds
* [ ] Docker Hub integration
* [ ] Deployment to a VPS
* [ ] HTTPS with Let's Encrypt
* [ ] Application monitoring
* [ ] AWS deployment
* [ ] Infrastructure as Code

#Author

**MisterMeshka**

GitHub: https://github.com/MisterMeshka
