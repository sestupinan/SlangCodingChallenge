def calculateNGrams(text, n):
    n = int(n)
    answer = []
    text_len = len(text)
    for i in range(text_len):
        if i+n <= text_len:
            answer.append(text[i:i+n])
    print(str(answer))


calculateNGrams(input("Text used for the n-gram:"), input("Number of n items:"))