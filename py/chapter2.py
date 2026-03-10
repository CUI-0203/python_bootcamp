#Chapter 2 - String Manipulation

single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line string"""


text = "Python Programming"

print(text[0])  #(first character)
print(text[-1]) #(last character)
print(text[0:6]) #(slice 0 to 5)
print(text[:6]) #(from start to 5)
print(text[7:]) #(7 to end)


name = " Mike the builder "

print(len(name)) # Length
print(name.strip()) # Remove whitespace
print(name.upper()) # Uppercase
print(name.lower()) # Lowercase
print(name.title()) # Title case
print(name.replace("Mike","Mabel")) # Replace


name = "John Wick"
age = 45

message_1 = f"My name is {name} and I am {age} years old." # f-strings
message_2 = "My name is {} and I am {} years old".format(name, age) # str.format()
message_3 = "My name is %s and I am %d years old" % (name, age) # %-formatting

print(message_1)
print(message_2)
print(message_3)


text = """Python is a powerful programming language. It's easy to learn and versatile! You can use Python for web development, data science, and automation. The syntax is clean and readable. This makes Python perfect for beginners and experts alike."""

char_count = len(text)
words = text.split()
word_count = len(words)

sentence_count = text.count(".") + text.count("!")+ text.count("?")


print("Character count:", char_count)
print("Word count:", word_count)
print("Sentence:", sentence_count)
