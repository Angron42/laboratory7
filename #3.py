def removeRepetitions(text, chars):
    if not isinstance(chars, list):
        chars = [chars]

    removeIndexes = []
    
    for char in chars:
        allIndexes = text.find_all(char)
        for i in allIndexes:
            if i in removeIndexes:
                continue
            if i != 0:
                if text[i - 1] is char:
                    removeIndexes.append(i)
                    continue
            elif i != len(text) - 1:
                if text[i + 1] is char:
                    removeIndexes.append(i)
    
    newText = ''
    for i in range(len(text)):
        if i in removeIndexes:
            continue
        newText += text[i]

    return newText

text = input('Введите любой текст >> ')

threeDot = text.find_all('...')
text = removeRepetitions(text, ('.', '!', '?'))

simple = text.find_all('.')
interrogative = text.find_all('?')
exclamatory = text.find_all('!')