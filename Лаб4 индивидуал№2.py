if __name__ == '__main__':
    Word = input("Введите словосочетание ")
    for i in range(len(Word)):
         if (Word[i] == 'ж' or Word[i] == 'ш') and Word[i + 1] != 'и':
            input("Вы написали все верно")
    else:
        r =Word.replace('у', 'а')
        print("Исправленное букво сочетание:", r)
        input("Вы написали буквосочетание неверно ")







