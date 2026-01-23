// Task 1: simple constructure

class Size {
    // 'static' keyword allows to access the values directly from the class
    static small = "Small";
    static medium = "Medium";
    static large = "Large";
}

class Toy {
    constructor() {
        this.name = "Teddy";
        this.size = Size.medium;
    }

    info() {
        console.log(`Toy name: '${this.name}' and size: '${this.size}'`)
    }
}

const toy = new Toy();
toy.info();