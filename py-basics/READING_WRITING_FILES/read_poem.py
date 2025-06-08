"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in your python program and find out words with maximum occurance.
"""

from collections import Counter
import string

# Reading the file
with open('poem.txt', 'r') as file:
    text = file.read()

# Remove punctuation and convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation)).lower()

# Split into words
words = text.split()

# Count word frequency
word_count = Counter(words)

# Find the maximum occurrence
max_count = max(word_count.values())

# Find all words with the maximum occurence
most_common_words = [word for word, count in word_count.items() if count == max_count]

# Display results
print(f"Most frequent words: {most_common_words}")
print(f"Occurences: {max_count}")

file.close()