#WAP to replace dictionary ca marks values with their average, 

d1 = [{'Roll no.': 101, 'Course': 'Python', 'CA1': 65, 'CA2': 82, 'CA3': 95},
      {'Roll no.': 102, 'Course': 'Python', 'CA1': 72, 'CA2': 82, 'CA3': 88},
      {'Roll no.': 103, 'Course': 'Python', 'CA1': 85, 'CA2': 82, 'CA3': 90},]

for i in d1:
    marks = i['CA1'], i['CA2'], i['CA3']
    average = sum(marks) / len(marks)

    i['CA1'] = average
    i['CA2'] = average
    i['CA3'] = average
    # print(average)
    d1['CA1','CA2','CA3'] = d1[average]
    del [d1['CA1'], ['CA2'], ['CA3']]

for i in d1:
    print(i)