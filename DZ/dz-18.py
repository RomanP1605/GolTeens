import matplotlib.pyplot as plt

walking = [1, 1.5, 1, 1, 1, 0.5, 0.5]
friends = [1, 2, 0.5, 1, 1, 2, 2]
studying = [2, 1, 2, 2.5, 3, 3.5, 5]
computer = [3, 2.5, 2, 1.5, 3, 2, 4]

days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця', 'Субота', 'Неділя']

plt.plot(days, walking, label='Прогулянка')
plt.plot(days, friends, label='Час з друзями')
plt.plot(days, studying, label='Навчання')
plt.plot(days, computer, label="Час за комп'ютером")

plt.title('Скільки проводжу часу')
plt.xlabel('Дні тижня')
plt.ylabel('Години')

plt.legend()

plt.show()
