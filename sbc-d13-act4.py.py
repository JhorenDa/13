word = input("Enter > ")
# wordList = []
# wordList.extend(word.split())
# print(wordList)

prefixes = ["un", "re", "ful", "less", "dis", "pre", "dis", "mis","ness", "ly", "er"]
breakword = []
i = 0
b = -4
while i < len(word):
    w = word[:i]
    hashtag = len(w)
    j = word[b:]
    
    i = i+1 
    b = b - -1
    if w in prefixes:
        breakword.append(w.strip())
        breakword.append(f"{hashtag * '#'}{word[i-1:]}")
        print(breakword)
        break
    else:
        if j in prefixes:
            hashtag2 = len(j)
            breakword.append(f"{word[:b -1]}{hashtag2 * '#'}")
            breakword.append(word[b- 1:])
            print(breakword)

    
        
            
        


    