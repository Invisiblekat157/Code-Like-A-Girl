#For Loops
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
days_of_week.extend(["Saturday","Sunday"])

for day in days_of_week:
    print (day)

#Nested Loops
for week in range(1, 5):
    print ("week {0}".format(week))

    for day in days_of_week:
        print ("    ", day)
