temperature = input("What is the temperature (in degrees)? ")

if int(temperature) > 35:   # tempeture above 40
     print("It is a very hot")
     print("Get very hydrated")

elif int(temperature) > 19: # temperature above 19
     print("It is a nice day")
     print("Go for a nice walk")

elif int(temperature) > 5: # temperature above 5
     print("It is mild")
     print("Have fun")

else:                       # if none of the above conditions is true, then temperature is below 5
     print("It is very cold")
     print("Stay indoors")
print("Done")