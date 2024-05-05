#!/usr/bin/env python3



def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

# Test cases
print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Expected output: [0, 8]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))  # Expected output: ["Hello!", "I'm doing great!", "Python is fun!"]
