# Database Connections

## How to connect postgreSQL(RDBMS) in terminal:

- Using `sudo -u postgres psql` command, access the psql (shell) which is used for executing queries.

### Common meta-commands for postgreSQL:

1. `\l` - List all databases
2. `\c database_name` - Connect to a specific database
3. `\dt` - Display tables in the current database
4. `\d table_name` - Describe a specific table structure
5. `\q` - Quit the psql shell

## How to connect MySQL(RDBMS) in terminal:

- Using `mysql -u root -p` command, access the MySQL shell which is used for executing queries.

### Common meta-commands for MySQL:

1. `SHOW DATABASES;` - List all databases
2. `USE database_name;` - Connect to a specific database
3. `SHOW TABLES;` - Display tables in the current database
4. `DESCRIBE table_name;` - Describe a specific table structure
5. `SELECT DATABASE();` - Check current database
6. `EXIT;` or `QUIT;` - Quit the shell

## How to connect SQLite(RDBMS) in terminal:

- Using `sqlite3` command, access the SQLIte shell which is used for executing queries.

### Common meta-commands for SQLite:

1. `.databases` - List names and files attached with the databases
2. `.tables` - Display tables in the current database
3. `.schema table_name` - Show the `CREATE` statement for a specific table
4. `.header on` - show column name in query results
5. `.mode column` - Format output into clean, redable columns
6. `.quit` or `.exit` - Exit the SQLite shell

## How to connect MongoDB(NoSQL) in terminal:

- Using `sudo systemctl start mongod` and `mongosh` command, access the connection which is used for connting with MongoDB Compass.

### Common meta-commands for MongoDB:

1. `show dbs` - List all databases
2. `use database_name` - Switch to a database
3. `db` - check current database
4. `show collections` - List collections of tables
5. `db.help()` - Get help/manual
6. `exit` or `quit()` - Exit the shell