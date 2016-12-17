contacts = {
    'Ben': {'phone': '201-333-1234', 'twitter': '@neb8', 'github': '@benneb8'},
    'Clair': {'phone': '301-444-5678', 'twitter': '@clai', 'github': '@clair67'},
    'Archie': {'phone': '401-555-9012', 'twitter': '@archi', 'github': '@arthur457'}
}

for contact in sorted(contacts.keys()):
    print("\n{0}'s contact information is:".format(contact))
    for value in sorted(contacts.get(contact).keys()):
        print("{0}: {1}".format(value,contacts.get(contact).get(value)))


print("<table border='1'>")
for contact in sorted(contacts.keys()):
    print("\n<tr><td colspan='3'>{0}</td>".format(contact))
    print("</tr>")
    print("<tr>")
    for value in sorted(contacts.get(contact).keys()):
        print("<td>{0}: {1}</td>".format(value,contacts.get(contact).get(value)))
    print("</tr>")
print("</table>")


with open("contacts.html", "w") as newfile:
    newfile.write("<table border='1'>")
    for contact in sorted(contacts.keys()):
        newfile.write("\n<tr><td colspan='3'>{0}</td>".format(contact))
        newfile.write("</tr>")
        newfile.write("<tr>")
        for value in sorted(contacts.get(contact).keys()):
            newfile.write("<td>{0}: {1}</td>".format(value,contacts.get(contact).get(value)))
        newfile.write("</tr>")
    newfile.write("</table>")
