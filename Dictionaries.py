#Dictionaries
contacts = {
    "Shannon" : "202-555-1234",
    "Bridgit" : "703-555-9876",
    "Christine" : "410-555-1293"
    }
contacts["Mel"] = "301-555-1111" #Adding to a dictionary

#print(contacts.get("Shannon")) #Reading a dictionary

#Can contain; strings, lists or other dictionaries

contacts2 = {
    "Shannon" : {"phone" : "202-555-1234",
                 "twitter" : "@svt827",
                 "github" : "shannonnvturner"
                 },
    "Bridgit" : {"phone" : "703-555-1222",
                 "github" : "bridgitongithub"
                 },
    "Alison" : {"phone" : "315-555-1111",
                "twitter" : "@alisonjo2786",
                "github" : "alisonjo2786"
                }
    }
#print(contacts2.get("Shannon").get("twitter"))#Put in both keys like this

for contact in sorted(contacts2.keys()):
    print("\n{0}'s info:".format(contact))
    for value in sorted(contacts2.get(contact).keys()):#Follow the Path
        print("{0}: {1}".format(value,contacts2.get(contact).get(value)))#Same
