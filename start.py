# %%
from my_class import MyClass

# %%
# Create an instance of MyClass
my_obj = MyClass()

# %%
# Call the new_func method
my_obj.new_func()
# %%

label = input("Press Enter to continue...")

print(label)


# %%
import random

def generate_random_rating():
    return random.randint(1, 5)

# Example usage:
rating = generate_random_rating()
print(rating)



# %%
from cities import cities


def generate_random_rating1(cities):
    for city in cities:
        for pub in city["pubs"]:
            pub["rating"] = random.randint(1, 5)

generate_random_rating(cities)

for city in cities:
    print(city["name"])
    for pub in city["pubs"]:
        print(f"* {pub['name']}, Address: {pub['address']}, Rating: {pub['rating']} ") 
    print()


def sort_cities_by_rating(cities, reverse_order=False):
    sorted_cities = sorted(cities, key=lambda city: sum(pub["rating"] for pub in city["pubs"]) / len(city["pubs"]), reverse=reverse_order)
    return sorted_cities

# print a line with caption "sorted_cities" and another dashed line
print("sorted_cities")
print("-" * 20) 


# Example usage:
sorted_cities = sort_cities_by_rating(cities)
for city in sorted_cities:
    average_rating = sum(pub["rating"] for pub in city["pubs"]) / len(city["pubs"])
    print(f"{city['name']} - Average Pub Rating: {average_rating:.2f}")

print()

reversed_sorted_cities = sort_cities_by_rating(cities, reverse_order=True)
for city in reversed_sorted_cities:
    average_rating = sum(pub["rating"] for pub in city["pubs"]) / len(city["pubs"])
    print(f"{city['name']} - Average Pub Rating: {average_rating:.2f}")






# %%
