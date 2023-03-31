import matplotlib.pyplot as plt
import csv

with open('temperature_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    next(data)
    temperatures = []
    dates = []
    for row in data:
        # temperatures.append(str(row[30]))
        temperatures.append(row[11])
        dates.append(row[2])
plt.plot(dates, temperatures)
plt.title("Температура за місяць")
plt.xlabel("Дата")
plt.ylabel("Температура, °C")
plt.gcf().set_size_inches(12, 6)
plt.savefig("temperature_plot.png")
plt.show()
