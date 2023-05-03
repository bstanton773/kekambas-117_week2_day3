# Write a function that brings in a word and 
# returns that word with all the vowels removed.
# Y is NOT considered as a vowel
# the starting word will contain upper and lowercase letters


def solution(word):
    output = ''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for letter in word:
        if letter.lower() not in vowels:
            output += letter
    return output
