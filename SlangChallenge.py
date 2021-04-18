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
    # total complexity O(text_len * n)
    print(answer)

calculateNGrams(input("Text used for the n-gram:"), input("Number of n items:"))