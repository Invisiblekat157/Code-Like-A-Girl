#My first Program!!!!
addresses = []
QuadrantNW = []
QuadrantNE = []
QuadrantSW = []
QuadrantSE = []

address1 = input("Please type an address.") #Stops for input
address2 = input("Please type another address.")#Ditto
address3 = input("Please type a third address.")#Ditto

addresses.append(address1)
if "NW" in address1 or "nw" in address1:
    QuadrantNW.append(address1)
elif "NE" in address1 or "ne" in address1:
    QuadrantNE.append(address1)
elif "SW" in address1 or "sw" in address1:
    QuadrantSW.append(address1)
elif "SE" in address1 or "se" in address1:
    QuadrantSE.append(address1)
else:
    print ("Your address is not in a quadrant.")

addresses.append(address2)
if "NW" in address2 or "nw" in address2:
    QuadrantNW.append(address2)
elif "NE" in address2 or "ne" in address2:
    QuadrantNE.append(address2)
elif "SW" in address2 or "sw" in address2:
    QuadrantSW.append(address2)
elif "SE" in address2 or "se" in address2:
    QuadrantSE.append(address2)
else:
    print ("Your address is not in a quadrant.")

addresses.append(address3)
if "NW" in address3 or "nw" in address3:
    QuadrantNW.append(address3)
elif "NE" in address3 or "ne" in address3:
    QuadrantNE.append(address3)
elif "SW" in address3 or "sw" in address3:
    QuadrantSW.append(address3)
elif "SE" in address3 or "se" in address3:
    QuadrantSE.append(address3)
else:
    print ("Your address is not in a quadrant.")

print ("NW",QuadrantNW)
print ("NE",QuadrantNE)
print ("SW",QuadrantSW)
print ("SE",QuadrantSE)
