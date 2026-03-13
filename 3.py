try:
    grades_input = input("Введіть оцінки студентів через пробіл: ")
    grades = [int(x) for x in grades_input.split()]
    average = sum(grades) / len(grades)
    print(f"Середній бал: {average}")
except ValueError:
    print("Помилка: всі введені значення повинні бути числами.")
except ZeroDivisionError:
    print("Помилка: список оцінок порожній.")
finally:
    print("Завершення обчислень")