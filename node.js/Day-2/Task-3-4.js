// Task 3:
// 4. Accessors (Getters):

class Car {
    constructor(brand) {
        this._brand = brand
    }

    get brand_name() {
        return this._brand.toUpperCase();
    }
}

const car = new Car("Audi");
console.log(car.brand_name);