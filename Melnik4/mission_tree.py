import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Функція для обчислення віку
def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Спроба зчитати CSV файл
csv_file = 'people.csv'
try:
    # Завантажуємо CSV файл в DataFrame
    df = pd.read_csv(csv_file, delimiter=';', encoding='utf-8-sig')

    # Перетворюємо стовпець з датами народження на формат datetime
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%Y-%m-%d')

    # Обчислюємо вік для кожної особи
    df['Вік'] = df['Дата народження'].apply(calculate_age)

    print("Ok")

    # Рахуємо кількість чоловіків і жінок
    gender_counts = df['Стать'].value_counts()
    print("\nКількість чоловіків і жінок:")
    print(gender_counts)

    # Побудова діаграми для статі
    gender_counts.plot(kind='bar', color=['blue', 'pink'])
    plt.title('Кількість чоловіків і жінок')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.show()

    # Визначаємо вікові категорії
    bins = [0, 18, 45, 70, 150]
    labels = ['younger_18', '18-45', '45-70', 'older_70']
    df['Вікова категорія'] = pd.cut(df['Вік'], bins=bins, labels=labels, right=False)

    # Рахуємо кількість співробітників у кожній віковій категорії
    age_category_counts = df['Вікова категорія'].value_counts()
    print("\nКількість співробітників у кожній віковій категорії:")
    print(age_category_counts)

    # Побудова діаграми для вікових категорій
    age_category_counts.plot(kind='bar', color='green')
    plt.title('Кількість співробітників у вікових категоріях')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.show()

    # Рахуємо кількість чоловіків і жінок у кожній віковій категорії
    gender_age_counts = df.groupby(['Вікова категорія', 'Стать']).size().unstack()
    print("\nКількість чоловіків і жінок у кожній віковій категорії:")
    print(gender_age_counts)

    # Побудова діаграми для кожної вікової категорії з поділом на стать
    gender_age_counts.plot(kind='bar', stacked=True, color=['blue', 'pink'])
    plt.title('Кількість чоловіків і жінок у вікових категоріях')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.show()

except FileNotFoundError:
    print(f"Помилка: файл {csv_file} не знайдено.")
except Exception as e:
    print(f"Неможливо обробити файл CSV. Помилка: {e}")
