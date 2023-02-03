aaa = input("ваше речення: ")
bbb = dict()
for word in aaa.split(" "):
  bbb[len(word)] = word

biggest_word = bbb[max(bbb)]
print("найбільше слово в вашому реченні:" + biggest_word)