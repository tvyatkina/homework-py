# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие буквы "абв"'
print('Исходный текст: ', text)

def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_some_words(text)
print('Измененный текст: ',text)