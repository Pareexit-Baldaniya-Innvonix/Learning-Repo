const {Pool} = require('pg');

// Database creation
async function createDatabase() {
    const pool = new Pool ({
        user: 'postgres',
        host: 'localhost',
        password: 'postgres',
        database: 'student',
        port: 5432
    });

    try {
        await pool.connect();
        await pool.query("CREATE DATABASE test");
        console.log("Database 'test' created successfully.");
    } catch(error) {
        console.log("Error creating database:", error);
    } finally {
        await pool.end();
    }
}

createDatabase();

// Table creation
const pool = new Pool ({
    user: 'postgres',
    host: 'localhost',
    password: 'postgres',
    database: 'test',
    port: 5432,
});


async function createTable() {
    try {
        await pool.query("DROP TABLE IF EXISTS users;");
        const tableQuery = `CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            email VARCHAR(255) UNIQUE
        );`;

        await pool.query(tableQuery);
        console.log("Table 'users' created.");

        const insertQuery = "INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *";
        const newUser = await pool.query(insertQuery, ['Virat', 'virat@india.com']);
        console.log("Inserted user: ", newUser.rows[0]);

        const selectQuery = "SELECT * FROM users";
        const allUsers = await pool.query(selectQuery);
        console.log("Read all users: ");
        console.table(allUsers.rows);

        const updateQuery = await pool.query("UPDATE users SET email = 'kingkohli@cricket.com' RETURNING *");
        console.log("Updated user table: ", updateQuery.rows[0]);
        console.table(updateQuery.rows);
    } catch (error) {
        console.error("Database error: ", error.message);
    } finally {
        await pool.end();
    }
}

createTable();