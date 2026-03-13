try:
    dollars = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну на євро: "))
    if rate == 0:
        print("Помилка: курс обміну не може дорівнювати нулю")
    else:
        euros = dollars * rate
        print("Сума в євро:", euros)
except ValueError:
    print("Помилка: введено некоректне число.")
finally:
    print("Операція завершена.")
