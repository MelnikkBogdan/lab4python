import pandas as pd
from datetime import datetime
import os

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

    # Створюємо writer для XLSX файлу
    xlsx_file = 'people_by_age.xlsx'
    with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
        # Записуємо всі дані на аркуш "all"
        df.to_excel(writer, sheet_name='all', index=False)

        # Створюємо фільтри за віковими групами
        df_younger_18 = df[df['Вік'] < 18]
        df_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
        df_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
        df_older_70 = df[df['Вік'] > 70]

        # Записуємо дані на відповідні аркуші
        df_younger_18.to_excel(writer, sheet_name='younger_18', index=False)
        df_18_45.to_excel(writer, sheet_name='18-45', index=False)
        df_45_70.to_excel(writer, sheet_name='45-70', index=False)
        df_older_70.to_excel(writer, sheet_name='older_70', index=False)

    print("Ok")

except FileNotFoundError:
    print(f"Помилка: файл {csv_file} не знайдено.")
except Exception as e:
    print(f"Неможливо створити файл XLSX. Помилка: {e}")
