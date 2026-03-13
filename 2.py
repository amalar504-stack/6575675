try:
    dollars = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну на євро: "))
    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю")
    euros = dollars * rate
    print(f"Сума в євро: {euros}")
except ValueError:
    print("Помилка: введено некоректне число.")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Операція завершена.")