# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('Seminar5/homework/homework5_1/text1.txt', 'r', encoding = 'utf-8') as file:
#     s1 = file.readline()
# s2 = "люб"

with open('Seminar5/homework/homework5_1/text2.txt', 'r', encoding = 'utf-8') as file:
    s1 = file.readline()

s2 = "без"

def f(a, b):
    count = 0
    for i in range(len(a) - len(b)):
        if b in a[i:i + len(b)]:
            count += 1
    return count

print(f(s1, s2))
