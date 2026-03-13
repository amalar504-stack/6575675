try:
    order_number = input("Введіть номер замовлення: ")
    
    correct = True
    
    if len(order_number) < 4 or order_number[0] != "O" or order_number[1] != "R" or order_number[2] != "D":
        correct = False
    else:
        for ch in order_number[3:]:
            if ch < "0" or ch > "9":
                correct = False
                break

    if correct:
        print("Номер замовлення коректний")
    else:
        print("Помилка: неправильний формат номера замовлення")

finally:
    print("Перевірка завершена")
