"""
Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
"""

germany = ["berlin", "munich", "hamburg", "frankfurt", "cologne"]
switzerland = ["zurich", "geneva", "bern", "lausanne", "basel"]
uk = ["london", "manchester", "birmingham", "glasgow", "liverpool"]
us = ["new york", "los angeles", "chicago", "houston", "san francisco"]
australia = ["sydney", "melbourne", "brisbane", "perth", "adelaide"]
new_zealand = ["auckland", "wellington", "christchurch", "hamilton", "dunedin"]
canada = ["toronto", "vancouver", "montreal", "calgary", "ottawa"]
nepal = ["kathmandu", "pokhara", "biratnagar", "lalitpur", "bharatpur"]


city_name1 = input("Enter name of first city: ").lower()
city_name2 = input("Enter name of second city: ").lower()

if city_name1 in india and city_name2 in india:
    print("Both cities are in India.")
elif city_name1 in pakistan and city_name2 in pakistan:
    print("Both cities are in pakistan.")
elif city_name1 in bangladesh and city_name2 in bangladesh:
    print("Both cities are in bangladesh.")
else:
    print("They don't belong to same country")



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

city_name1 = input("Enter name of first city: ")
city_name2 = input("Enter name of second city: ")

found = False

for country, city_list in cities.items():
    if city_name1 in city_list and city_name2 in city_list:
        print(f"Both the cities are in {country.title()}")
        found = True
        break

if not found:
    print("Both the cities are from different countries.")