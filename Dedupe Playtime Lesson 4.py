#Dedupe Playtime
def textfile_to_string(filename):
    """This function takes a file and returns a string of the file contents."""
    with open(filename, "r") as text_file:
        text = text_file.read().split("\n")
    return text

def dedupe(filename1, filename2):
    list1 = textfile_to_string(filename1)
    print("List 1:",list1)
    list2 = textfile_to_string(filename2)
    print("\nList 2:",list2)
    duplicates = []
    for index,value in enumerate(list2):
        if value in list1:
            duplicates.append(value)
        else:
            list1.append(value)
    
    return(list1, duplicates)

(List_of_attendees, Dupes) = dedupe("film_screening_attendees.txt", "happy_hour_attendees.txt")
print("\nDupes: ",Dupes)
print("\nList of Attendees: ",List_of_attendees)
