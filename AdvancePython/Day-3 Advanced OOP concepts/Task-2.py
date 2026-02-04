# Task 2:
class DemoClass:
    def instance_method(self) -> str:
        return "Instance method called"

    @classmethod
    def class_method(cls) -> str:
        return "Class method called"

    @staticmethod
    def static_method() -> str:
        return "Static method called"


demo_instance = DemoClass()
print(demo_instance.instance_method())
print(DemoClass.class_method())
print(DemoClass.static_method())
