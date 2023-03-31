with open("name_list.txt", "r") as f:
    names = f.readlines()
    for name in names:
        print("Привіт, " + name.strip())
