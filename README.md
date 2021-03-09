# Simple Flask CRUD App with Docker (Create, Read, Update, Delete)

- SQLlite database with SQL-Alchemy 
- "docker-compose up -d" to deploy quickly
- Uses volume for persistent storage
- "docker cp <container_name>:/crud/test.db ./test.db.backup" for backing up the sqllite database
