const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("./database.db", (err) => {
  if (err) {
    return console.error("Error opening database: ", err.message());
  }
  console.log("connected to the sqlite database.");
});

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE
    )`);
});

const name = "John doe";
const email = "john@example.com";

db.run(
  `INSERT INTO users (name, email) VALUES (?, ?)`,
  [name, email],
  function (err) {
    if (err) {
      return console.log(err.message);
    }
    console.log(`A row has been inserted with rowid ${this.lastID}`);
  },
);

const sql = `SELECT * FROM users WHERE id = ?`;
const userId = 1;

db.get(sql, [userId], (err, row) => {
  if (err) {
    return console.error(err.message);
  }
  console.log(row ? row : "No user found");
});

db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log("Closed the database connection.");
});
