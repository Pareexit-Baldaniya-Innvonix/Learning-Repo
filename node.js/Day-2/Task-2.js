// Task 2: parameterized constructure
class Movie {
    constructor(name, type, cinema) {
        this.name = name;
        this.type = type;
        this.cinema = cinema;
    }

    info() {
        console.log(`Movie: ${this.name}, Type: ${this.type}, Cinema: ${this.cinema}`);
    }
}

const movie = new Movie("Iron-man", "Action", "IMAX");
movie.info();