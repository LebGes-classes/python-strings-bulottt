text=input('Введите текст: ')

split_list = []
text_split=[]
current_word = ''
text_split_reverse=[]

for i in range(len(text)-1,-1,-1):
    split_list.append(text[i])
print('Строка в обратном порядке: ', *split_list,sep='')

for i in range(len(text)):
    if text[i]!=' ':
        current_word+=(text[i])

    if text[i]==' ' and text[i+1]!=' ' or (i+1)==len(text):
        text_split.append(current_word)
        current_word=''

for i in range(len(text_split)-1,-1,-1):
    text_split_reverse.append(text_split[i])
print('Зеркальный вид введенной строки: ', *text_split_reverse)