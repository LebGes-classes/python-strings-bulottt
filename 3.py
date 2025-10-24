text=input('Введите текст:')

replays=[]
count_words=[]
current_word=''
text_split=[]
textsplit=[]
split_list=[]
splitlist=[]
unique_words = []
replays = []

for i in range(len(text)):
    if text[i]!=' ':
        current_word += (text[i])
    else:
        if current_word:
            text_split.append(current_word)
            current_word=''

if current_word:
    text_split.append(current_word)
    current_word=''

for i in range(len(text)):
    split_list.append(text[i])

low_alph='abcdefghijklmnopqrstuvwxyz'
high_alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_rus_alph='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
high_rus_alph='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

for i in range(len(split_list)):
    if split_list[i] in high_alph:
        index=high_alph.find(split_list[i])
        splitlist.append(low_alph[index])
    elif split_list[i] in high_rus_alph:
        index = high_rus_alph.find(split_list[i])
        splitlist.append(low_rus_alph[index])
    else:
        splitlist.append(split_list[i])

words_from_splitlist = []
current_word1 = ''
for i in range(len(splitlist)):
    if splitlist[i] != ' ':
        current_word1 += splitlist[i]
    else:
        if current_word1:
            words_from_splitlist.append(current_word1)
            current_word1 = ''

if current_word1:
    words_from_splitlist.append(current_word1)
    current_word1 = ''

for word in words_from_splitlist:
    if word not in unique_words:
        unique_words.append(word)
        replays.append(words_from_splitlist.count(word))

for i in range(len(unique_words)):
    for j in range(i + 1, len(unique_words)):
        if int(replays[i]) < int(replays[j]):
            unique_words[i], unique_words[j] = unique_words[j], unique_words[i]
            replays[i], replays[j] = replays[j], replays[i]

for i in range(min(5,len(replays))):
    print('слово:', unique_words[i])
    print('повторов:', replays[i])