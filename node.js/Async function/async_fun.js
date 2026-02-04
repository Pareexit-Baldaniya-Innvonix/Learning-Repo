fetchUserFromDb = () => {  // function
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({id: 1, name: "Virat"});
        }, 2000);
    });
}

const displayUser = async () => {  // async function
    console.log("Fetching user data...");
    try {
        const user = await fetchUserFromDb();  // await keyword
        console.log("Data retrived: ", user.name);
    } catch(error) {
        console.error("Error: ", error.message);
    }
}

console.log("1. Program started");
displayUser();
console.log("2. Program continuous while data is being fetched...");