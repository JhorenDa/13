def tokenize_sentences(text):
    
    sentence_endings = ['.', '!', '?']

    sentences = []
    start = 0
    i = 0
    while i < len(text):
        if text[i] in sentence_endings:
           
            if i+1 < len(text) and not text[i].isdigit():
                sentences.append(text[start:i].strip())
                start = i + 1
        i += 1
    

    if start < len(text):
        sentences.append(text[start:len(text)-1].strip())

    return sentences


text = "Hello! How are you? I'm doing fine."
sentences = tokenize_sentences(text)
print(sentences)
