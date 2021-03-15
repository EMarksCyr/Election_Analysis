# print("Hello World")
# type(3)

# print(5+2*3)
# print(5+9*3/2-4)
# print(5+(9*3/(2-4)))
# counties = ["Arapahoe","Denver","Jefferson"]
# print(counties[-1])
# print(len(counties))
# counties.insert(2,"El Paso")
# print(counties)
# counties.append("El Polko")
# print(counties)
# counties.remove("El Paso")
# print(counties)
# counties.pop(3)
# print(counties)
# counties[2] = "Ragnarok"
# counties = ["Arapahoe","Denver","Jefferson"]
# print(counties)
# counties.append("El Paso")
# counties.remove("Arapahoe")
# print(counties)
# counties[0] = "El Paso"
# counties[2] = "Denver"
# counties.append("Arapahoe")
# print(f"counties: {counties}")
# counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
# print(counties_dict)
# print(len(counties_dict))
# print(counties_dict.keys())
# a = "Arapahoe"
# voting_data = []
# voting_data.append({"county": a, "registered_voters": 422829})
# voting_data.append({"county": "Denver", "registered_voters": 463353})
# voting_data.append({"county": "Jefferson", "registered_voters": 432438})
# print("voting_data: " + str(voting_data))
# "voting_data: {}".format(voting_data)
# print(f"voting_data: {voting_data}")
# #How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(f"from counties: {counties[1]}")
if counties[2] != 'Jefferson':
    print(counties[2])

# temp = int(input("What is the temperature outside?"))
# if temp > 80:
#     print("It's too hot! Turn on the AC")
# else:
#     print("It's not that bad, just open the windows")

# grade = int(input("What is your grade?"))

# if grade >= 90:
#     print("Your grade is an A!")
# elif grade >= 80:
#     print("Your grade is a B!")
# elif grade >= 70:
#     print("Your grade is a C :/")
# elif grade >= 60:
#     print("Your grade is a D :[]")
# else:
#     print("You fail >>>:[]")

# if 'El Paso' in counties:
#     print("El paso is in the list of counties.")
# else: 
#     print("It's not")

# if 'Arapahoe' in counties and  'El Paso' not in counties:
#     print("they are!")
# else:
#     print("one, or both, are not.")
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
# for county in counties:
#     print(county)

# for snake in counties:
#     print(snake)

# for num in range(15):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuple = ("Ark", "Den", "Jeff")
# for county in counties_tuple:
#     print(county)

# counties_dict = {"Ark": 402, "Den": 330, "Jeff": 101}
# for county in counties_dict:
#     print(counties_dict[county])

# for key, value in counties_dict.items():
#     print(key, value)

cake_list = [{"cake": "Vanilla", "frosting": "Chocolate", "price": 12},
    {"cake": "Chocolate", "frosting": "Caramel", "price": 15},
    {"cake": "Matcha", "frosting": "Vanilla", "price": 17}]

# # for cake_dict in cake_list:
# #     print(cake_dict)

# for i in range(len(cake_list)):
#     print(cake_list[i])

# for cake_dict in cake_list:
#         print(cake_dict['price'])

# print(f"You ordered {cake_list[1]} .")

# for cake_dict in cake_list:
#  for cake in cake_dict:
#     print(f"{cake_dict['cake']} cake, with {cake_dict['frosting']} frosting, costs {cake_dict['price']} CAD")


for cake_dict in cake_list:
    print(f"{cake_dict['cake']} cake, with {cake_dict['frosting']} frosting, costs {cake_dict['price']} CAD")