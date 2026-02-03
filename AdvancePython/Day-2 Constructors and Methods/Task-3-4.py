# Task 3:
# 4. Accessors:
class Car:
    def __init__(self, brand: str) -> None:
        self._brand: str = brand  # '_(underscore prefix)' means 'internal use'

    @property
    def brand_name(self) -> str:
        return self._brand.upper()


car_brand = Car("BMW")
print(f"Car brand is: {car_brand.brand_name}")
