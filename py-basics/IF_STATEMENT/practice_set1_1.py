"""
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Write a program that asks user to enter a city name and it should tell which country the city belongs to
"""
# Solution 1
germany = ["berlin", "munich", "hamburg", "frankfurt", "cologne"]
switzerland = ["zurich", "geneva", "bern", "lausanne", "basel"]
uk = ["london", "manchester", "birmingham", "glasgow", "liverpool"]
us = ["new york", "los angeles", "chicago", "houston", "san francisco"]
australia = ["sydney", "melbourne", "brisbane", "perth", "adelaide"]
new_zealand = ["auckland", "wellington", "christchurch", "hamilton", "dunedin"]
canada = ["toronto", "vancouver", "montreal", "calgary", "ottawa"]
nepal = ["kathmandu", "pokhara", "biratnagar", "lalitpur", "bharatpur"]

city_name = input("Enter the name of the city: ").lower()

if city_name in india:
    print(f"{city_name} city is in India")
elif city_name in pakistan:
    print(f"{city_name} city is in Pakistan")    
elif city_name in bangladesh:
    print(f"{city_name} city is in Bangladesh")
else:
    print("This city is not form any of these country.")


# Solution 2

cities = {
    "germany": ["berlin", "munich", "hamburg", "frankfurt", "cologne"],
    "switzerland": ["zurich", "geneva", "bern", "lausanne", "basel"],
    "uk": ["london", "manchester", "birmingham", "glasgow", "liverpool"],
    "us": ["new york", "los angeles", "chicago", "houston", "san francisco"],
    "australia": ["sydney", "melbourne", "brisbane", "perth", "adelaide"],
    "new zealand": ["auckland", "wellington", "christchurch", "hamilton", "dunedin"],
    "canada": ["toronto", "vancouver", "montreal", "calgary", "ottawa"],
    "nepal": ["kathmandu", "pokhara", "biratnagar", "lalitpur", "bharatpur"]
}


city_name = input("Enter the name of the city: ").lower()

found = False
for country, city_list in cities.items():
    if city_name in city_list:
        print(f"{city_name.title()} is in {country.title()}")
        found = True
        break

if not found:
    print("This city is not from any of these countries.")

