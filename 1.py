'''
Write a Python program that does the following:

a. Creates an empty dictionary called guests.
b. Asks the user to input the number of guests they'd like to invite to the party.
c. Uses a for loop to prompt the user to input the name and favorite food of each guest. Store this information in a list called guest_info.
d. Appends each guest_info list to the guests dictionary, using the name of the guest as the key and the guest_info list as the value.
e. Once all the guests have been added to the dictionary, print out the complete guest list, including each guest's name and favorite food.
'''

# a. Creates an empty dictionary called guests.
guests = {}

# b. Asks the user to input the number of guests they'd like to invite to the party.
invite = input(
    "Please enter the number of guest you want to invite to the party :- ")
number_of_guests = int(invite)

# c. Uses a for loop to prompt the user to input the name and favorite food of each guest. Store this information in a list called guest_info.
for i in range(number_of_guests):
    guests_info = []
    name = input("what is the guest name :- ")
    food = input("what is the favorite food :- ")
    guests_info.append(name)
    guests_info.append(food)
    # d. Appends each guest_info list to the guests dictionary, using the name of the guest as the key and the guest_info list as the value.
    guests[name] = guests_info

# e. Once all the guests have been added to the dictionary, print out the complete guest list, including each guest's name and favorite food.
print("Here is the guests list :- ")
for name, food in guests.items():
    print("guest " + name + " favorate food is " + food[1])
