import matplotlib.pyplot as plt

walking = [1, 1.5, 1, 1, 1, 0.5, 0.5]
friends = [1, 2, 0.5, 1, 1, 2, 2]
studying = [2, 1, 2, 2.5, 3, 3.5, 3]
computer = [5, 5.5, 6, 5.5, 5, 6, 6.5]

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
