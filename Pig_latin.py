# It only takes one one at a time for now !
def pig_latin(word):

    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        trans = word+"way"
        return trans
    else:
        trans = word[1:]+word[0]+"ay"
        return trans

      # print(char)


english_word = input("Enter an English word ").lower()
print(pig_latin(english_word))
