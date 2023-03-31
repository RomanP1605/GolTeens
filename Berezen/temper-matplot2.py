import matplotlib.pyplot as plt
import csv

# відкриваємо csv файл і зчитуємо дані
with open('temperature_data.csv', 'r') as file:
    reader = csv.reader(file)
    # пропускаємо перший рядок з заголовками стовпчиків
    next(reader)
    # створюємо два списки: дати та температури
    dates = []
    temps = []
    for row in reader:
        dates.append(row[31])
        temps.append(row[1])

# побудова графіка температур
plt.plot(dates, temps)
plt.title('Температура')
plt.xlabel('Дата')
plt.ylabel('Температура, °C')
plt.show()

