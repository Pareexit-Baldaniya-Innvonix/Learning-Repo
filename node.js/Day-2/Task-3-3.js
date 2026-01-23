// Task 3:
// 3. Static Method:

class WeatherUtils {
    static toFahrenheis(celsius) {
        return (celsius * 1.8) + 32;
    }
}

console.log(WeatherUtils.toFahrenheis(30));