# Tanner Schramm
# UWYO COSC 1010
# 11//19/2024
# Lab 10
# Lab Section: 10
# Sources, people worked with, help given to: I was given help by the TA in parts of the code. I also used Chat GPT to debug and fix the code in parts that did not work correctly. It was able to help me. 
# your
# comments
# here

# import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

def password_crack():
    try:
        with open('hash', 'r') as hash_file:
            hashed=hash_file.read().strip()
    except FileNotFoundError:
        print("Error: 'hash' file not found")
        return
    try:
         with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as rockyou_file:
            for password in rockyou_file:
                password = password.strip()
                if get_hash(password) == hashed: # Goes to the hash file and hashes it from the get_hash function
                    print(f"Password found: {password}")
                    return
    except FileNotFoundError:
        print("Error: 'rockyou.txt' file not found.")

password_crack() # Runs the file 
    
# Answer: 
# Password Found: gopokes
    

    




# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
