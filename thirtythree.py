from collections import Counter
# sample text
text = """
Python is an amazing programming language. Python is fun to learn and powerful to use.
"""
# Split text into words and count frequency
words = text.lower().split()
word_count = Counter(words)
# Display word frequencies
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")