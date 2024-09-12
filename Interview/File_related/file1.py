with open("testing.txt","w+") as file:
    file.write("Hi vasanth is  billionaire")
    for words in file:
        words = words.split()
        print(words)

