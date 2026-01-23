// Task 5

class CarAge {
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    get age() {
        const currentYear = 2026;
        const calculatedAge = currentYear - this.year;
        return `Car age is ${calculatedAge} years.`;
    }

    set age(newAge) {
        this.year = newAge
    }
}

const info = new CarAge("BMW", "M5", 2024);
console.log(info.make);
console.log(info.model);
console.log(info.year);
console.log(info.age);