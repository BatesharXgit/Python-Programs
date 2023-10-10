#WAP to display top 3 havey prices items in a shop,

items = {'Item1': 75, 'Item2': 45, 'Item3': 99, 'Item4': 46.75, 'Item5': 80.4}

# sorted_items = {'Item3': 99, 'Item5': 80.4, 'Item1': 75, 'Item4': 46.75, 'Item2': 45}
import operator
sorted_items = sorted(items.items(), key=operator.itemgetter(1), reverse=True)

print("Top 3 heavy price items are:")
for item, price in sorted_items[:3]:
    print(item)