let mysql = require('mysql');

let con = mysql.createConnection ({
    host: "localhost",
    user: "root",
    passwd: "",
    database: "mydb"
});

con.connect(function(err) {
    if(err) throw err;
    console.log("Connected!");
    con.query("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), addr VARCHAR(255))", function(err, result) {
        if(err) throw err;
        console.log("Table created!");
    });
    con.query("INSERT INTO customers (name, addr) VALUES ('John Doe', 'USA')", function(err, result) {
        if(err) throw err;
        console.log("1 record inserted!")
    });
    con.query("SELECT * FROM customers", function(err, result, fields) {
        if(err) throw err;
        console.log(result);
    })
});