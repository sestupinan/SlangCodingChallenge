
def calculateNGrams(text, n):
    n = int(n)
    answer = []
    text_len = len(text)
    # we check for edge cases (if n is bigger than the length of the text, we return the text itself)
    if n >= text_len:
        answer.append(text)
        print(answer)
        return
    # we use python slicing to substring the text to calculate its n-grams.
    # we iterate over the text (O(text_len))
    for i in range(text_len):
        if i+n <= text_len:
            # we slice and append the n-gram in the array (worst case scenario O(n))
            answer.append(text[i:i+n])
    # total time complexity O(text_len * n), space complexity O(n) because of the array of the ngrams.
    print(answer)

def mostFrequentNGRam(text, n):
    n = int(n)
    ngram = ""
    # we use a dictionary and an auxiliary variable to keep track of the biggest ngram.
    biggest = 0
    dic = {}
    text_len = len(text)
    # we check for edge cases (if n is bigger than the length of the text, we return the text itself)
    if n >= text_len:
        print(text)
        return
    # we use python slicing to substring the text to calculate its n-grams.
    # we iterate over the text (O(text_len))
    for i in range(text_len):
        if i+n <= text_len:
            # we slice the n-gram in the array (worst case scenario O(n))
            aux = text[i:i+n]
            # we check if the ngram is in de dictionary (O(1))
            if dic.get(aux):
                dic[aux]+=1
            else:
                dic[aux]=1
            # we check if the current ngram is the most frequent at the moment O(1).
            if dic[aux] > biggest:
                biggest = dic[aux]
                ngram = aux                
    # total time complexity O(text_len * n), space complexity O(n) because of the dictionary.
    print("The most frequent n-gram is: " + ngram)

def menu():
    step = input("Select the step you want to run:\nType '1' for Step 1 and '2' for Step 2\n")
    if step == "1":
        calculateNGrams(input("Text used for the n-gram:"), input("Number of n items:"))
    elif step == "2":
        mostFrequentNGRam(input("Text used for the most frequent n-gram:"), input("Number of n items:"))
    else:
        print("Pick a valid step.")
menu()