english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

# Читаем строку
s = input()

# Проверяем все условия сразу
if (len(s) == 6 and 
    s[0] in english_alphabet and 
    s[1] in digits and 
    s[2] in digits and 
    s[3] in digits and 
    s[4] in english_alphabet and 
    s[5] in english_alphabet):
    print("YES")
else:
    print("NO")