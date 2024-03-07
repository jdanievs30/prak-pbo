class DecoratorExample:
    def decorator_example(func):
        def wrapper(self, *args, **kwargs):
            print(f"Decorator Example: Before {func.__name__}()")
            result = func(self, *args, **kwargs)
            print(f"Decorator Example: After {func.__name__}()")
            return result
        return wrapper

    @decorator_example
    def __init__(self, name):
        self.name = name
        print(f"Constructor Example: Object {self.name} is created.")

    @decorator_example
    def perform_task(self, task):
        print(f"Performing task: {task}")

    @decorator_example
    def __del__(self):
        print(f"Destructor Example: Object {self.name} is destroyed.")

# Membuat instance dari class dengan constructor dan destructor yang didekorasi
obj = DecoratorExample("Object1")

# Memanggil metode dengan decorator
obj.perform_task("Task1")

# Objek akan dihancurkan saat keluar dari scope
