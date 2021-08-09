a, b = int(input("Введите первое число:")), int(input("Введите второе число:"))
c = str(input("Введите символ"))
if c == "-":
    print(a - b)
elif c == "+":
    print(a + b)
elif c == "*":
    print(a * b)
else:
    print("Данные введены некоректно")
