print("\nQ1a\n")
# Q1a: Create a class of a country (include continent, climate, language etc in the inputs)


# A1a:
class Country:
    def __init__(self, country_name, continent, climate, language, currency, country_population):
        self.country_name = country_name
        self.continent = continent
        self.climate = climate
        self.language = language
        self.currency = currency
        self.country_population = country_population


chile = Country("Chile", "South America", ["Desert", "Mediterranean", "Oceanic", "Tundra", "Ice Cap"],
                ["Spanish", "Mapundungun", "Aymara", "Rapa Nui", "Quechua"], "Chilean Pesos", 19116201)

print(f"{chile.country_name} is in {chile.continent}. "
      f"\nIt has a {chile.climate} climate."
      f"\nThe languages spoken include {chile.language}."
      f"\nThe currency is {chile.currency}."
      f"\nThe population is {chile.country_population}.")


print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class


# A1b:
class City(Country):

    def __init__(self, city_name, coordinates, elevation, city_population, country_name, continent, climate, language, currency, country_population):
        super().__init__(country_name, continent, climate, language, currency, country_population)
        self.city_name = city_name
        self.coordinates = coordinates
        self.elevation = elevation
        self.city_population = city_population


santiago = City("Santiago", "33.4489° S, 70.6693° W", 570, 5614000,
                "Chile", "South America", ["Desert", "Mediterranean", "Oceanic", "Tundra", "Ice Cap"],
                ["Spanish", "Mapundungun", "Aymara", "Rapa Nui", "Quechua"], "Chilean Pesos", 19116201)

print(f"{santiago.city_name} is at {santiago.coordinates}. "
      f"\nIt sits at {santiago.elevation} metres above sea level."
      f"\nThe population is {santiago.city_population}."
      f"\n{santiago.city_name} is in {santiago.country_name}, which is in {santiago.continent}. "
      f"\nIt has a {santiago.climate} climate."
      f"\nThe languages spoken include {santiago.language}."
      f"\nThe currency is {santiago.currency}."
      f"\nThe population is {santiago.country_population}.")

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


# A2a:
list1 = []
for n in list_of_numbers:
    n = Number(n)
    if n.is_prime():
        print(f"{n.integer} is prime!")
        list1.append(n.integer)
print(f"List of primes: {list1}")

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
list1 = []
for n in list_of_numbers:
    n = Number(n)
    n = n.integer
    if n % 3 == 0:
        if n % 4 == 0:
            print(f"{n} is divisible by both 3 and 4!")
            list1.append(n)

print(f"List of numbers divisible by 3 and 4: {list1}")


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


# class Boss(object):
#     def __init__(self, name, attitude, behaviour, face):
#         name = name
#
#     attitude = attitude
#     behaviour = behaviour
#     face = face
#
#
# def get_attitude(self):
#     return attitude
#
#
# def get_behaviour(self):
#     return behaviour
#
#
# def get_face(self):
#     return face
#
#
# class GoodBoss(Boss):
#     def __init__(self, name, attitude, behaviour, face):
#         super()
#
#
# def encourage(self):
#     print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:
class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face


def get_attitude(self):
    return self.attitude


def get_behaviour(self):
    return self.behaviour


def get_face(self):
    return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)


def encourage(self):
    print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


Bart = Boss("Bart", "Pessimistic", "Great", "Happy")
print(f"{Bart.name}'s attitude is {get_attitude(Bart)}.")
print(f"{Bart.name}'s behaviour is {get_behaviour(Bart)}.")
print(f"{Bart.name}'s face is {get_face(Bart)}.")

Danny = GoodBoss("Danny", "Positive", "Nice", "Cool")
encourage(Danny)
# -------------------------------------------------------------------------------------- #






