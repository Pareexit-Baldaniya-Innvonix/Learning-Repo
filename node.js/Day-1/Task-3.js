// Task 3: Instantiate object from the class
class Car {
    constructor(make, model, year) {
        // 'this' keyward refers to the specific object instance being created or used
        this.make = make;
        this.model = model;
        this.year = year;
    }

    details() {
        console.log(`Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`)
    }
}


const c1 = new Car("Audi", "R8", 2025);
c1.details();