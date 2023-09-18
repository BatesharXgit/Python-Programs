#WAP to concatenate two lists 

list1 = ["Good", "Lucky"]
list2 = ["Morning", "Afternoon", "Evening"]

for i in range(len(list2)):
    list3 = list1[0] + " " + list2[i]
    print(list3)
    list4 = list1[1] + " " + list2[i]
    print(list4)

   

#WAP to create a text tuple      of the same size where each integer will presents the length of the corresponding words.