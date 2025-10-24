text=input('Введите текст: ')

anglalph='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
text_split=[]
textsplit=[]
result=[]
alph=[]
K=0
current_word = ''
vivod = ''
index = 0

for i in range(len(text)):
    if text[i]!=' ' and text[i]!=',' and text[i]!='.':
        current_word += (text[i])
    else:
        text_split.append(current_word)
        current_word=''

for i in range(len(text_split)):
    if text_split[i]!='':
        textsplit.append(text_split[i])

for i in range(len(textsplit)):
    if len(textsplit[i])>K:
        K=len(textsplit[i])


for i in range(len(anglalph)):
    alph.append(anglalph[i])

for i in range(len(textsplit)):
    for j in range(len(textsplit[i])):
        jj=alph.index(textsplit[i][j])
        result.append(alph[jj+K])

for i in range(len(text)):
    if text[i] not in [' ', ',', '.']:
        vivod += result[index]
        index += 1
    else:
        vivod += text[i]

print('Зашифрованный текст:',*vivod,sep='')
print('Число K:',K)