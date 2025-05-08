### Sorting using lambda function ###
# Example 1: Sorting a list of numbers in ascending order



numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted numbers (ascending):", sorted_numbers)

# Example 2 : Sorting a list of strings by length

words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=len)
print("Sorted words (by length):", sorted_words)

# Example 3 : sorting words in reverse alphabetical order

words = ["apple", "banana", "kiwi", "cherry", "orange", "grape", "pear"]
sorted_words = sorted(words, reverse=True)
print("Sorted words (reverse alphabetical):", sorted_words)


#####sorting using lambda function#####

# Example 1: sorting numbers in descending order

numbers = [5, 2, 9, 1, 5, 6]
sorted_desc = sorted(numbers, key=lambda x:-x)
print("sorted desc", sorted_desc)

# Example 2: sorting a list of dictionaries by a key

user =[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


sorted_users = sorted(user, key=lambda x: x["age"])
print("Sorted_users :", sorted_users)