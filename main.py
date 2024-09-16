def greet(name, age):
    print(f"Hello {name}, you are {age} years old")
person_info = {"name": "Alice", "age": 25}
greet(**person_info)