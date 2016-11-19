#File Handling
with open("states.csv", "r") as states_file: #.csv or .txt
    #stuff
    states = states_file.read().split("\n") #.split makes it a list not string

    for index, state in enumerate(states):
        # index = 0, state = Alabama
        # index = 1, state = Alaska
        states[index] = state.split(",")#makes a list of lists

#print(states)

#Puts the abbrs and names into lists
state_abbrs = []
state_names = []

for state in states:
    # state = ["AL","Alabama"]
    # state = ["AK","Alaska"]
    state_abbrs.append(state[0])
    state_names.append(state[1])

#print(state_abbrs)
#print(state_names)

#Makes it an html drop down menu
print('<select name = "state">')
print('<option value="">Select State</option>')

for abbr, state in zip(state_abbrs,state_names):
    print('<option value="{0}">{1}</option>'.format(abbr,state))
	
print('</select>')

#Put the menu into an html file
states_option_list = ""
states_option_list += '<select name=stat">'
print(states_option_list)

states_option_list += '\t<option value="">Select a state</option>'

for abbr, name in zip(state_abbrs, state_names):
    states_option_list += '\t<option value="{0}">{1}</option>'.format(abbr,name)

states_option_list += '</select>'

with open("states.html", "w") as new_file:
    new_file.write(states_option_list)


