#Making Strings into Lists

address = "1133 19th St NW Washington, DC 20036"
address_as_list = address.split(" ") #Split at spaces
print (address_as_list)

print ("19" in address)#Finding if its in the string

print ("19" in address_as_list)#Has to match list item exactly
