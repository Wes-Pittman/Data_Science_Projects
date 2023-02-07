import random

random_height_list = []
random_weight_list = []
random_show_size_list = []

# Generate sample for height between 165cm and 200cm
for height in range(11):
    heights = random.sample(range(150, 200), 1)
    random_height_list.append(heights)
# Generate sample for weight between 165cm and 200cm
for weight in range(11):
    weights = random.sample(range(60, 125), 1)
    random_weight_list.append(weights)
# Generate sample for shoes between 165cm and 200cm
for shoe_size in range(11):
    shoes = random.sample(range(24, 30), 1)
    random_show_size_list.append(shoes)


'''1. zipping the lists, making them into tuples
2. converting the zip objct into a list
3. going through each tuple object, converting them to a list'''
complete_list = list(map(lambda li: list(li), list(
    zip(random_height_list, random_weight_list, random_show_size_list))))


print(complete_list)
