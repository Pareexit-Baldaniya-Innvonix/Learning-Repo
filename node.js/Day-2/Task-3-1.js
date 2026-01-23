// Task 3:
// 1. Instance method:

class Car {
    constructor() {
        this.color = "Black";
    }

    ShowColor() {
        console.log(`Car color: ${this.color}`)
    }
}

const car = new Car();
car.ShowColor();