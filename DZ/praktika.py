students = [["Роман", "Паутов", "13"], ["Илья", "Іванов", "14"], ["Илья", "Селезень", "14"]]
abc = 0
for student in students:
    print(student)
    if "Илья" in student:
        abc += 1
print("Илья зустрічається стільки разів", abc)
