x = 50 

def func():
    global x
    print('x дорівнює', x)
    x = 2
    print('Змінюємо глобальне значення x на', x)

func()
print('Значення x складає', x)