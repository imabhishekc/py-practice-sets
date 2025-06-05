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

country_dict = {
    "china": 143,
    "usa": 32,
    "russia": 11,
    "germany": 25,
}

prompt = input("Input 'print' to view or 'add' to add or 'remove' to remove or 'query' to check a population of a country: ").strip().lower()

if prompt == 'print':
    for country, population in country_dict.items():
        print(f"{country} ==> {population}")

elif prompt == 'add':
    new_country = input("Enter the country name to add: ").strip().lower()
    if new_country in country_dict:
        print(f"{new_country} already exist!")
    else:
        try:
            new_population = int(input(f"Enter population (in crores) for {new_country}: "))
            country_dict[new_country] = new_population
            print(f"{new_country} ==> {new_population} added to dictionary.")
        except ValueError:
            print("Invalid population input. Please enter a number.")

elif prompt == 'remove':
    country_name = input("Enter the country you want to remove: ").strip().lower()
    if country_name in country_dict:
        country_dict.pop(country_name)
        print(f"{country_name} has been removed. Updated list:")
        for country, population in country_dict.items():
            print(f"{country} ==> {population}")
    else:
        print(f"{country_name} does not exist in the dictionary.")

elif prompt == 'query':
    query_country = input("Enter the country name to view it's population:")
    if query_country in country_dict:
        print(f"Population of {query_country} is {country_dict[query_country]} crores.")
    else:
        print(f"{query_country} does not exist.")