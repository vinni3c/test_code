#playing with lists

items = range(10)
print("List of Items 1-10: ", list(items))

items_list = list(items) #assigns the items list to variable items_list
print ("Every other item on the list starting with 1: ", list(items[1::2]))

items_2_to_7 = items[2:8]
print ("Items 2 - 7:", list(items_2_to_7))

item_list_length = len(items)
print("Total Items:", item_list_length)

reverse_sort = sorted(items, reverse=True)
print("Items in Reverse Order: ", reverse_sort)

print ("Is the list unchanged so far? ", items_list)

print("Reverse and remove the 6th item in the newly reversed list.")
items_list.sort(reverse=True)
items_list.pop(6)

print ("Is the list still unchanged? ", items_list)
print ("Item 3 was removed")
