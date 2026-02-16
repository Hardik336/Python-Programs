# 8. Write a Python program to perform following operation on given string input:
# a) Count Number of Vowel in given string
# b) Count Length of string (donot use len() )
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not

s = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

length = 0
for ch in s:
    length += 1

print("Length of string:", length)

reverse_str = ""
for ch in s:
    reverse_str = ch + reverse_str

print("Reversed string:", reverse_str)

find_char = input("Enter character to find: ")
replace_char = input("Enter character to replace with: ")

new_str = ""
for ch in s:
    if ch == find_char:
        new_str += replace_char
    else:
        new_str += ch

print("String after find and replace:", new_str)

if s == reverse_str:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")

