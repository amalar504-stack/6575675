try:
    numbers_input = input("Введіть послідовність чисел через пробіл: ")
    numbers_str = numbers_input.split()
    numbers = []
    for n in numbers_str:
        try:
            numbers.append(float(n))
        except ValueError:
            print(f"Попередження: '{n}' не є числом і буде пропущено")
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Сума: {total}, Середнє: {average}")
except ZeroDivisionError:
    print("Помилка: не введено жодного числа для обчислення")
finally:
    print("Обробка даних завершена")