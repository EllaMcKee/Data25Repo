print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:
def divisors(num):
    list1 = []
    for i in range(1, num + 1):
        if num % i == 0:
            list1.append(i)
    return list1


print(divisors(12))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:
def factors(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False


print(factors(8, 4))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def position(letter):
    for i in alphabet:
        if letter == i:
            return alphabet.index(i)


print(position('b'))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:
def id_num(name):
    string1 = ""
    name = name.lower()
    for n in name:
        id_number = alphabet.index(n)
        string1 += str(id_number)
    return string1


print(id_num("bob"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:
def password1(id_num):
    total = 0
    for n in str(id_num):
        total += int(n)
    return id_num - total

# ------------- Two ways to do this: ------------- #
# The first takes input as an integer, and needs to convert it into a string to iterate through.
# The second takes input as a string, and needs to convert it into an integer to operate on.


def password2(id_num):
    total = 0
    for n in id_num:
        total += int(n)
    return int(id_num) - total


print(password1(1141))
print(password2("1141"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:
def prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


print(prime(7))  # Should return True
print(prime(13))  # Should return True
print(prime(20))  # Should return False
print(prime(55))  # Should return False

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
def prime2(number):
    if number.isdigit():
        number = int(number)
        for x in range(2, number):
            if number % x == 0:
                return False
        return True
    else:
        print("Sorry, that isn't a number.")


v = input("Hi! Input a number and I will check if it's prime.\n")
print(f"{v} is prime: {prime2(v)}")

# -------------------------------------------------------------------------------------- #
