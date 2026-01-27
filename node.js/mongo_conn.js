const {MongoClient} = require('mongodb');

const url = 'mongodb://localhost:27017';
const client = new MongoClient(url);

const dbName = 'my_shop';

async function main() {
    try {
        await client.connect();
        console.log('Successfully connected to the MongoDB');

        const db = client.db(dbName);
        const collection = db.collection('products');

        const insertResult = await collection.insertOne({
            name: "Laptop",
            price: 12000,
            stock: 10
        });
        console.log('Inserted document id: ', insertResult.insertedId);

        const product = await collection.findOne({name: "Laptop"});
        console.log('Found product:', product); 
    } catch(err) {
        console.error('Connection failed: ', err);
    } finally {
        await client.close();
    }
}

main();