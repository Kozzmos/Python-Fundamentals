def delete_the_repeat(inp: str):
    words = inp.split()
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    final = " ".join(result)
    print(final)

inp = "hello I'm burak burak I'm burak"
delete_the_repeat(inp)

def order(sentence: str):
    list = sentence.split()
    list.sort()
    return list

sentence = "Hello, today we will list the words alphabetically with you."
print(order(sentence))
