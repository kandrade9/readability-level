import re

def readability(text):
    """
    Return grade level of text
    :param text: str
    :return: int
    """
    num_of_letters = letter_count(text)
    num_of_words = word_count(text)
    num_of_sentences = sentence_counter(text)

    L = (num_of_letters / num_of_words) * 100
    S = (num_of_sentences / num_of_words) * 100

    grade_level = 0.0588 * L - 0.296 * S - 15.8
    return grade_level

def letter_count(text):
    """
    Returns the number of letters in text
    :param text: str
    :return: int
    """
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters

def word_count(text):
    """
    Returns the number of words in text
    :param text: str
    :return: int
    """
    words = len(text.split())
    return words

def sentence_counter(text):
    """
    Returns the number of sentences in text
    :param text: str
    :return: int
    """
    sentences = len(re.split("\.|!|\?", text)) - 1
    return sentences

user_sentence = input("Text: ")
result = readability(user_sentence)
print(result)
