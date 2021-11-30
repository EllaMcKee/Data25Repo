# Have string variables with 2 words.
# Check whether two words are anagrams of each other.

input1 = "lemon"
input2 = "melon"

list1 = list(input1)
list2 = list(input2)

if len(list1) != len(list2):
    print(f"Nope, {input1} is not an anagram of {input2}.")
elif sorted(list1) == sorted(list2):
    print(f"Yes - {input1} is an anagram of {input2}.")

