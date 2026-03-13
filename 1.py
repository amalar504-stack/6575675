try:
    price = float(input("Введіть початкову ціну товару: "))
    discount = float(input("Введіть відсоток знижки: "))
    final_price = price * (1 - discount / 100)
    print(f"Фінальна ціна товару: {final_price}")
except ValueError:
    print("Помилка: введено некоректне число.")