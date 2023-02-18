def reservation_table(reservtable1):
    db = {
        "Pautov": "2",
        "Biletskiy": "4"
    }
    return db.get(reservtable1)
reservtable2 = input("Введіть ваше прізвище")
print("Ваш стіл замовлений на стільки чоловік:", reservation_table(reservtable1=reservtable2))
reservtable2 = input("Введіть ваше прізвище")
print("Ваш стіл замовлений на стільки чоловік:", reservation_table(reservtable1=reservtable2))