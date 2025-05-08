#####filter without using lambda function#####
# Example 1: Filter even numbers from a list

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

#example 2: Filtering position numbers from a list

def is_positive(num):
    return num > 0

value = [-10, -5, 0, 5, 10, 15]
positive_numbers = filter(is_positive, value)
print("Positive numbers:", list(positive_numbers))

# Example 3 : filtering words in uppercase from a list

def is_uppercase(word):
    return word.isupper()

words = ["HELLO", "world", "PYTHON", "programming"]
uppercase_words = filter(is_uppercase, words)
print("Uppercase words:", list(uppercase_words))



#######filter using lambda function#####

# Example 1: filtering numbers greater than 7

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
greater = list(filter(lambda x: x > 7, numbers))
print("greater:", greater)

#Example 2: filtering lowercase words from a list

words = ["HELLO", "world", "PYTHON", "programming", "JAVA", "c++"]
lowercase = list(filter(lambda x: x.islower(), words))
print("lowercase:", lowercase)