try:
    order_number = input("Введіть номер замовлення: ")
    if order_number.startswith("ORD") and order_number[3:].isdigit():
        print("Номер замовлення коректний")
    else:
        print("Помилка: неправильний формат номера замовлення")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Перевірка завершена")