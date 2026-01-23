// Task 3:
// 2. Class Method:
// In node.js, class method is a function defined inside a class that allows object to perform action

class Car {
    total_car = 0;

    constructor() {
        this.total_car += 1;
    }

    sum_of_car() {
        console.log(`Total cars = ${this.total_car}`);
    }
}

const car = new Car();
car.sum_of_car();