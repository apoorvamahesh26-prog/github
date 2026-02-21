import random
import string

print("Welcome to Password Generator")

length = int(input("Enter the length of password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation


all_characters = lower + upper + digits + symbols

password = "".join(random.choices(all_characters, k=length))

print("Generated Password:", password)
