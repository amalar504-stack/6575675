BALANCE = 1000

try:
    amount = int(input("Введіть суму для зняття: "))
    if amount % 10 != 0 or amount > BALANCE:
        print("Помилка: некоректна сума для зняття")
    else:
        print(f"Ви зняли {amount} грн. Залишок на рахунку: {BALANCE - amount}")
except ValueError:
    print("Помилка: введено некоректне число.")
finally:
    print("Транзакція завершена")