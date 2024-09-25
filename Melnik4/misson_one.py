import csv
from faker import Faker
import random

# Initialize Faker with Ukrainian locale
fake = Faker('uk_UA')

# Dictionaries for male and female patronymics
male_patronymics = [
    "Олександрович", "Іванович", "Миколайович", "Петрович", "Дмитрович",
    "Андрійович", "Васильович", "Сергійович", "Володимирович", "Юрійович",
    "Анатолійович", "Богданович", "Олегович", "Ілліч", "Романович",
    "Геннадійович", "Максимович", "Євгенович", "Степанович", "Вікторович"
]

female_patronymics = [
    "Олександрівна", "Іванівна", "Миколаївна", "Петрівна", "Дмитрівна",
    "Андріївна", "Василівна", "Сергіївна", "Володимирівна", "Юріївна",
    "Анатоліївна", "Богданівна", "Олегівна", "Іллівна", "Романівна",
    "Геннадіївна", "Максимівна", "Євгенівна", "Степанівна", "Вікторівна"
]

# Create a CSV file with utf-8-sig encoding and write the headers using semicolon as delimiter
with open('people.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')  # Use semicolon as delimiter
    writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження',
                     'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

    # Generate 2000 entries with 60% male and 40% female
    for _ in range(2000):
        gender = random.choice(['male'] * 60 + ['female'] * 40)
        if gender == 'male':
            first_name = fake.first_name_male()
            patronymic = random.choice(male_patronymics)
            last_name = fake.last_name_male()
        else:
            first_name = fake.first_name_female()
            patronymic = random.choice(female_patronymics)
            last_name = fake.last_name_female()

        birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
        position = fake.job()
        city = fake.city()
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()

        # Write a row to the CSV
        writer.writerow([last_name, first_name, patronymic, gender, birth_date,
                         position, city, address, phone, email])

print("Data generation complete. Saved to 'people.csv'.")
