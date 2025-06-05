"""
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

"""


# Doing the first task using functions

country_population = {
    "china": 145,
    "usa": 32,
    "germany": 8,
    "russia": 14,
}

# function to print the dictionary
def print_countries():
    for country, population in country_population.items():
        print(f"{country} ==> {population}")


def add_country():
    new_country = input("Enter the country name to add: ").strip().lower()
    if new_country in country_population:
        print("Country already exist in the dictionary.")
    else:
        try:
            new_population = int(input(f"Enter the population in (crores) of the {new_country}: "))
            country_population[new_country] = new_population
            print(f"{new_country} ==> {new_population} added!")
        except ValueError:
            print("Invalid input!")


def remove_country():
    country_name = input("Enter the country you want to remove: ").strip().lower()
    if country_name in country_population:
        country_population.pop(country_name)
        print(f"{country_name} has been removed. Updated list:")
        for country, population in country_population.items():
            print(f"{country} ==> {population}")
    else:
        print(f"{country_name} does not exist!")        


def query():
    user_query = input("Enter your query for a particular country: ")
    if user_query in country_population:
        print(f"Population of {user_query} is {country_population[user_query]} crores.")
    else:
        print(f"{user_query} does not exist!")


def main():
    prompt = input("Input 'print' to view or 'add' to add or 'remove' to remove or 'query' to check a population of a country: ").strip().lower()

    if prompt == 'print':
        print_countries()

    elif prompt == 'add':
        add_country()

    elif prompt == 'remove':
        remove_country()

    elif prompt == 'query':
        query()

    else:
        print("Invalid prompt given!!!")  

main()