# put your code here.
def counts_words(file):

    poem = open(file)

    words_dict = {}

    for line in poem:
        words = line.rstrip().split(" ")

        for word in words:
            word = word.lower()
            if word.endswith(",") or word.endswith(".") or word.endswith("?"):
                print(word)
                word = word.replace(".", "")
                word = word.replace(",", "")
                word = word.replace("?", "")
                print(word)
            words_dict[word] = words_dict.get(word, 0) + 1 

    return words_dict

print(counts_words('test.txt'))



