if __name__ == '__main__':
    Word = input("Введите словосочетание ")
    for i in range(len(Word)):
         if (Word[i] == 'ч' or Word[i] == 'щ') and Word[i + 1] != 'а':
            input("Вы написали все верно")
    else:
        r =Word.replace('е', 'а') and Word.replace('у', 'а')
        print("Исправленное букво сочетание:", r)
        input("Вы написали буквосочетание неверно ")







