names = ["Mike","Tina","Mala","Tony"]
names.append("Anna")    #This adds item to the end of the list
print(names)

names.insert(0,"Gab")    # This adds items to the beginning of the list
print(names)

names.remove("Tina")     #This removes an item in the list
print(names)

names.insert(-1,"Ken")   #This insets an item at a particular point in the list
print(names)

print("Kane" in names) # The 'in" operator checks for items and returns a True or False boolean

names.clear()  #This clears the items on the list
print(names)