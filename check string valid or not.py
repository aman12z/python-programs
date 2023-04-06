import keyword
words = str(input("enter the string:"))

for i in range (len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],"is keyword in python")
    else:
        print("not keyword",words[i])
