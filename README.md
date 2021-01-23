# SQL Injection Sandbox

The project contains a minimal Flask based web server with database backend. The server **intentionally** include SQL injection vulnerabilities. _docker-compose.yml_ include _MariaDB_ and _Postgres_ databases that can be used with the web server.

The idea behind the server is to have a quick sandbox for testing manual SQLi payloads when usage of _sqlmap_ is not an option (_like during OSWE/OSCP exams_).

## Getting Started

- Download missing container images.

  ```bash
  docker-compose pull
  ```

- Set database to be used in [docker-compose.yml](docker-compose.yml) container orchestration file. Comment/uncomment database URL variable in web server environment variables section.

- Build web server container image.

  ```bash
  docker-compose build
  ```

- Launch containers. The server will start with inbuilt _Debug_ functionality turned on. Local source code is going to be mapped to the running container. This means that any changes made locally will get included into the running server.

  ```bash
  docker-compose up -d
  ```

- Review [app/views.py](app/views.py) for available routes and functionality.

## References

- [Connect Flask to a Database with Flask-SQLAlchemy](https://hackersandslackers.com/flask-sqlalchemy-database-models/)
- [From SQL Injection to Shell: PostgreSQL edition](https://pentesterlab.com/exercises/from_sqli_to_shell_pg_edition/course)
- [PayloadsAllTheThings/SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
