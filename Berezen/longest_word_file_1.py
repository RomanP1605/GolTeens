def longest_word_in_file(file_1):
    file = open(file_1, 'r', encoding='UTF-8')
    max_word=''
    for line in file:
        words=line.split()
        for word in words:
            word_without_punc=remove_punctuation(word)
            if len(word_without_punc)>=len(max_word):
                max_word=word_without_punc
    return max_word

def remove_punctuation(word):
    from string import punctuation
    for punc in punctuation:
        if punc in word:
            word=word.replace(punc, '')
    return word

print(longest_word_in_file('file_1.txt'))
