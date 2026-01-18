items = ["apple", "banana", "orange", "apple", "mango"]

unique_item =  set()
for item in items:
    if(item in unique_item):
        print(f"{item.capitalize} come twice in this items: {items}")
        break
    unique_item.add(item)