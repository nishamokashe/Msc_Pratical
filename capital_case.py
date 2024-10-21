''' Make the first letter of every word in the given sentence to capital case '''

def capitalize_words(sentence):
    if sentence.strip() == "":  # Check if the sentence is empty or only contains spaces
        return "The sentence is empty."
    else:
        return sentence.title()  # Capitalize the first letter of each word

sentence = "make the first letter of every word capital."
capitalized_sentence = capitalize_words(sentence)

if capitalized_sentence == "The sentence is empty.":
    print(capitalized_sentence)
else:
    print(f"Capitalized Sentence: {capitalized_sentence}")
