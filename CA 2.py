# Write a program to create a friend list by taking inputs from the user. Ask the user for his three 
#close friends and shift them at first, second and third positions respectively, in the list, Remove
#one friend from the list who is not in touch for long period. at last, reverse the names of all other
#friends having name length more than 4.

friends = []

for i in range(8):
    name = input("Enter the name of your friend: ")
    friends.append(name)

friend_1 = input("Enter the name of 1st friend: ")
if friend_1 in friends:
    friends.remove(friend_1)
else:
    print("No friend found with name: ", friend_1)

friend_2 = input("Enter the name of 2nd friend: ")
if friend_2 in friends:
    friends.remove(friend_2)
else:
    print("No friend found with name: ", friend_2)

friend_3 = input("Enter the name of 3rd friend: ")
if friend_3 in friends:
    friends.remove(friend_3)
else:
    print("No friend found with name: ", friend_3)

friends.insert(0, friend_1)
friends.insert(1, friend_2)
friends.insert(2, friend_3)

print(friends)

friend_not_in_touch = input("Enter the name of friend not in touch for long: ")
if friend_not_in_touch in friends:
    friends.remove(friend_not_in_touch)

for i in range(len(friends)):
    if len(friends[i]) > 4:
        friends[i] = friends[i][::-1]

print(friends)

