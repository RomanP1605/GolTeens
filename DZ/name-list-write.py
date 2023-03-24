with open("name_list.txt", "w") as f:
    for i in range(10):
        name = input("Введіть ім'я: ")
        f.write(name + "\n")
print("Імена були записані у файл name_list.txt")
