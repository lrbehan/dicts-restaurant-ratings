"""Restaurant rating lister."""
import sys

input_file = open(sys.argv[1])
restaurant_ratings = {}
for line in input_file:
    line = line.rstrip()
    words = line.split(":")

    restaurants = words[0]
    ratings = words[1]
    

    for word in words:
        restaurant_ratings[restaurants] = ratings
        
def print_the_sorted_ratings():
    sorted_restaurant_ratings = sorted(restaurant_ratings.items())
    for i in range(len(sorted_restaurant_ratings)):
        print(f"{sorted_restaurant_ratings[i][0]} is rated at {sorted_restaurant_ratings[i][1]}.")
        
print_the_sorted_ratings()
print('What is restaurant name?')
new_restaurant = input( ">")
print('What is your rating for this restaurant?')
new_restaurant_rating = input( ">")
restaurant_ratings[new_restaurant]= new_restaurant_rating
print_the_sorted_ratings()
