// Task 3:
// 5. Mutators (Setters):

class Car {
    constructor(speed) {
        this._speed = speed
    }

    get speed() {
        return `Car speed is ${this._speed} km/h`;
    }
    
    set speed(curSpeed) {
        if(curSpeed < 0) {
            console.log("Speed can not be negative!");
        }
        this._speed = curSpeed;
    }
}

const car = new Car(60);
car.speed = 50;
console.log(car.speed);