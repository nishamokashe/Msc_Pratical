''' Count the words in a given sentence '''

def count_words(sentence):
    if sentence.strip() == "":  # Check if the sentence is empty or only contains spaces
        return 0
    else:
        words = sentence.split()  # Split the sentence into words
        return len(words)

sentence = "Please count the words in a given sentence."
word_count = count_words(sentence)

if word_count == 0:
    print("The sentence is empty.")
else:
    print(f"Word count: {word_count}")
