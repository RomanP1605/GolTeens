import csv
with open('goods_list.txt', encoding='utf-8') as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)
    temperatures=[]
    for row in reader:
        temperature=row[1]
        temperatures.append(temperature)
    print(temperatures)