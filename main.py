def greet(name, message = "Привет"):
    print(f"{message}, {name}")

# використовує значення за замовчуванням для message
greet("Олексій")  

# передача власного значення для message
greet("Марія", message="Добрий день")  
